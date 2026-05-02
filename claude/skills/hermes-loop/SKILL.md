---
name: hermes-loop
description: Hermes Agent 风格的本地编排元技能。用于先做任务路由、再决定角色分工、知识落点和技能沉淀；适合设计本地 AI 工作流、角色体系、复盘机制和可复用自动化流程。
user-invocable: true
argument-hint: "[任务或改造目标]"
---

# Hermes Loop

这个 skill 不直接替代现有角色，而是给本地系统加一层 Hermes Agent 风格的运行框架：

1. **Role Routing**：任务先路由到合适角色
2. **Memory Tiering**：信息按复用价值落到不同存储层
3. **Skill Extraction**：把重复工作提炼成 skills
4. **Review Loop**：定期复盘并修正规则

核心目标：**先判断任务该由谁主导、信息该落哪里、流程是否值得沉淀，再进入具体执行。**

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

如果无法明确主角色，先按“谁对最终结果负责”来定主角色，其他角色只作为辅助视角。

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

### C. 长期知识层 + 结构化研究层（统一进 Obsidian）

放可跨项目复用的经验、原则、踩坑、方法，以及持续维护的主题知识。

建议位置：
- **Obsidian**（`~/knowledge-hub/wiki/`）— 用 `obsidian-vault` skill 读写，支持 wikilinks 和图谱
- 包含：技术经验（`开发问题总结/`）、团队经验（`团队经验教训.md`）、老板偏好（`老板偏好.md`）、项目文档（`项目/`）、日报（`日报/`）
- `~/knowledge-base/` 和 `~/knowledge-wikis/` 均为 symlink → `~/knowledge-hub/wiki/`，旧路径仍可用

### Obsidian 双向读写规则

**AI → Obsidian（写入）：**
- 整理好的主题知识、概念解释、研究结论 → 用 `obsidian-vault` skill 创建新笔记
- 笔记用 Title Case 命名，用 `[[wikilinks]]` 关联相关笔记
- Index 笔记（如 `AI 架构 Index.md`）汇总同主题的所有条目

**Obsidian → AI（读取）：**
- 任务开始前，如涉及某主题，用 `obsidian-vault` skill 搜索相关笔记作为上下文
- 有相关 Index 笔记时，优先读 Index 再按需展开

### 判断顺序

不要直接选存储位置，按顺序判断：

1. 这条信息只服务当前对话吗？→ 会话层
2. 这条信息只服务当前项目吗？→ 项目层
3. 其他（跨项目复用 / 长期维护 / 结构化研究）→ Obsidian（`~/knowledge-hub/wiki/`）

## Step 3: 判断是否应该提炼成 skill

如果一项工作满足以下 3 条及以上，就应该考虑提炼：

- 重复执行过至少两次
- 输入输出相对稳定
- 步骤顺序清晰
- 可以被检查和验收
- 与某一类项目或角色强相关

### 落位原则

- 全局通用：`~/.agents/skills/`（Claude 和 Codex 共享单一真源）
- 项目专用：`<project>/.claude/skills/`（仅存项目特有的，其余用 symlink 指向全局）
- 角色定义：`~/.agents/skills/role-*/SKILL.md`
- 人格/方法论：`~/.agents/skills/role-*/persona/`（仅 main 和 lobster 有完整 persona，其他角色人格内嵌在 SKILL.md）
- 知识沉淀：`~/knowledge-hub/wiki/`（Obsidian）

如果只是做过一次、还没有稳定输入输出，不要急着提炼 skill，先记为 SOP 草稿。

## Step 4: 做技能边界切分

一个健康的本地 skills 体系应当把以下四类能力分开：

1. **人格与角色**
   - `commands/*.md`
   - `SOUL.md`
   - `AGENTS.md`
   - `IDENTITY.md`

2. **执行技能**
   - 开发、测试、埋点、设计、评审类 skills

3. **长期记忆 + 研究型知识库**（统一）
   - Obsidian（`~/knowledge-hub/wiki/`）
   - 用 `obsidian-vault` skill 读写

