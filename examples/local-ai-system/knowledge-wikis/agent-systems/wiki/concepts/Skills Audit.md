# Skills Audit

## Summary

Skills audit 是本地 Agent 体系的治理动作，用于定期检查：

- 重复能力
- 角色与 skill 的边界漂移
- 已失效或低活跃度的技能
- 应沉淀但未沉淀的流程
- `knowledge-base` 与 `knowledge-wikis` 的边界是否混乱

它的目标不是“清理得越少越好”，而是让整个体系持续保持可解释、可维护、可扩展。

## Why It Exists

随着本地系统同时包含：

- 角色入口
- 全局 skills
- 项目私有 skills
- 长期知识库
- 结构化 wiki

能力数量会上升得很快。  
如果没有周期治理，常见问题会越来越严重：

- 新 skill 创建后没人登记
- 项目 skill 与全局 skill 做同一件事
- 原本是路由层的东西逐渐膨胀成重技能
- 长期知识散在会话和项目文档里
- wiki 与 knowledge-base 边界变得模糊

## Audit Dimensions

### 1. Duplication

关注：

- 是否有两个 skill 覆盖同一输入输出
- 项目 skill 是否已经完全取代某个全局 skill
- 某个 command 是否只是在重复 skill 的工作

### 2. Boundary Clarity

关注：

- 角色层是否越权
- routing layer 是否承担了执行责任
- 执行 skill 是否错误接管知识沉淀
- 结构化知识是否放错地方

### 3. Liveness

关注：

- 哪些 skill 长期不用
- 哪些说明已过时
- 哪些触发词已经不能反映真实职责

### 4. Missing Extraction

关注：

- 是否有重复流程仍停留在聊天习惯层
- 是否有经验应进入 registry、knowledge-base 或 wiki
- 是否有项目经验已经值得抽成全局能力

## Cadence

推荐双节奏：

- **每周轻审计**：快速检查新增、重复、说明缺失
- **每月深审计**：系统检查边界、迁移、归档、提炼

## Outputs

一次有效的 skills audit 至少应产出以下之一：

- 更新 `SKILLS_REGISTRY.md`
- 新增 / 合并 / 归档 skill
- 新增一个 wiki 条目
- 补一份说明或边界文档

## Current Local Implementation

当前本地系统已增加：

- `skills-audit` skill
- skills audit 模板
- registry
- `agent-systems` wiki 页面

这意味着本地能力体系已经从“静态堆积”变成“可周期治理”。
