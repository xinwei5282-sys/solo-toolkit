---
name: productivity-routing
description: 轻量效率路由技能。用于识别文档、表格、汇报、总结、流程整理类请求该走项目文档、知识库、还是某个具体执行 skill。
user-invocable: true
---

# Productivity Routing

这个 skill 负责把“文档/汇报/整理/沉淀”类请求先分流。

## 适用请求

- 写文档
- 做汇报
- 整理信息
- 生成表格
- 形成 SOP
- 复盘总结

## 路由规则

### A. 当前项目执行文档

去向：
- 项目目录
- `dev-workflow`
- `pm`

### B. 通用经验总结

去向：
- `~/knowledge-base/`

### C. 结构化主题资料

去向：
- `llm-wiki`
- `~/knowledge-wikis/`

### D. 可重复流程

去向：
- 新建或更新 skill
- 更新 `SKILLS_REGISTRY.md`

## 关键判断

如果输出物主要是为了“以后重复用”，优先考虑沉淀 skill 或长期知识；  
如果主要是为了“当前项目推进”，优先写项目文档。
