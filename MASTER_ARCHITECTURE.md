# Local AI System Master Architecture

本文件是你当前本地 AI 系统的统一蓝图。

目标不是发明一套新体系，而是把你已经安装并实际在用的这些系统收成一套**不打架、可维护、可演化**的总架构：

- `Claude`
- `Codex`
- `gstack`
- `OpenClaw`
- `Qclaw`
- `shared-ai-skills / solo-toolkit`
- `knowledge-base`
- `knowledge-wikis`
- `BMAD-METHOD`

---

## 1. 总原则

你的系统以后按 6 层管理：

1. **Persona Layer**
2. **Routing Layer**
3. **Workflow Layer**
4. **Skill Layer**
5. **Tool Layer**
6. **Memory & Knowledge Layer**

核心原则：

- 一层只解决一类问题
- 每层有唯一的 source of truth
- 高层决定方向，低层负责执行
- 先路由，再执行，再沉淀
- 尽量减少平行体系之间的重复定义

一句话总结：

> `OpenClaw` 管人格，`Hermes` 管路由，`gstack` 管工程工作流，`shared-ai-skills` 管具体能力，`knowledge-base / knowledge-wikis` 管沉淀。

---

## 2. 当前真实资产盘点

### 2.1 Claude 运行层

主要目录：

- `~/.claude/commands/`
- `~/.claude/skills/`
- `~/.claude/projects/`
- 项目内 `<project>/.claude/skills/`

当前作用：

- 人类主要交互入口
- 角色命令入口
- 全局与项目级 skill 挂载点

### 2.2 Codex 运行层

主要目录：

- `~/.codex/skills/`
- `~/.codex/skills/.system/`
- `~/.codex/skills/codex-primary-runtime/`
- `~/.codex/skills/gstack/`

当前作用：

- Codex 自带运行时技能
- system skill / runtime skill / Darwin skill

### 2.3 OpenClaw 角色系统

主要目录：

- `~/.openclaw/agents/*/agent/`
- `~/.openclaw/workspace/`
- `~/.openclaw/skills/`

当前角色：

- `main`
- `arch`
- `dev`
- `pm`
- `design`
- `ops`
- `finance`
- `legal`
- `growth`
- `support`
- `content`
- `trader`

每个角色已有：

- `IDENTITY.md`
- `SOUL.md`
- `AGENTS.md`

这已经是你最完整的人格层资产。

### 2.4 Gstack 工作流系统

主要目录：

- `~/.gstack/repos/gstack`
- `~/.claude/skills/gstack -> ~/.gstack/repos/gstack`

当前作用：

- review
- qa
- ship
- deploy
- browse
- plan reviews
- health / benchmark / canary

这是你最成熟的工程工作流层。

### 2.5 Shared Skills / Solo Toolkit 能力库

主要目录：

- `~/.shared-ai-skills/`
- `~/.shared-ai-skills/solo-toolkit/data/impeccable/`

代表性能力：

- `frontend-design`
- `critique`
- `audit`
- `optimize`
- `extract`
- `llm-wiki`
- `market-research`
- `competitive-brief`
- `prd-writer`
- `summarize`
- `knowledge-routing`
- `research-routing`
- `productivity-routing`
- `agent-architecture-routing`
- `hermes-loop`

这是你最丰富的执行能力层。

### 2.6 Knowledge 层

主要目录：

- `~/knowledge-base`
- `~/ai-system-config/knowledge-wikis/*`

当前主题：

- `agent-systems`
- `trading-thesis`

这已经形成了“通用知识库 + 结构化主题 wiki”双层知识体系。

### 2.7 BMAD-METHOD

主要目录：

- `~/BMAD-METHOD`
- `~/BMAD-METHOD/.cursor/commands`
- `~/BMAD-METHOD/_bmad-output`

当前作用：

- 方法论 / planning artifact / architecture artifact 生成

更适合作为模板库和规划方法库，而不是默认主系统。

### 2.8 Qclaw

主要目录：

- `~/.qclaw`
- `~/.qclaw/agents`
- `~/.qclaw/plugins`
- `~/.qclaw/memory`

当前作用：

- 另一套轻量 agent runtime / plugin / memory 结构

从全局架构角度看，它目前更像“并行试验分支”，不是主轴。

---

## 3. 统一分层模型

## 3.1 Persona Layer

定义：

- 角色身份
- 说话方式
- 方法论偏好
- 角色边界

**唯一 source of truth：**

- `~/.openclaw/agents/*/agent/`

**入口层：**

- `~/.claude/commands/*.md`

规则：

- `commands/*.md` 只做入口，不再承载完整人格正文
- 人格正文一律下沉到 `SOUL.md`
- 角色边界一律下沉到 `AGENTS.md`

当前建议保留的主角色：

- `main`
- `arch`
- `dev`
- `pm`
- `design`
- `ops`

