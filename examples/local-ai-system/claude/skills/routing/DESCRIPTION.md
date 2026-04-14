---
description: Routing-layer skills for Hermes-style local agent orchestration. These skills classify requests before execution, decide which role should lead, choose the right memory tier, and determine whether work belongs in project docs, reusable skills, knowledge-base, or structured wikis.
---

# Routing Layer

这不是一个执行 skill，而是本地能力体系中的**路由层分类说明**。

## 目标

在真正加载重技能前，先回答：

1. 这次任务该由哪个角色主导？
2. 该调用哪个重 skill 或项目私有 skill？
3. 信息应落到哪一层记忆？
4. 是否值得沉淀为新 skill、规范或 wiki 条目？

## 当前路由技能

- `hermes-loop`
- `research-routing`
- `productivity-routing`
- `knowledge-routing`
- `agent-architecture-routing`

## 设计原则

- 路由 skill 优先做分类，不承担完整执行
- 重技能负责明确工作流和产物
- 项目私有 skill 优先于全局默认
- 长期结构化主题优先进入 `knowledge-wikis`

## 何时扩展路由层

当某类请求反复出现，且在进入执行前总需要先判断“该走哪层、哪个角色、哪个知识落点”时，应优先新增 routing skill，而不是直接新增另一个重技能。
