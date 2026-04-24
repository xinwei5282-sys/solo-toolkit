# AI System Config

本仓库用于版本化管理本地 AI 系统的关键配置、角色入口、skills 架构与结构化知识库。

## Included

- `MASTER_ARCHITECTURE.md`
  - 本地 AI 系统统一架构蓝图与 source of truth 说明
- `claude/commands/`
  - 本地角色入口
- `claude/skills/`
  - 全局 skills、routing layer、审计能力、wiki 相关技能
- `claude/SKILLS_REGISTRY.md`
  - 本地能力体系总索引
- `claude/skills-audit-reports/`
  - skills 审计报告
- `knowledge-wikis/`
  - 结构化主题知识库

## Purpose

这个仓库不是运行时目录，而是一个可追踪、可回滚、可审计的配置与知识快照。

它的目标是：

1. 记录本地 AI 架构的演化
2. 让角色、skills、routing、wiki 结构可版本化
3. 为后续迁移、审计和复盘提供稳定基线

## Notes

- 运行时目录仍位于用户主目录下的原始位置
- 本仓库主要保存配置与知识资产，不保存临时会话状态
- 如后续新增全局 skill、角色入口或 wiki 主题，应同步更新本仓库
