# Skills Registry

本文件是本地 `Claude + OpenClaw + 项目私有 skills` 体系的总索引。

目标不是替代各自的 `SKILL.md` / `SOUL.md` / `AGENTS.md`，而是回答四个问题：

1. 这项能力属于哪一层？
2. 它应该放在哪个目录？
3. 它负责什么，不负责什么？
4. 与哪些能力互补，和哪些能力容易重叠？

---

## 一、分层模型

本地能力体系按 5 层管理：

1. **角色层**
   - 入口：`~/.claude/commands/`
   - 资产：`~/.openclaw/agents/*/agent/`
   - 职责：人格、视角、方法论、角色边界

2. **路由层**
   - 入口：`~/.claude/skills/*-routing/`、`hermes-loop`
   - 职责：先判断走哪类能力，再决定加载哪个重 skill

3. **执行技能层**
   - 入口：`~/.claude/skills/`、`<project>/.claude/skills/`
   - 职责：完成具体工作流，如开发、评审、测试、埋点、设计

4. **记忆层**
   - 入口：Hindsight、`~/knowledge-base/`
   - 职责：保存短中长期可复用信息

5. **结构化研究层**
   - 入口：`~/.claude/skills/llm-wiki`、`~/knowledge-wikis/`
   - 职责：持续编译主题知识、交叉链接、长期查询

---

## 二、角色层

### `dev`
- 入口：`~/.claude/commands/dev.md`
- 主职责：编码实现、调试、重构、测试、联调
- 不负责：业务优先级、PRD 主导、视觉方向
- 依赖：`~/.openclaw/agents/dev/agent/*`

### `pm`
- 入口：`~/.claude/commands/pm.md`
- 主职责：需求分析、优先级、业务判断、PRD、竞品与策略
- 不负责：直接主导编码和视觉定稿
- 依赖：`~/.openclaw/agents/pm/agent/*`

### `ui`
- 入口：`~/.claude/commands/ui.md`
- 主职责：页面结构、交互体验、视觉系统、设计规范
- 不负责：业务优先级和代码实现细节
- 依赖：`~/.openclaw/agents/design/agent/*`

### `arch`
- 入口：`~/.claude/commands/arch.md`
- 主职责：架构设计、技术选型、非功能需求、风险评估
- 不负责：业务代码实现

### 其他角色入口
- `ba.md`
- `sm.md`
- `hindsight.md`
- `merge-skill.md`

---

## 三、路由层

这层不主打执行，而主打“先分类，再加载”。

### `hermes-loop`
- 位置：`~/.claude/skills/hermes-loop/SKILL.md`
- 类型：元 skill / Hermes 风格运行层
- 职责：
  - 角色路由
  - 记忆分层
  - 技能沉淀判断
  - 周期复盘规则

### `research-routing`
- 类型：轻量路由 skill
- 用途：识别研究、资料整理、知识沉淀类请求

### `productivity-routing`
- 类型：轻量路由 skill
- 用途：识别文档、表格、汇报、效率类请求

### `knowledge-routing`
- 类型：轻量路由 skill
- 用途：决定信息应落到会话、项目文档、knowledge-base 还是 knowledge-wikis

### `agent-architecture-routing`
- 类型：轻量路由 skill
- 用途：识别 agent 架构、roles、skills、tooling、memory 设计类请求

---

## 四、全局执行技能层

### `solo-toolkit`
- 位置：`~/.claude/skills/solo-toolkit`
- 类型：重技能集合
- 职责：产品设计、前端设计、UX 评审、实现规范
- 子技能：
  - `frontend-design`
  - `audit`
  - `critique`
  - `adapt`
  - `polish`
  - `normalize`
  - 等
- 不负责：结构化研究知识库、交易分析、长期记忆

### `llm-wiki`
- 位置：`~/.claude/skills/llm-wiki`
- 类型：重技能
- 职责：
  - 主题知识库脚手架
  - raw → wiki 编译
  - query / lint / audit
- 不负责：
  - 普通笔记
  - 每日随手记录
  - 项目开发流程

---

## 五、项目私有执行技能层

### `sphere-search-mobile/.claude/skills`
- 典型技能：
  - `data-analyst`
  - `track-helper`
  - `track-sync`
  - `design-system`
  - `frontend-design`
  - `testing`
  - `code-reviewer`
  - `dev-workflow`
