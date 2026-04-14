---
title: Skill Extraction
type: concept
created: 2026-04-14
updated: 2026-04-14
sources: []
tags: [agent-systems, skills, extraction]
---

# Skill Extraction

## Definition

Skill extraction 是把重复出现、边界明确、输入输出稳定的流程提炼成 skill 或 command 的过程。

## Extraction Heuristics

一个流程若满足以下至少 3 条，通常可视为候选：

- 重复出现至少 2 次
- 输入输出稳定
- 步骤顺序明确
- 结果可验证
- 与某个角色或项目强关联

## Outcomes

- 提炼为全局 skill
- 提炼为项目私有 skill
- 提炼为角色规范或 command

## Related Pages

- [[Local Agent Stack]]
- [[Role Routing]]
- [[Skills Audit]]