保留但默认非主入口的角色：

- `finance`
- `legal`
- `growth`
- `support`
- `content`
- `trader`

### 关于“龙虾人格”

如果“龙虾人格”要进入主系统，它应被定义为：

- 一个正式角色，落在 `~/.openclaw/agents/lobster/agent/`

或者：

- 某个现有角色的风格变体，而不是散落在别处的 prompt 片段

它不应该直接塞进 skill，也不应该和 workflow 混写。

## 3.2 Routing Layer

定义：

- 判断任务该由谁主导
- 判断走哪个 skill / workflow
- 判断信息落哪里

**唯一 source of truth：**

- `hermes-loop`
- `agent-architecture-routing`
- `knowledge-routing`
- `research-routing`
- `productivity-routing`

推荐职责分配：

- `hermes-loop`
  - 总路由器
  - 先判角色、记忆落点、是否需要技能沉淀
- `agent-architecture-routing`
  - 只处理“系统本身怎么改”
- `knowledge-routing`
  - 只处理信息落点
- `research-routing`
  - 只处理研究任务下一跳
- `productivity-routing`
  - 只处理文档、汇报、整理类下一跳

规则：

- 先经过路由层，再进入重 skill
- 不允许每个角色各自发明独立路由逻辑

## 3.3 Workflow Layer

定义：

- 大型任务按什么流程推进
- 哪些阶段需要 review / QA / deploy / plan

**主工作流引擎：**

- `gstack`

**辅助方法库：**

- `BMAD-METHOD`

规则：

- 工程、上线、review、dogfood、QA 统一优先走 `gstack`
- `BMAD` 作为 planning / architecture / artifact 模板库使用
- `OpenClaw role flow` 负责“谁来主导”，不替代 `gstack` 的工程流程

### 建议分工

- `OpenClaw`
  - 角色身份与协作壳
- `Hermes`
  - 路由与沉淀判断
- `gstack`
  - 工程执行大流程
- `BMAD`
  - 方案模板和规划工件

## 3.4 Skill Layer

定义：

- 完成具体工作流
- 有稳定输入输出
- 能被调用、组合和复用

**主能力库 source of truth：**

- `~/.shared-ai-skills/`
- `~/.shared-ai-skills/solo-toolkit/data/impeccable/`

高频主 skill：

- `frontend-design`
- `critique`
- `audit`
- `optimize`
- `extract`
- `llm-wiki`
- `market-research`
- `competitive-brief`
- `prd-writer`
- `summarize`

二级风格 / 微调 skill：

- `adapt`
- `arrange`
- `bolder`
- `colorize`
- `delight`
- `distill`
- `harden`
- `normalize`
- `onboard`
- `polish`
- `quieter`
- `teach-impeccable`
- `typeset`

规则：

- 高频主 skill 独立保留入口
- 风格类 skill 作为二级 skill，不承担总入口职责
- 项目内 `.claude/skills/` 仅覆盖项目特有规则，不重造全局能力

## 3.5 Tool Layer

定义：

- 浏览器
- MCP
- 插件
- adapter
- runtime-specific execution capability

主要位置：

- `~/.claude/skills/gstack`
- `~/.codex/skills/.system`
- `~/.openclaw/extensions`
- `~/.qclaw/plugins`

规则：

- 工具层只负责“有没有这能力”
- 工具层不承载人格
- 工具层不承载业务工作流

## 3.6 Memory & Knowledge Layer

定义：

- 会话记忆
- 项目级状态
- 长期知识
- 结构化主题研究

推荐分层：

### 会话层

- Claude / Codex / OpenClaw 的当前会话上下文

### 项目层

- 项目内 `.claude/skills/`
- `progress.json`
- 项目内 `.readme/dev-docs/`

### 长期知识层

- `~/knowledge-base`

适合：

- 可跨项目复用的原则
- 经验
- 决策
- 踩坑

### 结构化研究层

- `~/ai-system-config/knowledge-wikis/*`

适合：

- 长期主题
- 多来源编译
- 交叉链接
- 持续查询

规则：

- `knowledge-base` 放通用长期知识
- `knowledge-wikis` 放持续维护的主题知识
- 不要把研究型内容直接塞进普通 knowledge-base

---

## 4. 最终主系统定义

你的主系统以后建议这样定义：

### 4.1 主系统

- **交互壳**：`Claude`
- **人格系统**：`OpenClaw`
- **路由系统**：`Hermes`
- **工程工作流系统**：`gstack`
- **能力主库**：`shared-ai-skills`
- **知识系统**：`knowledge-base + knowledge-wikis`

### 4.2 降级系统

- **BMAD-METHOD**
  - 作为方法库 / 模板库保留
  - 不做默认主入口

- **Qclaw**
  - 作为实验分支 / 备用 runtime 保留
  - 不做主系统 source of truth

### 4.3 不建议继续做的事

