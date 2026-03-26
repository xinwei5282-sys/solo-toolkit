# Document Release — 发版后文档同步

**时机：/ship 之后、PR 合并之前。**

## 流程

### 1. Diff 分析
- `git diff origin/<base> --stat`
- 发现所有 .md 文件
- 分类变更：新功能、行为变更、功能移除、基础设施

### 2. 逐文件审计
对每个文档交叉引用 diff：

| 文档 | 检查点 |
|------|--------|
| README | 功能列表、安装步骤、示例、故障排查 |
| ARCHITECTURE | 图表、组件描述、设计决策 |
| CONTRIBUTING | 环境搭建、测试说明、工作流 |
| CLAUDE.md | 项目结构、命令、构建/测试指令 |

分类：**Auto-update**（事实性更正）| **Ask**（叙述性变更、删除、大改写）

### 3. 应用更新
- Auto-update 直接改
- Ask 的逐个问用户

### 4. CHANGELOG 润色
- 先读完整 CHANGELOG
- 只润色措辞（永不删除/替换条目）
- 以用户能做什么开头，不以技术变更开头

### 5. 跨文档一致性
- README 功能列表 = CLAUDE.md？
- ARCHITECTURE = CONTRIBUTING 项目结构？
- CHANGELOG 版本 = VERSION 文件？

### 6. VERSION bump
- 未修改 → 问用户：A) PATCH B) MINOR C) 跳过
- 已修改 → 检查 CHANGELOG 是否覆盖所有重要变更

### 7. 提交
- 按文件名 stage（不用 `git add -A`）
- 单次提交：`docs: update project documentation for vX.Y.Z`
- 推送到当前分支

### 输出
```
文档健康摘要
├── README:        Updated (补充了新功能说明)
├── ARCHITECTURE:  Current
├── CHANGELOG:     Voice polished
├── CLAUDE.md:     Updated (更新了命令列表)
├── VERSION:       Bumped to X.Y.Z
└── TODOS:         3 items completed, 1 added
```
