# SCRM Project AI Integration

这个目录展示 `SCRM` 项目如何只保留 AI 接入层，而不把整套本地 AI 运行时复制进业务仓库。

## 保留什么

- `.claude/role-registry.md`
  - 项目内角色映射表
- `.claude/skills/role-router/SKILL.md`
  - 按上下文决定是否接入角色视角的薄路由
- `tools/install-shared-skill.sh`
  - 把独立 AI 仓库中的共享 skill 链接到本地运行时目录

## 不保留什么

- 不在项目内复制 `~/.openclaw/agents/*/agent/`
- 不在项目内复制全局 `~/.claude/skills/*`
- 不在项目内复制 `.gstack/` 或完整 `.agents/skills/gstack/`

## 原则

1. 角色真源固定在 `~/.openclaw/agents/<role>/agent/`
2. 全局 skill 真源固定在独立 AI 仓库
3. 项目仓库只维护映射、薄路由和安装入口
4. 这样可以避免业务仓库与 AI 底层能力一起漂移
