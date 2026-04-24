# 合并 Skill 到 Solo Toolkit

> 这是内部维护命令，不是日常角色入口。默认不建议从主菜单暴露，只在维护 skill 体系时使用。

将新安装的 Skill 自动合并进 solo-toolkit，保持只有一个 Skill 目录。

## 用法

如果用户提供了 skill 路径或名称，直接执行合并：

```bash
python3 ~/.claude/skills/solo-toolkit/scripts/merge-skill.py $ARGUMENTS
```

如果用户想先安装再合并（如 `npx skills add xxx`），按以下步骤：

1. 执行安装命令
2. 找到安装后的 skill 目录（通常在 `~/.claude/skills/` 或 `~/.agents/skills/`）
3. 运行合并脚本

## 合并逻辑

- **角色类 Skill**（含人格提示词） → 生成 OpenClaw Agent（SOUL.md + AGENTS.md + IDENTITY.md）+ Claude Code `/command`
- **工具类 Skill**（含数据/脚本/流程） → 合并进 `solo-toolkit/data/` + 更新 SKILL.md 触发词
- **重复能力** → 提示用户确认是否覆盖

$ARGUMENTS
