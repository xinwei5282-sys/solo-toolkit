# MASTER_ROUTING.md

> 统一路由规则。所有角色、技能、知识落点的路由决策以本文件为 source of truth。
> 其他文件（CLAUDE.md、SKILLS_REGISTRY.md）的路由描述均以本文件为准，不单独维护。

---

## 一、路由总流程

```
用户输入
  │
  ▼
① 角色判断（查"二、角色路由表"）
  │
  ├─ 方向不清 / 范围失控 / "全都要" → 先拉 /lobster 挑战
  │
  ▼
② 是否需要技能叠加？（查"三、技能路由"）
  │
  ▼
③ 多步骤开发任务？→ 启动任务编排（progress.json 流程）
  │
  ▼
④ 信息落点判断（查"四、知识路由"）
```

---

## 二、角色路由表

| 任务类型 | 主角色 | 命令 | OpenClaw Agent |
|---------|--------|------|---------------|
| 代码实现、调试、重构、联调 | 码匠 | `/dev` | `agents/dev` |
| 需求分析、PRD、优先级、竞品 | 明策 | `/pm` | `agents/pm` |
| 页面设计、交互、视觉、体验 | 绘心 | `/ui` | `agents/design`（命名历史遗留） |
| 架构设计、技术选型、风险评估 | 架构师 | `/arch` | `agents/arch` |
| 战略挑战、取舍、拆假问题 | 龙虾 | `/lobster` | `agents/lobster` |
| 量化交易、策略执行、仓位管理 | 操盘 | `/trader` | `agents/trader` |
| 系统运维、告警、稳定性 | 守卫 | `/ops` | `agents/ops` |
| 内容规划、文章撰写 | 墨言 | `/content` | `agents/content` |
| 用户增长、渠道、漏斗 | 拓客 | `/growth` | `agents/growth` |
| 用户支持、反馈收集 | 暖客 | `/support` | `agents/support` |
| 账务、财务分析 | 算盘 | `/finance` | `agents/finance` |
| 合同、合规、隐私 | 律己 | `/legal` | `agents/legal` |
| 协调分派、进度跟进 | 晓秘 | `/main` | `workspace/` |
| 无明确角色 | 晓秘（默认） | `/main` | `workspace/` |

### B 级入口（非默认，由 main 按需调用）

`/content`、`/finance`、`/growth`、`/legal`、`/ops`、`/support`

### 兼容性入口（指向 /pm）

`/ba`（业务分析子模式）、`/sm`（敏捷推进子模式）

### 龙虾介入时机

**介入**：方向可能错了 / 范围失控 / "都重要" / 方案像在堆复杂度

**不介入**：问题已明确是实现/设计/架构/测试/部署

---

## 三、技能路由

角色确定后，判断是否需要叠加专项技能：

| 场景 | 技能 |
|------|------|
| 设计/前端交付 | `solo-toolkit` / `frontend-design` |
| 研究任务落点不清 | `research-routing` 先判断 |
| 知识应落哪层 | `knowledge-routing` 先判断 |
| Agent 体系调整 | `agent-architecture-routing` |
| 多角色任务协调 | `hermes-loop` |
| 代码审查 | `review` (gstack) |
| 系统安全审计 | `cso` (gstack) |
| 多 AI 二次意见 | `codex` (gstack) |
| Skill 质量优化 | `darwin-skill`（达尔文） |
| Skill 体系治理 | `skills-audit`（达尔文是单个skill优化，skills-audit是体系治理） |

### 项目私有技能优先级

当工作目录存在 `.claude/skills/`，优先加载项目 skill，再叠加全局技能。

---

## 四、知识路由

| 内容类型 | 落点 | 路径 |
|---------|------|------|
| 当前任务临时信息 | 会话上下文 | — |
| 当前项目执行状态 | 项目文档 | `progress.json`、项目 `.claude/` |
| 日常工作笔记、日报、项目文档 | Obsidian Vault | `~/knowledge-wikis/wiki/` |
| 可跨项目复用的经验/原则/踩坑 | 通用知识库 | `~/knowledge-base/` |
| 需持续编译的主题研究 | 结构化研究 | `~/ai-system-config/knowledge-wikis/` |

### 判断"通用知识 vs 结构化研究"

进入 `knowledge-wikis` 的条件（满足 2 条以上）：
- 需要多来源交叉引用
- 长期持续维护（不是一次性记录）
- 有明确主题边界（如 `agent-systems`、`trading-thesis`）
- 会被反复查询

否则进 `knowledge-base`。

---

## 五、多步骤任务编排触发条件

满足以下条件时，在角色上下文内启动 progress.json 编排流程：

- 任务需要 3 步以上才能完成
- 跨多个文件或模块的修改
- 预期耗时超过当前会话

单步骤任务（修 typo、解释代码、回答问题）不启用编排。

---

## 六、Source of Truth 表

| 层 | Source of Truth |
|---|---|
| 人格/角色 | `~/.openclaw/agents/*/agent/` |
| 命令入口 | `~/.claude/commands/` |
| 路由规则 | **本文件** `MASTER_ROUTING.md` |
| 工程工作流 | `gstack` |
| 全局技能 | `~/.shared-ai-skills/` |
| 项目技能 | `<project>/.claude/skills/` |
| 日常笔记 | `~/knowledge-wikis/wiki/`（Obsidian） |
| 通用知识 | `~/knowledge-base/` |
| 主题研究 | `~/ai-system-config/knowledge-wikis/` |
