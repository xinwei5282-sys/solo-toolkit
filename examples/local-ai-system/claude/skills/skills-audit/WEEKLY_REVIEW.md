# Weekly Skills Review

## Purpose

每周做一次轻量治理，避免本地能力体系继续无序增长。

这不是深度重构，而是一次 15-30 分钟的固定巡检。

## Fixed Inputs

每次 review 至少检查以下位置：

- `~/.claude/commands/`
- `~/.claude/skills/`
- `~/.claude/SKILLS_REGISTRY.md`
- 常用项目 `.claude/skills/`
- `~/knowledge-base/`
- `~/knowledge-wikis/`

## Weekly Checklist

### 1. New Capabilities

检查本周是否新增了：

- 新 skill
- 新 command
- 新 wiki 主题
- 新的角色说明或规范

如果新增了，确认是否已登记到 `SKILLS_REGISTRY.md`。

### 2. Duplicate / Overlap

检查：

- 是否有两个 skill 现在在做同一件事
- 是否有项目 skill 已完全覆盖全局 skill
- 是否有 routing skill 开始承担执行工作

### 3. Documentation Drift

检查：

- 新建 skill 是否缺少说明
- 触发词是否过时
- wiki 的 `CLAUDE.md` 是否仍是模板态
- `index.md` 是否反映当前页面

### 4. Knowledge Placement

检查：

- 本周新增经验是否应进入 `knowledge-base`
- 本周新增主题知识是否应进入 `knowledge-wikis`
- 是否有本该进 wiki 的内容还留在聊天或项目文档中

### 5. Extraction Opportunities

检查：

- 是否有重复出现至少 2 次的流程仍未沉淀
- 是否有项目能力值得抽为全局 skill
- 是否有全局 skill 应降级为项目内 skill

## Output

每周 review 结束后：

1. 复制 `TEMPLATE.md`
2. 生成当周报告到 `~/.claude/skills-audit-reports/`
3. 至少执行一项修复动作

## Suggested Filename

```text
~/.claude/skills-audit-reports/YYYY-MM-DD-weekly.md
```

## Minimum Success Condition

一次 weekly review 至少满足：

- 有一份报告
- 有一项实际修复
- `SKILLS_REGISTRY.md` 保持最新
