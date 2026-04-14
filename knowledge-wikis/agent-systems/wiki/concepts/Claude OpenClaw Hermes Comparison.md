---
title: Claude OpenClaw Hermes Comparison
type: concept
created: 2026-04-14
updated: 2026-04-14
sources: []
tags: [agent-systems, claude, openclaw, hermes, comparison]
---

# Claude OpenClaw Hermes Comparison

## Summary

当前本地系统不是单独运行在 Claude、OpenClaw 或 Hermes 任一框架之上，而是从三者分别借用了不同层级的能力：

- `Claude` 提供本地会话、命令入口和 skills 载入机制
- `OpenClaw` 提供多角色 persona、agent 资产与部分独立技能
- `Hermes` 提供 routing、memory tiering、skills governance、周期复盘的架构启发

因此最准确的描述不是“迁移到了 Hermes”，而是：  
**当前本地系统是一个以 Claude/OpenClaw 为底座、吸收 Hermes 运行哲学的混合栈。**

## High-Level Comparison

| Layer | Claude | OpenClaw | Hermes | Current Local Stack |
|------|--------|----------|--------|---------------------|
| 会话入口 | 强 | 中 | 强 | 主要用 Claude |
| 角色人格 | 中 | 强 | 中 | 主要用 OpenClaw personas |
| 技能执行 | 强 | 中 | 强 | Claude skills + 项目私有 skills |
| 路由层 | 弱 | 中 | 强 | Hermes-style routing layer |
| 记忆分层 | 中 | 中 | 强 | Hindsight + knowledge-base + knowledge-wikis |
| 周期治理 | 弱 | 弱 | 强 | skills-audit + weekly review |

## 1. Claude

### Strengths

- 会话式工作流自然
- 本地 `commands` 与 `skills` 机制直观
- 适合承接日常交互与快速任务切换

### Limitations

- 原生更偏“当前回合能力调度”
- 如果没有额外设计，长期治理和分层沉淀容易不足

### Current Usage

当前本地主要用 Claude 承接：

- `~/.claude/commands/`
- `~/.claude/skills/`
- `SKILLS_REGISTRY.md`
- `skills-audit` 报告流程

## 2. OpenClaw

### Strengths

- 角色人格层表达很强
- `SOUL.md / AGENTS.md / IDENTITY.md` 结构适合做分工
- 已有一些独立技能资产，例如 `daily-stock-analysis`

### Limitations

- 如果没有额外索引和治理，容易变成“角色资产很多，但缺统一总图”

### Current Usage

当前本地主要用 OpenClaw 承接：

- `~/.openclaw/agents/*/agent/`
- 角色人格和工作手册
- 部分独立 domain skills

## 3. Hermes

### Strengths

- routing / skills / memory / cron 是统一 runtime 思维
- 更强调自我治理和自我改进闭环
- skill 体系里既有轻量分类，也有重型 workflow

### Limitations

- 如果全量迁移，代价较高
- 对现有本地体系而言，完全替换并不是当前收益最高的动作

### Current Usage

当前本地主要借用了 Hermes 的这些思想：

- Role routing
- Memory tiering
- Skill extraction
- Weekly / monthly audit
- Registry-driven governance

## Current Design Choice

当前本地系统选择的是：

1. 保留 Claude 作为主要交互与 skills 入口
2. 保留 OpenClaw 作为 persona 和部分 domain skill 资产来源
3. 不直接迁移成 Hermes runtime
4. 但用 Hermes 的运行原则来整理本地架构

## Why This Hybrid Works

这套混合方案的优点是：

- 不需要一次性推翻原体系
- 能继续使用已有角色资产和项目私有 skill
- 通过 routing layer 和 registry，把体系变得更清晰
- 通过 wiki 和 audit，把长期知识沉淀能力补强

## Current Risks

- 仍有一部分流程依赖人工遵守
- OpenClaw / Claude / Hermes 三套概念并存，后续若不持续治理容易再次混乱
- 自动检测和自动同步能力仍缺失

## Related Pages

- [[Local Agent Stack]]
- [[Role Routing]]
- [[Memory Tiering]]
- [[Skills Audit]]
