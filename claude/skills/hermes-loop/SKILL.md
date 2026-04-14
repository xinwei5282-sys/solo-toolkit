---
name: hermes-loop
description: Hermes Agent 风格的本地编排元技能。用于把任务先路由到正确角色，再按记忆分层落盘，并把重复工作流沉淀为 skills。适用于：设计本地 agent 架构、整理角色与 skills 边界、把经验转成可复用流程、规划日/周复盘机制。
user-invocable: true
argument-hint: "[任务或改造目标]"
---

# Hermes Loop

这个 skill 不直接替代现有角色，而是给本地系统加一层 Hermes Agent 风格的运行框架：

1. **Role Routing**：任务先路由到合适角色
2. **Memory Tiering**：信息按复用价值落到不同存储层
3. **Skill Extraction**：把重复工作提炼成 skills
4. **Review Loop**：定期复盘并修正规则

## 适用场景

- 你准备新增一个 skill，但不确定该放全局还是项目内
- 你发现多个 skills 职责重叠，需要重新切边界
- 你想把聊天中的稳定方法论变成命令、skill、wiki 或规范
- 你要设计多角色协作：`dev`、`pm`、`ui`、`arch`
- 你希望把经验沉淀为长期资产，而不是散在历史会话里

## Step 1: 做角色路由

先回答：

- 这个任务的主角色是谁？
- 需要叠加哪个项目私有 skill？
- 哪些角色只需要提供辅助视角，而不是主导？

默认路由：

- 代码实现、调试、重构 → `dev`
- 需求、业务、方案、优先级 → `pm` / `ba`
- 页面、视觉、交互、体验 → `ui`
- 系统设计、边界、技术风险 → `arch`

## Step 2: 做记忆分层

不要把所有东西都写到一个库里。

### A. 会话层

放短期上下文、最近偏好、上次做到哪一步。

建议位置：
- Hindsight
- 当前会话上下文

### B. 项目层

放当前项目的执行过程、任务状态、开发决策。

建议位置：
- `progress.json`
- `claude-progress.txt`
- 项目内 `.readme/dev-docs/`
- 项目内 `.claude/skills/`

### C. 长期知识层

放可跨项目复用的经验、原则、踩坑、方法。

建议位置：
- `~/knowledge-base/`

### D. 结构化研究层

放需要持续编译、交叉链接、长期查询的主题知识。

建议位置：
- `~/knowledge-wikis/`

## Step 3: 判断是否应该提炼成 skill

如果一项工作满足以下 3 条及以上，就应该考虑提炼：

- 重复执行过至少两次
- 输入输出相对稳定
- 步骤顺序清晰
- 可以被检查和验收
- 与某一类项目或角色强相关

### 落位原则

- 全局通用：`~/.claude/skills/`
- 项目专用：`<project>/.claude/skills/`
- 人格/方法论：`~/.openclaw/agents/*/agent/`
- 结构化研究：`~/knowledge-wikis/`

## Step 4: 做技能边界切分

一个健康的本地 skills 体系应当把以下四类能力分开：

1. **人格与角色**
   - `commands/*.md`
   - `SOUL.md`
   - `AGENTS.md`
   - `IDENTITY.md`

2. **执行技能**
   - 开发、测试、埋点、设计、评审类 skills

3. **长期记忆**
   - hindsight
   - `knowledge-base`

4. **研究型知识库**
   - `llm-wiki`
   - `knowledge-wikis/*`

如果两个 skill 同时在做“同一输入、同一输出、同一流程”的事情，就说明边界有问题，应合并或重新命名。

## Step 5: 任务完成后的 Hermes 闭环

每次完成一个中大型任务后，追加检查：

1. 是否产生了新的长期知识？
2. 是否形成了新的稳定 SOP？
3. 是否暴露了现有角色或 skill 的边界缺陷？

处理方式：

- 新知识 → `knowledge-base` 或 `knowledge-wikis`
- 新 SOP → 新建或更新 skill
- 边界缺陷 → 更新角色说明、命令、触发词或 skill 描述

## 对你当前本地体系的推荐落位

- `~/.claude/commands/`：角色入口
- `~/.openclaw/agents/*/agent/`：人格与角色方法论
- `~/.claude/skills/solo-toolkit`：通用设计与前端能力
- `~/.claude/skills/llm-wiki`：结构化研究型知识库能力
- `~/knowledge-wikis/`：研究主题内容
- 项目内 `.claude/skills/`：项目专有能力

## 使用方式

当用户说下面这些话时，应优先加载本 skill：

- “帮我整理本地 skills 架构”
- “这个能力应该做成 skill 还是命令”
- “怎么把经验沉淀下来”
- “这些 skills 有点重叠，帮我切边界”
- “基于 Hermes Agent 思路改一下我本地体系”
