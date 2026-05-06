---
name: memory-audit
description: 记忆体检。扫描 ~/.claude/projects/-Users-weiran/memory/ 中所有记忆文件，验证里面引用的具体路径/skill 名/命令名是否仍然存在，生成结构化报告供用户确认。仅校验 project/reference 类记忆，跳过 user/feedback 类（这些不会因系统结构变化而失效）。
user-invocable: true
---

# Memory Audit — 记忆体检

定期校验本地记忆库中的"结构性引用"是否仍然成立。

## 触发场景

- 每月 1 号被 schedule routine 自动调用
- 用户手动调用 `/memory-audit`
- 大量改动 .agents/skills 后用户主动触发

## 执行流程

### Step 1：读取记忆索引

读 `~/.claude/projects/-Users-weiran/memory/MEMORY.md`，列出所有记忆文件。

### Step 2：分类筛选

逐个读 memory 文件，看 frontmatter 里的 `type:` 字段：

| type | 是否校验 | 原因 |
|------|---------|------|
| `project` | ✓ 校验 | 含具体路径、决策、状态，可能过时 |
| `reference` | ✓ 校验 | 是外部系统指针，最容易失效 |
| `user` | ✗ 跳过 | 用户身份/偏好，不会因系统变化失效 |
| `feedback` | ✗ 跳过 | 行为指引，与文件系统无关 |

### Step 3：提取引用

对每个待校验文件，用正则提取以下模式：

- 绝对路径：`/Users/weiran/...`、`~/...`
- skill 名：`~/.agents/skills/<name>/`、`~/.claude/skills/<name>/`
- 命令名：`/<name>` 形式（如 `/dev`、`/review`）
- 项目目录：`<project>/.claude/skills/`

### Step 4：逐项验证

对每个提取到的引用：

```bash
# 路径
[ -e "$path" ] && echo "OK" || echo "MISSING"

# skill
[ -d "$HOME/.agents/skills/$skill" ] || [ -L "$HOME/.claude/skills/$skill" ] && echo "OK" || echo "MISSING"

# 命令
[ -f "$HOME/.claude/commands/${cmd}.md" ] && echo "OK" || echo "MISSING"
```

### Step 5：生成报告

写入 `~/.claude/projects/-Users-weiran/memory/audit-YYYY-MM-DD.md`：

```markdown
# Memory Audit Report — YYYY-MM-DD

## Summary
- 校验文件数：N
- 总引用数：M
- 失效引用：K

## Findings

### memory file: system_setup.md
- ✓ ~/.agents/skills/role-main/persona/SOUL.md
- ✗ ~/some-removed-path/  ← 需要更新
- ✓ /<dev>

### memory file: tools_reference.md
（如有）

## Recommended Actions

1. system_setup.md line 15：删除失效路径 `~/some-removed-path/...`
2. ...

## 用户确认指令
- 批准全部：回复"按报告改"
- 单独处理：回复"改 X，保留 Y"
- 跳过本次：回复"忽略"
```

### Step 6：通知用户

报告生成后：
- 如果是 schedule 触发：通过 PushNotification 发推送（"本月记忆体检：N 项失效待确认"）
- 如果是手动调用：直接打印报告

### Step 7：等待用户决策

**绝不自动修改 memory 文件**。用户确认后才执行修改。

## 不做的事

- 不扫描整个文件系统找新东西（那是 skills-audit 的工作）
- 不校验 user/feedback 类记忆
- 不自动删除或重写 memory 内容
- 不验证记忆里的"判断"或"经验"是否仍然成立（无法机械验证）

## 与 skills-audit 的区别

| skills-audit | memory-audit |
|---|---|
| 检查 skill 体系本身 | 检查 memory 是否反映真实系统 |
| 关注 skills 重复/边界/失效 | 关注 memory 引用是否过时 |
| 扫描 .agents/skills 等目录 | 扫描 memory 目录 |
| 输出 skill 治理建议 | 输出 memory 修正清单 |

两者互补，但目标不同。
