#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Solo Toolkit — Skill 自动合并脚本

用法:
  python3 ~/.claude/skills/solo-toolkit/scripts/merge-skill.py <skill-path>

功能:
  1. 读取新安装的 skill 目录
  2. 分析是"角色"还是"工具"
  3. 角色 → 生成 OpenClaw Agent + Claude Code command
  4. 工具 → 合并进 solo-toolkit/data/ + 更新 SKILL.md 触发词
  5. 清理原始 skill 目录
"""

import os
import sys
import json
import re
import shutil
from pathlib import Path
from datetime import datetime

# ============================================================
# 路径配置
# ============================================================
HOME = Path.home()
SOLO_TOOLKIT = HOME / ".claude" / "skills" / "solo-toolkit"
SKILL_MD = SOLO_TOOLKIT / "SKILL.md"
OPENCLAW_AGENTS = HOME / ".openclaw" / "agents"
CLAUDE_COMMANDS = HOME / ".claude" / "commands"
DATA_DIR = SOLO_TOOLKIT / "data"
WORKFLOWS_DIR = DATA_DIR / "workflows"
BUSINESS_DIR = DATA_DIR / "business"

# ============================================================
# 角色关键词（用于判断 skill 是角色还是工具）
# ============================================================
ROLE_KEYWORDS = [
    "you are a", "you are an", "act as", "role:", "persona:",
    "你是一个", "你是一位", "扮演", "角色:", "身份:",
    "your role is", "as a senior", "as an expert",
    "core competencies", "core values", "personality",
    "work methodology", "工作方法论", "核心能力", "人格",
    "skill_id: bmad", "module: bmm", "module: bmb",
]

TOOL_KEYWORDS = [
    "workflow", "checklist", "template", "script", "data",
    "csv", "search", "analyze", "report", "framework",
    "步骤", "流程", "检查清单", "模板", "脚本", "数据",
    "when to use", "how to use", "触发", "trigger",
]


def read_skill(skill_path: Path) -> dict:
    """读取 skill 目录，解析 SKILL.md 的 frontmatter 和内容"""
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        print(f"  错误: {skill_md} 不存在")
        sys.exit(1)

    content = skill_md.read_text(encoding="utf-8")

    # 解析 YAML frontmatter
    frontmatter = {}
    body = content
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            for line in parts[1].strip().split("\n"):
                if ":" in line:
                    key, val = line.split(":", 1)
                    frontmatter[key.strip()] = val.strip().strip('"').strip("'")
            body = parts[2].strip()

    # 收集附带文件
    extra_files = []
    for f in skill_path.rglob("*"):
        if f.is_file() and f.name != "SKILL.md":
            extra_files.append(f)

    return {
        "path": skill_path,
        "name": frontmatter.get("name", skill_path.name),
        "description": frontmatter.get("description", ""),
        "frontmatter": frontmatter,
        "body": body,
        "extra_files": extra_files,
    }


def classify_skill(skill: dict) -> str:
    """判断 skill 是角色(role)还是工具(tool)"""
    text = (skill["description"] + "\n" + skill["body"]).lower()

    role_score = sum(1 for kw in ROLE_KEYWORDS if kw.lower() in text)
    tool_score = sum(1 for kw in TOOL_KEYWORDS if kw.lower() in text)

    # 如果有明确的角色标志
    if any(kw in text for kw in ["skill_id: bmad", "module: bmm", "module: bmb"]):
        return "role"

    # 如果有脚本或数据文件，大概率是工具
    has_scripts = any(f.suffix in [".py", ".js", ".ts", ".sh"] for f in skill["extra_files"])
    has_data = any(f.suffix in [".csv", ".json", ".html"] for f in skill["extra_files"])
    if has_scripts or has_data:
        tool_score += 3

    if role_score > tool_score:
        return "role"
    return "tool"


def extract_triggers(description: str) -> list:
    """从 description 中提取触发词"""
    # 去掉引号，按常见分隔符拆分
    desc = description.strip('"').strip("'")
    # 提取引号内的短语
    triggers = re.findall(r'"([^"]+)"', desc)
    if not triggers:
        # 按逗号或句号拆分，取前几个有意义的短语
        parts = re.split(r'[,，.。;；]', desc)
        triggers = [p.strip() for p in parts if len(p.strip()) > 2][:5]
    return triggers


def merge_as_tool(skill: dict):
    """将 skill 作为工具合并进 solo-toolkit"""
    name = skill["name"]
    slug = re.sub(r'[^a-z0-9-]', '-', name.lower()).strip('-')

    print(f"  类型: 工具")
    print(f"  合并到: solo-toolkit/data/")

    # 决定放在哪个子目录
    body_lower = skill["body"].lower()
    if any(kw in body_lower for kw in ["market", "business", "startup", "revenue", "metric", "cac", "ltv"]):
        target_dir = BUSINESS_DIR
    elif any(kw in body_lower for kw in ["workflow", "debug", "review", "ship", "qa", "deploy", "test"]):
        target_dir = WORKFLOWS_DIR
    else:
        # 默认放在 data/ 下以 skill 名命名的目录
        target_dir = DATA_DIR / slug
        target_dir.mkdir(parents=True, exist_ok=True)

    # 复制 SKILL.md 内容为参考文档
    target_file = target_dir / f"{slug}.md"
    content = f"# {skill['name']}\n\n"
    if skill["description"]:
        content += f"> {skill['description']}\n\n"
    content += skill["body"]
    target_file.write_text(content, encoding="utf-8")
    print(f"  写入: {target_file}")

    # 复制附带文件
    if skill["extra_files"]:
        for f in skill["extra_files"]:
            rel = f.relative_to(skill["path"])
            dest = target_dir / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(f, dest)
            print(f"  复制: {rel}")

    # 更新 SKILL.md 的 description 触发词
    triggers = extract_triggers(skill["description"])
    if triggers:
        update_skill_md_triggers(name, triggers, f"data/{target_dir.relative_to(DATA_DIR)}/{slug}.md")

    # 更新 SKILL.md body — 添加模块引用
    update_skill_md_module(name, slug, str(target_file.relative_to(SOLO_TOOLKIT)))

    print(f"  完成: {name} 已合并为工具模块")


def merge_as_role(skill: dict):
    """将 skill 作为角色生成 OpenClaw Agent + command"""
    name = skill["name"]
    slug = re.sub(r'[^a-z0-9-]', '-', name.lower()).strip('-')

    # 生成一个简短的中文名（如果有的话）
    cn_name = name
    cn_match = re.search(r'[\u4e00-\u9fff]+', skill["body"])
    if cn_match:
        cn_name = cn_match.group()[:4]

    print(f"  类型: 角色")
    print(f"  生成 Agent: {slug}")

    # 创建 OpenClaw Agent 目录
    agent_dir = OPENCLAW_AGENTS / slug / "agent"
    agent_dir.mkdir(parents=True, exist_ok=True)

    # 生成 IDENTITY.md
    identity = f"""# {name}