- 特征：项目规则强、输入输出稳定、与项目上下文紧耦合

#### 详细清单

| Skill | 主职责 | 备注 |
|------|--------|------|
| `app-router` | 路由结构、生成机制、配置规范 | 路由问题优先使用 |
| `branch-test-cases` | 分支变更测试用例生成 | 偏前后端联调用例 |
| `code-reviewer` | 项目规范代码审查 | 项目约束优先于全局习惯 |
| `dark-mode-migration` | 主题变量迁移 | 偏设计 token 改造 |
| `data-analyst` | SLS 数据分析与行为洞察 | 偏真实埋点数据 |
| `demo-page-dev` | demo 原型页开发 | 偏演示环境 |
| `design-system` | 项目设计规范 | 与全局设计 skill 配合使用 |
| `dev-workflow` | 标准开发流程 | 新功能开发优先加载 |
| `frontend-design` | 项目内前端设计方向 | 比全局设计 skill 更贴项目 |
| `js-to-ts-migration` | JS→TS 迁移 | 类型覆盖提升 |
| `prototype-page-migration` | 原型迁移 | 原型到正式项目 |
| `quick-dev` | 小型开发 / 修复 / 调整 | 轻量开发入口 |
| `review-branch` | 分支级审查 | 偏功能和影响面 |
| `skill-creator` | skill 创建 | 项目局部扩展 |
| `tailwind-page-dev` | Tailwind 页面规范 | 偏样式实现 |
| `test-runner` | 自动执行测试用例 | 与 `branch-test-cases` 配合 |
| `testing` | 单元测试规范 | 偏 vitest |
| `track-helper` | 埋点扫描、补充、统计 | 埋点治理主入口 |
| `track-sync` | 埋点同步飞书 | 埋点交付层 |
| `vue-component-generator` | Vue 组件生成 | 项目内标准化组件 |
| `webapp-testing` | Playwright Web 测试 | 偏浏览器自动化 |
| `zombie-code-cleaner` | 清理无用代码 | 偏代码资产治理 |

### `sphere-scrm/.claude/skills`
- 典型技能：
  - `dev-workflow`
  - `quick-dev`
  - `code-reviewer`
  - `reactive-fetch-list`

#### 详细清单

| Skill | 主职责 | 备注 |
|------|--------|------|
| `code-reviewer` | 项目规范代码审查 | 偏合规性与问题发现 |
| `dev-workflow` | 标准开发流程 | 新功能、需求分析优先加载 |
| `quick-dev` | 轻量开发和修复 | 不需要完整流程时使用 |
| `reactive-fetch-list` | reactive + fetch 列表页规范 | 强项目特定模式 |

### `SCRM/.claude`
- 典型资产：
  - `role-registry.md`
  - `skills/role-router`
  - `tools/install-shared-skill.sh`
- 特征：
  - 只保留项目 AI 接入层
  - 不在项目仓库复制角色人格或全局 skills
  - 通过映射表、薄路由和共享安装脚本接入独立 AI 仓库

#### 详细清单

| Asset | 主职责 | 备注 |
|------|--------|------|
| `role-registry.md` | 维护项目内角色映射 | 唯一角色真源仍是 `~/.openclaw/agents/*/agent/` |
| `skills/role-router` | 按上下文决定是否接入角色视角 | 只做薄路由，不复制人格 |
| `tools/install-shared-skill.sh` | 把共享 skill 链接到 Claude / Codex 运行时目录 | 业务项目只保留引用入口 |

### 其他独立技能
- `~/.openclaw/skills/daily-stock-analysis`
  - 职责：股票技术面分析与操作建议
  - 不负责：长期 thesis 知识库编译

---

## 六、记忆层与知识层

### Hindsight
- 职责：会话级、近中期上下文记忆
- 适合：用户偏好、近期状态、最近对话线索

### `~/knowledge-base/`
- 职责：通用长期知识
- 适合：经验、原则、踩坑、方法、决策记录

### `~/knowledge-wikis/`
- 当前主题：
  - `agent-systems`
  - `trading-thesis`
- 职责：结构化、交叉链接、持续编译的主题知识库

---

## 七、路由规则

### 1. 先判定角色

- 实现、调试、重构 → `dev`
- 业务、需求、优先级 → `pm` / `ba`
- 视觉、交互、体验 → `ui`
- 架构、选型、边界 → `arch`

