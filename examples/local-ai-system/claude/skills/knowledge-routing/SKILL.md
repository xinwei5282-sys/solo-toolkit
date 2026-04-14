---
name: knowledge-routing
description: 轻量知识路由技能。用于决定信息应该留在会话、项目文档、knowledge-base，还是 knowledge-wikis，避免长期知识和短期信息混存。
user-invocable: true
---

# Knowledge Routing

核心目标：**把信息放到正确的层，而不是全塞进一个地方。**

## 四层落点

### 1. 会话层

适合：
- 临时上下文
- 最近对话线索
- 当前轮次判断

### 2. 项目层

适合：
- 当前项目需求
- 实现计划
- 开发进度
- 设计决策

### 3. 长期知识层

位置：
- `~/knowledge-base/`

适合：
- 原则
- 方法
- 踩坑
- 通用经验

### 4. 结构化研究层

位置：
- `~/knowledge-wikis/`

适合：
- 可持续扩展主题
- 需要交叉链接
- 会反复查询和编译

## 快速判断题

如果一条信息：

- 只对当前会话有用 → 不落长期
- 只对当前项目有用 → 进项目层
- 对多个项目有用 → 进 `knowledge-base`
- 会成长成一个主题网络 → 进 `knowledge-wikis`