- **名称**: {cn_name}
- **角色**: {skill['description'][:100] if skill['description'] else name}
- **ID**: {slug}
- **语言**: 中文
"""
    (agent_dir / "IDENTITY.md").write_text(identity, encoding="utf-8")
    print(f"  写入: IDENTITY.md")

    # 生成 SOUL.md（从 skill body 提取方法论部分）
    soul = f"# {cn_name} — 人格与方法论\n\n{skill['body']}"
    (agent_dir / "SOUL.md").write_text(soul, encoding="utf-8")
    print(f"  写入: SOUL.md")

    # 生成 AGENTS.md（空模板，待用户填充）
    agents_md = f"""# {cn_name} — 工作手册

> 本文件记录 {cn_name} 的具体工作流程和模板。随着项目经验积累持续更新。

## 工作流程

（待补充）

## 模板

（待补充）

## 边界

- **可以做的**：（待定义）
- **需要确认的**：（待定义）
- **不做的**：（待定义）
"""
    (agent_dir / "AGENTS.md").write_text(agents_md, encoding="utf-8")
    print(f"  写入: AGENTS.md")

    # 生成 Claude Code command
    CLAUDE_COMMANDS.mkdir(parents=True, exist_ok=True)
    cmd_file = CLAUDE_COMMANDS / f"{slug}.md"
    cmd_content = f"""# {cn_name}

先加载{cn_name}的人格和工作手册：
1. 阅读 `~/.openclaw/agents/{slug}/agent/SOUL.md`（人格 + 方法论）
2. 阅读 `~/.openclaw/agents/{slug}/agent/AGENTS.md`（工作手册）
3. 阅读 `~/.openclaw/workspace/LESSONS.md`（团队经验教训，避免重复犯错）
4. 阅读 `~/.openclaw/workspace/USER.md`（老板偏好，务必遵循）

以{cn_name}的角色身份工作，执行以下任务：

$ARGUMENTS
"""
    cmd_file.write_text(cmd_content, encoding="utf-8")
    print(f"  写入: /{slug} 命令 → {cmd_file}")

    print(f"  完成: {name} 已生成为 OpenClaw Agent")
    print(f"  调用: 在 Claude Code 中输入 /{slug}")


def update_skill_md_triggers(name: str, triggers: list, ref_path: str):
    """在 SKILL.md 的 description 末尾追加触发词"""
    content = SKILL_MD.read_text(encoding="utf-8")

    # 在 description 的最后一个引号前插入新触发词
    trigger_str = ", ".join(triggers[:5])
    addition = f" {name}: {trigger_str}."

    # 找到 description 行的末尾
    desc_match = re.search(r'(description:\s*")(.*?)(")', content, re.DOTALL)
    if desc_match:
        old_desc = desc_match.group(0)
        new_desc = desc_match.group(1) + desc_match.group(2).rstrip('.') + addition + desc_match.group(3)
        content = content.replace(old_desc, new_desc, 1)
        SKILL_MD.write_text(content, encoding="utf-8")
        print(f"  更新: SKILL.md description 追加触发词")


def update_skill_md_module(name: str, slug: str, ref_path: str):
    """在 SKILL.md body 末尾追加模块引用"""
    content = SKILL_MD.read_text(encoding="utf-8")

    module_section = f"""
