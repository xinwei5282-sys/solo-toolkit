# Ship — PR 创建与合并工作流

## Step 1: 飞行前检查
- 确认不在 base branch 上
- 检查工作区是否干净（有未提交的改动则提示）
- 检测 base branch（main/master）

## Step 2: 自动更新
- 从 commit 历史生成 CHANGELOG 条目
- 如有 VERSION 文件，询问是否 bump

## Step 3: 创建 PR
```bash
gh pr create --title "{title}" --body "$(cat <<'EOF'
## Summary
{从 commit 历史提取的变更摘要}

## Changes
{按类型分组的变更列表}

## Test plan
{测试说明}
EOF
)"
```

## Step 4: TODOS 清理
- 标记被此分支完成的 TODO
- 附注版本号 + 日期

## Step 5: 合并
- `git fetch origin <base>`
- 检查 CI 状态
- 询问合并方式：squash / rebase / merge commit
- 合并到 base
- 询问是否删除 feature branch

## Step 6: 合并后
- 生成一行摘要（可发 Slack/飞书）
- 输出 PR URL 和 merge commit SHA
