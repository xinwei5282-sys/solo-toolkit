---
name: skills-audit
description: 周期性审计本地 skills 体系，检查重复能力、边界模糊、失效技能、命名不清、触发不稳、缺失沉淀，并输出结构化治理报告；适合清理和优化全局 skill 库。
user-invocable: true
argument-hint: "[审计范围，可选]"
---

# Skills Audit

这个 skill 用于治理本地 skills 体系，而不是执行某个业务任务。

## 适用场景

- 想做每周 skills review
- 怀疑有重复 skill
- 某些 skill 已经失效或长期不用
- 某类流程已经重复出现，但还没沉淀成 skill
- 不确定某个能力应该放全局还是项目内

## 审计范围

优先检查：

- `~/.claude/commands/`
- `~/.claude/skills/`
- `~/.openclaw/agents/*/agent/`
- 项目内 `.claude/skills/`
- `~/knowledge-base/`
- `~/knowledge-wikis/`
- `~/.claude/SKILLS_REGISTRY.md`

## 审计维度

### 1. 重复能力

检查：

- 两个 skill 是否在做同一输入、同一输出、同一流程
- 项目 skill 是否已覆盖全局 skill
- 某个 command 是否和 skill 边界重叠

### 2. 边界清晰度

检查：

- 角色入口是否越权
- routing skill 是否误变成重技能
- 长期知识是否混入项目文档
- 碎片信息是否被错误塞进 wiki

### 3. 活跃度与有效性

检查：

- 长期不用的 skill
- 已过时但未删除的流程
- 缺失说明或触发词的 skill
- registry 未登记的新增能力

### 4. 缺失沉淀

检查：

- 是否有重复出现 2 次以上的流程仍未沉淀
- 是否有知识应进入 `knowledge-base` 或 `knowledge-wikis`
- 是否有项目私有能力值得抽成全局 skill

## 输出格式

输出一个审计报告，建议格式：

```markdown
# Skills Audit Report

## Summary
- 审计范围
- 主要发现

## Findings
### P1
- ...
### P2
- ...
### P3
- ...

## Recommendations
- Merge
- Split
- Archive
- Promote
- Document
```

## 固定建议动作

每次审计结束后，至少做以下动作之一：

- 更新 `SKILLS_REGISTRY.md`
- 新建 / 合并 / 归档一个 skill
- 补充一个 wiki 条目
- 补一个项目内 skill 的说明

## 周期建议

- 每周一次轻审计
- 每月一次深审计
- 每当新增 2 个以上 skill 后，立即补一次审计
