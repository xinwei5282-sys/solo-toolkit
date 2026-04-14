# Safety Guardrails (careful + freeze + guard)

## /careful — 危险命令拦截

在执行以下命令前**必须警告用户并等待确认**：
- `rm -rf`（排除 node_modules/dist/__pycache__/build/.next/.cache）
- `DROP TABLE` / `DROP DATABASE` / `TRUNCATE`
- `git push --force` / `git reset --hard` / `git checkout .`
- `kubectl delete` / `docker rm -f` / `docker system prune`
- `chmod 777` / `chown -R`

用户可以逐条覆盖。会话级生效。

## /freeze — 限制编辑范围

1. 询问用户要锁定哪个目录
2. 解析为绝对路径
3. 之后所有 Edit/Write 操作只允许目标目录内的文件
4. Read/Bash/Glob/Grep 不受限制
5. 用 `/unfreeze` 解除

## /guard — 最大安全模式

同时启用 /careful + /freeze：
- 危险命令需确认
- 编辑范围受限
- 适用于生产环境或共享系统调试
