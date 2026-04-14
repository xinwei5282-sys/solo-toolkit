---
name: agent-architecture-routing
description: 轻量 Agent 架构路由技能。用于识别一个请求是在调整角色、skills、工具、记忆、网关、定时任务还是知识层，并决定该改哪一层。
user-invocable: true
---

# Agent Architecture Routing

当请求和 Agent 系统本身有关时，不要直接修改文件，先判断目标层。

## 分层判断

### A. 角色层

关键词：
- 人格
- 角色
- SOUL
- command
- 身份

改动位置：
- `~/.claude/commands/`
- `~/.openclaw/agents/*/agent/`

### B. 路由 / 编排层

关键词：
- Hermes
- 路由
- 编排
- 技能边界
- 架构调整

改动位置：
- `hermes-loop`
- routing skills
- `SKILLS_REGISTRY.md`
- `~/.claude/CLAUDE.md`

### C. 执行技能层

关键词：
- skill
- workflow
- 触发词
- SOP

改动位置：
- `~/.claude/skills/`
- 项目内 `.claude/skills/`

### D. 工具层

关键词：
- MCP
- 浏览器
- 命令执行
- 插件

改动位置：
- 工具配置
- 插件配置
- gateway / tool adapters

### E. 记忆 / 知识层

关键词：
- memory
- hindsight
- knowledge
- wiki

改动位置：
- Hindsight
- `knowledge-base`
- `knowledge-wikis`

## 输出要求

处理这类请求时，先明确：

1. 当前问题属于哪一层
2. 应修改哪个目录
3. 是否会影响其他层
4. 需要更新哪些注册表或规范文件