- 不再让 `Claude`、`OpenClaw`、`Qclaw` 同时维护一套完整人格定义
- 不再让每个项目复制一份全局 skill 正文
- 不再让 `BMAD` 和 `gstack` 争夺默认工程工作流地位
- 不再把“龙虾人格”写成散落 prompt 片段

---

## 5. 统一入口设计

建议最终对外只保留少数高层入口：

- `/main`
- `/arch`
- `/dev`
- `/pm`
- `/ui`
- `/ops`
- `/research`
- `/knowledge`
- `/review`

### 默认内部流程

1. 入口命令读取对应角色人格
2. 先过 `hermes-loop`
3. 若是系统改造，再过 `agent-architecture-routing`
4. 决定下一跳：
   - `gstack`
   - 全局 skill
   - 项目 skill
   - `BMAD` 模板
   - `knowledge-base`
   - `knowledge-wikis`

---

## 6. Source of Truth 表

| 层 | Source of Truth | 说明 |
|---|---|---|
| Persona | `~/.openclaw/agents/*/agent/` | 人格、方法论、角色边界 |
| Command Entry | `~/.claude/commands/` | 对外入口 |
| Routing | `hermes-loop` + routing skills | 下一跳与落点判断 |
| Workflow | `gstack` | 工程类标准流程 |
| Planning Templates | `BMAD-METHOD` | 模板库，不是主工作流 |
| Skills | `~/.shared-ai-skills/` | 全局能力主库 |
| Project Skills | `<project>/.claude/skills/` | 项目特化规则 |
| General Knowledge | `~/knowledge-base` | 通用长期知识 |
| Structured Knowledge | `~/ai-system-config/knowledge-wikis/` | 主题研究型知识 |

---

## 7. 当前重复与治理建议

### 7.1 人格重复

现状：

- `~/.claude/commands/*.md`
- `~/.openclaw/agents/*/agent/SOUL.md`

建议：

- 保留 command 入口
- 正文只保留在 OpenClaw agent 目录

### 7.2 Skill 正文重复

现状：

- `~/.shared-ai-skills`
- `~/.claude/skills`
- 项目内 `.claude/skills`

建议：

- 正文 source of truth 统一在 `~/.shared-ai-skills`
- `~/.claude/skills` 只做链接层
- 项目内 skill 只保留项目私有差异

### 7.3 工作流重复

现状：

- `gstack`
- `BMAD`
- command-based role orchestration

建议：

- `gstack` 负责工程流
- `BMAD` 负责模板与规划方法
- role orchestration 负责谁主导，不负责替代工程流

### 7.4 知识落点重复

现状：

- `knowledge-base`
- `knowledge-wikis`
- 项目文档
- 会话历史

建议：

- 会话临时信息不要直接进入长期层
- 通用知识进 `knowledge-base`
- 需要编译、交叉引用、长期查询的主题进 `knowledge-wikis`

---

## 8. “龙虾人格”接入规范

如果要正式整合“龙虾人格”，按下面规则：

### 方案 A：作为新角色

创建：

- `~/.openclaw/agents/lobster/agent/IDENTITY.md`
- `~/.openclaw/agents/lobster/agent/SOUL.md`
- `~/.openclaw/agents/lobster/agent/AGENTS.md`
- `~/.claude/commands/lobster.md`

适合：

- 龙虾人格是独立身份
- 有稳定的说话方式、方法论和边界

### 方案 B：作为现有角色变体

例如：

- `dev-lobster`
- `arch-lobster`
- `main-lobster`

适合：

- 它本质不是新职能，只是风格变体

### 不建议的方案

- 直接把龙虾 prompt 塞进 skill
- 在多个 command 里复制同一份人格描述
- 让龙虾人格和现有角色边界重叠但无明确分工

---

## 9. 未来演化路线

### V1

- 确认主系统边界
- 固定 source of truth
- 停止继续平行扩张

### V2

- 把高频入口统一到少数 command
- 把所有项目技能接入层切到链接模式
- 补一个全局 `MASTER_ROUTING.md`

### V3

- 给“龙虾人格”正式归位
- 裁掉低使用率平行架构
- 建立系统级变更准入规则

---

## 10. 当前执行建议

从现在开始，默认采用以下判断：

1. 先问：这是人格问题、路由问题、workflow 问题、skill 问题，还是知识问题？
2. 人格问题 → 改 `OpenClaw agent`
3. 路由问题 → 改 `Hermes / routing skills`
4. 工程工作流问题 → 改 `gstack`
5. 通用执行能力问题 → 改 `shared-ai-skills`
6. 项目特化规则问题 → 改项目内 `.claude/skills`
7. 长期知识问题 → 改 `knowledge-base / knowledge-wikis`

最终原则：

> 不再新增平行体系。所有新增资产必须先判断属于哪一层，再落到该层唯一 source of truth。
