---
title: Memory Tiering
type: concept
created: 2026-04-14
updated: 2026-04-14
sources: []
tags: [agent-systems, memory, knowledge]
---

# Memory Tiering

## Definition

Memory tiering 是把信息按复用价值和时间跨度分流到不同层，而不是全部写进同一个地方。

## Current Tiers

- Session context / Hindsight
- Project docs / `progress.json`
- `knowledge-base`
- `knowledge-wikis`

## Principle

- 临时信息不进长期层
- 项目状态不直接进入结构化 wiki
- 结构化主题知识优先进入 `knowledge-wikis`

## Related Pages

- [[Local Agent Stack]]
- [[Role Routing]]
- [[Skill Extraction]]
