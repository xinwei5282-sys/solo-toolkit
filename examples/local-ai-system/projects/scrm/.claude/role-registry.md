# Role Registry

> 本文件定义项目内的角色映射。
> **唯一角色真源** 固定为 `~/.openclaw/agents/<role>/agent/`。
> 不在项目内复制人格，不在多处维护角色定义。
> 本文件不是顶层调度器；顶层调度以任务上下文为第一原则。

## 目标

- 让 Claude 和 Codex 都能用同一套本地角色源
- 保持用户习惯不变，继续直接说“绘心”“明策”“龙虾”
- 项目内只维护映射和上下文接入规则，不维护第二套人格

## 单一事实源

- 角色人格、职责、方法论：`~/.openclaw/agents/<role>/agent/`
- Claude 入口包装：`~/.claude/commands/*.md`
- 项目内薄路由：`/Users/weiran/SCRM/.claude/skills/role-router/SKILL.md`

## 角色映射

### `design`

- 中文名：绘心
- 英文别名：ui, ux, designer, design
- 真源目录：`~/.openclaw/agents/design/agent/`
- 核心加载文件：
  - `~/.openclaw/agents/design/agent/IDENTITY.md`
  - `~/.openclaw/agents/design/agent/SOUL.md`
  - `~/.openclaw/agents/design/agent/AGENTS.md`
- 适用任务：
  - 页面结构、交互、视觉层级、设计规范、可用性判断

### `pm`

- 中文名：明策
- 英文别名：pm, product-manager, product
- 真源目录：`~/.openclaw/agents/pm/agent/`
- 核心加载文件：
  - `~/.openclaw/agents/pm/agent/IDENTITY.md`
  - `~/.openclaw/agents/pm/agent/SOUL.md`
  - `~/.openclaw/agents/pm/agent/AGENTS.md`
- 适用任务：
  - 需求分析、业务判断、优先级、PRD、方案取舍

### `lobster`

- 中文名：龙虾
- 英文别名：lobster
- 真源目录：`~/.openclaw/agents/lobster/agent/`
- 核心加载文件：
  - `~/.openclaw/agents/lobster/agent/IDENTITY.md`
  - `~/.openclaw/agents/lobster/agent/SOUL.md`
  - `~/.openclaw/agents/lobster/agent/AGENTS.md`
- 适用任务：
  - 目标挑战、范围收敛、优先级冲突、战略级取舍

### `dev`

- 中文名：开发
- 英文别名：dev, engineer, developer
- 真源目录：`~/.openclaw/agents/dev/agent/`
- 核心加载文件：
  - `~/.openclaw/agents/dev/agent/IDENTITY.md`
  - `~/.openclaw/agents/dev/agent/SOUL.md`
  - `~/.openclaw/agents/dev/agent/AGENTS.md`
- 适用任务：
  - 开发实现、修 bug、调试、重构

### `arch`

- 中文名：架构
- 英文别名：arch, architect
- 真源目录：`~/.openclaw/agents/arch/agent/`
- 核心加载文件：
  - `~/.openclaw/agents/arch/agent/IDENTITY.md`
  - `~/.openclaw/agents/arch/agent/SOUL.md`
  - `~/.openclaw/agents/arch/agent/AGENTS.md`
- 适用任务：
  - 架构、边界、技术选型、复杂系统设计

## 使用原则

1. 角色名是**意图信号**，不是强制执行器。
2. 先判断任务上下文，再决定是否需要某个角色视角。
3. 角色主要用于：
   - 关注点偏置
   - 输出口吻
   - 评审标准
   - 方案取舍方式
4. 角色不应主导：
   - 事实检索
   - 精确代码修复
   - 明确的工具调用流程
   - 本来已经可以靠直接上下文完成的小任务
5. 如果用户同时点多个角色，先判断主导上下文，再决定哪些角色仅作为补充视角。
6. 不复制角色内容到项目目录，避免角色漂移。

## 推荐加载层级

### L0：无角色

适用于：

- 简单查询
- 小型代码修改
- 明确的工具执行
- 只需直接回答的问题

### L1：角色摘要

适用于：

- 需要某个角色的判断口径，但不需要完整人格
- 如“按绘心视角看层级”“按明策视角收敛方案”

做法：

- 只使用本文件中的角色职责与适用任务

### L2：完整角色真源

适用于：

- 复杂评审
- 多轮方案推演
- 需要稳定保持某角色工作方法的长任务

做法：

- 再读取对应 `IDENTITY.md` / `SOUL.md` / `AGENTS.md`

## 维护规则

- 新增角色：只在此文件补映射，不复制人格文本
- 修改角色人格：只改 `~/.openclaw/agents/<role>/agent/`
- 修改 Claude 入口文案：改 `~/.claude/commands/*.md`
- 修改 Codex/项目唤起逻辑：改本项目 `CLAUDE.md` 与 `role-router` skill