### /{slug} — {name}
When triggered by {name} related tasks:
Read: `skills/solo-toolkit/{ref_path}`
"""

    # 追加到文件末尾
    content = content.rstrip() + "\n" + module_section
    SKILL_MD.write_text(content, encoding="utf-8")
    print(f"  更新: SKILL.md 追加模块引用")


def cleanup(skill_path: Path):
    """清理原始 skill 目录和 symlink"""
    skill_name = skill_path.name
    claude_skills = HOME / ".claude" / "skills"
    agents_skills = HOME / ".agents" / "skills"

    # 删除 .claude/skills/ 下的 symlink
    link = claude_skills / skill_name
    if link.is_symlink():
        link.unlink()
        print(f"  清理: symlink {link}")

    # 删除 .agents/skills/ 下的目录
    agent_dir = agents_skills / skill_name
    if agent_dir.is_dir() and not agent_dir.is_symlink():
        shutil.rmtree(agent_dir)
        print(f"  清理: {agent_dir}")

    # 如果原始路径还存在且不是 solo-toolkit
    if skill_path.is_dir() and "solo-toolkit" not in str(skill_path):
        shutil.rmtree(skill_path)
        print(f"  清理: {skill_path}")

    # 更新 .skill-lock.json
    lock_file = agents_skills.parent / ".skill-lock.json"
    if lock_file.exists():
        try:
            lock = json.loads(lock_file.read_text(encoding="utf-8"))
            if skill_name in lock.get("skills", {}):
                del lock["skills"][skill_name]
                lock_file.write_text(json.dumps(lock, indent=2, ensure_ascii=False), encoding="utf-8")
                print(f"  清理: skill-lock.json")
        except (json.JSONDecodeError, KeyError):
            pass


def check_duplicate(skill: dict) -> bool:
    """检查 solo-toolkit 中是否已有同类能力"""
    name_lower = skill["name"].lower()
    desc_lower = skill["description"].lower()

    # 检查现有模块文件
    for f in DATA_DIR.rglob("*.md"):
        existing = f.read_text(encoding="utf-8").lower()
        # 简单的关键词重叠检测
        name_words = set(re.findall(r'\w+', name_lower))
        existing_words = set(re.findall(r'\w+', existing[:500]))
        overlap = name_words & existing_words
        if len(overlap) >= 3:
            print(f"  警告: 可能与 {f.relative_to(SOLO_TOOLKIT)} 重复 (重叠词: {overlap})")
            return True

    return False


# ============================================================
# 主流程
# ============================================================
def main():
    if len(sys.argv) < 2:
        print("用法: python3 merge-skill.py <skill-path>")
        print("")
        print("示例:")
        print("  python3 merge-skill.py ~/.claude/skills/new-skill")
        print("  python3 merge-skill.py ~/.agents/skills/some-skill")
        sys.exit(1)

    skill_path = Path(sys.argv[1]).expanduser().resolve()

    if not skill_path.is_dir():
        print(f"错误: {skill_path} 不是有效目录")
        sys.exit(1)

    print(f"")
    print(f"{'='*60}")
    print(f"Solo Toolkit — Skill 合并")
    print(f"{'='*60}")
    print(f"  来源: {skill_path}")

    # Step 1: 读取
    skill = read_skill(skill_path)
    print(f"  名称: {skill['name']}")
    print(f"  描述: {skill['description'][:80]}...")
    print(f"  附件: {len(skill['extra_files'])} 个文件")

    # Step 2: 检查重复
    is_dup = check_duplicate(skill)
    if is_dup:
        response = input("  已存在同类能力，是否继续合并？(y/N): ").strip().lower()
        if response != 'y':
            print("  已取消")
            sys.exit(0)

    # Step 3: 分类
    skill_type = classify_skill(skill)
    print(f"")

    # Step 4: 合并
    if skill_type == "role":
        merge_as_role(skill)
    else:
        merge_as_tool(skill)

    # Step 5: 清理
    print(f"")
    cleanup(skill_path)

    print(f"")
    print(f"{'='*60}")
    print(f"  合并完成！重启 Claude Code 后生效。")
    print(f"{'='*60}")
    print(f"")


if __name__ == "__main__":
    main()