如果两个 skill 同时在做“同一输入、同一输出、同一流程”的事情，就说明边界有问题，应合并或重新命名。

## Step 4.5: 判断影响范围

在真正动手前，补做一次范围判断：

1. 这是全局规则，还是项目内规则？
2. 是修改现有 skill，还是新建 skill？
3. 是否需要同步更新注册表、命令入口、知识落点规则？

## Step 5: 任务完成后的 Hermes 闭环

每次完成一个中大型任务后，追加检查：

1. 是否产生了新的长期知识？
2. 是否形成了新的稳定 SOP？
3. 是否暴露了现有角色或 skill 的边界缺陷？

### 知识写回规则

| 内容类型 | 写入位置 |
|---------|---------|
| 技术踩坑、解决方案 | `~/knowledge-hub/wiki/开发问题总结/<分类>/` |
| 团队经验教训 | `~/knowledge-hub/wiki/团队经验教训.md`（追加） |
| 老板新偏好 | `~/knowledge-hub/wiki/老板偏好.md`（追加） |
| 新 SOP / 可复用流程 | `~/.agents/skills/<新skill>/SKILL.md` |
| 角色边界缺陷 | `~/.agents/skills/role-<role>/SKILL.md`（更新） |

笔记格式：标题用中文，内容简洁，用 `[[wikilinks]]` 关联相关笔记。

## 输出格式

使用本 skill 时，至少输出：

```md
## Hermes Loop Decision
- 主角色：
- 辅助角色：
- 记忆落点：
- 是否需要 skill 沉淀：
- 影响范围：
- 下一步动作：
```

## 检查点

以下情况先确认用户：

- 你不确定该做成全局能力还是项目能力
- 你不确定是“新建 skill”还是“更新现有 skill”
- 你不确定知识该落项目层还是长期层
- 改动会影响多个角色、多个项目或多个注册表

## Fallback

如果判断不清，默认走更轻路径：

- 先指定主角色，不立刻扩多角色
- 先项目内沉淀，不立刻做全局 skill
- 先写 SOP 草稿，不立刻抽象成正式能力
- 先放项目层或会话层，不立刻写入长期知识库

原则：**先形成可运行闭环，再决定是否全局化。**

## 对你当前本地体系的推荐落位

- `~/.claude/commands/`：角色入口
- `~/.agents/skills/role-*/`：角色定义 + 可选 persona 子目录
- `~/.claude/skills/solo-toolkit`：通用设计与前端能力
- `~/.claude/skills/llm-wiki`：结构化研究型知识库能力
- `~/knowledge-hub/wiki/`：Obsidian vault（所有长期知识统一入口）
- 项目内 `.claude/skills/`：项目专有能力

## 使用方式

当用户说下面这些话时，应优先加载本 skill：

- “帮我整理本地 skills 架构”
- “这个能力应该做成 skill 还是命令”
- “怎么把经验沉淀下来”
- “这些 skills 有点重叠，帮我切边界”
- “基于 Hermes Agent 思路改一下我本地体系”
- “先帮我判断这个项目任务该走哪个角色和 skill”
- “这个需求要不要拆成一个可复用 skill”
- “当前会话应该优先加载哪些 skills”
- “帮我把这个流程整理成可复用 SOP / skill”
- “这个项目的执行规则和触发条件怎么定”

### 强触发场景

只要用户正在做以下类型的事情，就应优先评估并考虑加载本 skill，而不是先直接进入通用回答：

- 设计本地 agent 架构、角色路由、skills 边界
- 判断一个任务该由哪个角色主导、是否需要叠加 project skill
- 把重复出现的流程整理成可复用 workflow / SOP / skill
- 统一项目级、全局级、知识库级的落位规则
- 调整 Hermes、路由、记忆、技能沉淀相关规范

如果任务同时涉及“怎么做”和“该由谁做”，优先先用本 skill 做路由判断，再进入具体执行 skill。