### 2. 再判定是否需要项目私有 skill

如果当前工作目录存在项目内 `.claude/skills/`，优先加载项目 skill，再叠加全局能力。

### 3. 再判定信息落点

- 当前会话临时信息 → 会话上下文
- 当前项目执行状态 → 项目文档 / `progress.json`
- 通用长期知识 → `~/knowledge-base/`
- 结构化研究主题 → `~/knowledge-wikis/`

### 4. 最后判断是否需要沉淀 skill

以下条件满足至少 3 条，进入候选：

- 重复出现至少 2 次
- 输入输出稳定
- 步骤顺序明确
- 可验证
- 与某一角色或项目强关联

---

## 八、冲突与边界

### 允许互补
- `daily-stock-analysis` + `trading-thesis`
  - 前者负责即时分析
  - 后者负责长期 thesis

- `solo-toolkit` + `ui`
  - 前者提供方法库
  - 后者提供角色视角

- `llm-wiki` + `knowledge-base`
  - 前者负责结构化 wiki
  - 后者负责通用长期知识

### 需要警惕重叠
- 全局 `code-reviewer` vs 项目 `code-reviewer`
- 全局设计技能 vs 项目 `design-system`
- 普通知识记录 vs `llm-wiki` 结构化知识编译

处理原则：
- 项目约束优先于全局默认
- 结构化研究优先进入 `knowledge-wikis`
- 短期/碎片信息不要强行塞进 wiki

---

## 九、维护规则

每次新增或修改 skill、角色入口、知识库主题后，更新本文件：

- 新增了什么
- 放在哪层
- 主职责是什么
- 和现有能力是否重叠

建议每周做一次 registry review：

1. 是否有失效 skill
2. 是否有重复 skill
3. 是否有应提炼但尚未提炼的 SOP
4. 是否有知识该进入 `knowledge-wikis` 但仍散落在聊天记录中

---

## 十、触发词与典型场景

### 角色入口

| 入口 | 典型触发词 | 典型场景 |
|------|-----------|---------|
| `dev` | 开发、修复、重构、联调、实现、debug | 代码实现、故障排查、工程改造 |
| `pm` | 需求、PRD、优先级、方案、竞品、策略 | 做产品方案、需求澄清、业务判断 |
| `ui` | 设计、页面、交互、视觉、体验、规范 | 页面设计、设计评审、交互优化 |
| `arch` | 架构、选型、边界、系统设计、风险 | 技术架构评审、系统拆分、ADR |
| `ba` | 用户研究、业务分析、流程梳理、市场调研 | 业务洞察、流程分析、用户问题拆解 |
| `sm` | 任务拆解、排期、阻塞、Sprint、协作流程 | 迭代管理、流程推进、团队协作 |

### 路由层

| Skill | 典型触发词 | 典型场景 |
|------|-----------|---------|
| `hermes-loop` | 架构调整、skills 体系、沉淀经验、Hermes | 调整本地 agent 体系、切边界 |
| `research-routing` | 研究、查资料、竞品、论文、行业、交易研究 | 先判断研究请求该走哪层 |
| `productivity-routing` | 文档、汇报、整理、SOP、总结 | 先判断产物该落项目还是长期知识 |
| `knowledge-routing` | 记忆、知识库、沉淀、wiki、经验记录 | 先判断信息落点 |
| `agent-architecture-routing` | agent、roles、skills、memory、tooling | 先判断该改角色、skill 还是知识层 |

### 全局执行技能

| Skill | 典型触发词 | 典型场景 |
|------|-----------|---------|
| `solo-toolkit` | 前端设计、UX、界面评审、页面实现 | 设计与前端交付类任务 |
| `llm-wiki` | scaffold、ingest、compile、query、lint、audit | 结构化主题知识库维护 |
| `skills-audit` | 审计 skill、重复能力、边界治理 | 周期性清点本地能力体系 |

### 知识层

| 层 | 典型触发词 | 典型场景 |
|----|-----------|---------|
| 会话层 | 先记住、等会再用、刚才说到 | 临时上下文 |
| 项目层 | 当前项目、这次迭代、这份 PRD | 项目执行信息 |
| `knowledge-base` | 经验、原则、踩坑、方法 | 通用长期知识 |
| `knowledge-wikis` | 主题研究、概念体系、长期沉淀 | 结构化长期知识 |
