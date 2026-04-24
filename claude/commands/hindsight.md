# Hindsight 记忆管理 — 长期记忆系统 🧠

> 这是记忆系统运维入口，不是角色命令。默认由 `main` 或系统维护流程决定是否调用。

你现在是 Hindsight 记忆管理助手。Hindsight 是一个仿生长期记忆系统，通过 Claude Code 插件自动运行。

## 可用操作

根据用户请求执行以下操作：

### 查看状态
```bash
# 检查 daemon 运行状态
uvx hindsight-embed@latest daemon --profile claude-code status 2>&1 || echo "Daemon 未运行"

# 检查健康
curl -s http://localhost:9077/health 2>/dev/null || echo "API 不可达"
```

### 查看日志
```bash
tail -50 ~/.hindsight/profiles/claude-code.log 2>/dev/null || echo "暂无日志"
```

### 查看配置
```bash
cat ~/.hindsight/claude-code.json
```

### 调试模式
在 `~/.hindsight/claude-code.json` 中设置 `"debug": true` 启用详细日志。

### 重置记忆状态
如需重置插件状态（不删除记忆），查找并清理 `$CLAUDE_PLUGIN_DATA/state/` 目录。

## 注意事项
- Hindsight 插件通过 hooks 自动运行：SessionStart（健康检查）、UserPromptSubmit（自动召回）、Stop（自动保存）、SessionEnd（清理）
- 记忆按 agent + project 维度隔离
- LLM provider 配置为 claude-code（使用 Claude Code 自身模型）
- 首次使用需要重启 Claude Code 会话才能激活

执行以下任务：

$ARGUMENTS
