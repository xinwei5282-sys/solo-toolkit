# Review — 合并前代码审查

**目标：发现测试抓不到的结构性问题。**

## Step 1: 准备
- 检测 base branch（`gh pr view` 或 `main`/`master`）
- `git diff origin/<base>` 获取完整 diff

## Step 2: 范围漂移检测
- 读 PR 描述、commit messages
- 对比声明意图 vs 实际 diff
- 标记：范围蔓延（无关文件）、遗漏需求

## Step 3: 两轮审查

### Pass 1 — CRITICAL（必须修复）
| 类别 | 检查点 |
|------|--------|
| SQL & 数据安全 | 原始 SQL 拼接、缺少事务、级联删除 |
| 竞态条件 | 共享状态无锁、check-then-act |
| LLM 输出信任 | 未校验的 AI 输出直接用于业务逻辑 |
| 枚举完整性 | switch/case 缺少分支（需读 diff 外的代码） |

### Pass 2 — INFORMATIONAL（建议修复）
| 类别 | 检查点 |
|------|--------|
| 条件副作用 | if 内有 mutation 但 else 没有 |
| 魔法数字 | 未命名的常量 |
| 死代码 | 不可达分支 |
| 测试缺口 | 新逻辑无对应测试 |
| 前端 | 缺少 loading/error/empty 状态 |

## Step 4: 修复
- **AUTO-FIX**：明确的事实性问题，直接修
- **ASK**：需要判断的问题，批量问用户
- 应用用户批准的修复

## Step 5: 文档检查
- 变更的功能是否有文档描述？文档是否需要更新？
- TODOS 交叉引用

## 输出
```
Pre-Landing Review: N issues (X critical, Y informational)
```
