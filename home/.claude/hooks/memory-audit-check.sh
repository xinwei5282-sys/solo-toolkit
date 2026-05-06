#!/bin/bash
# Memory audit reminder hook
# 检查记忆体检是否过期（>=7 天），过期时通过 stderr 提示 Claude

MEMORY_DIR="$HOME/.claude/projects/-Users-weiran/memory"
LAST_PROMPT_FILE="$HOME/.claude/hooks/.last-audit-prompt"
INTERVAL_DAYS=7
PROMPT_COOLDOWN_HOURS=24

# 找最新的 audit 报告
LATEST=$(ls -t "$MEMORY_DIR"/audit-*.md 2>/dev/null | head -1)

# 决定是否需要提示
NEED_PROMPT=0
DAYS=0

if [ -z "$LATEST" ]; then
  NEED_PROMPT=1
  REASON="尚未做过任何记忆体检"
else
  LATEST_DATE=$(basename "$LATEST" | sed 's/audit-\(.*\)\.md/\1/')
  LATEST_TS=$(date -j -f "%Y-%m-%d" "$LATEST_DATE" +%s 2>/dev/null)
  if [ -n "$LATEST_TS" ]; then
    NOW_TS=$(date +%s)
    DAYS=$(( (NOW_TS - LATEST_TS) / 86400 ))
    if [ "$DAYS" -ge "$INTERVAL_DAYS" ]; then
      NEED_PROMPT=1
      REASON="距上次体检 ${DAYS} 天"
    fi
  fi
fi

# 不需要提示则静默退出
[ "$NEED_PROMPT" -eq 0 ] && exit 0

# 防止刷屏：24 小时内最多提示一次
if [ -f "$LAST_PROMPT_FILE" ]; then
  LAST_PROMPT_TS=$(cat "$LAST_PROMPT_FILE" 2>/dev/null)
  if [ -n "$LAST_PROMPT_TS" ]; then
    HOURS_SINCE=$(( ($(date +%s) - LAST_PROMPT_TS) / 3600 ))
    [ "$HOURS_SINCE" -lt "$PROMPT_COOLDOWN_HOURS" ] && exit 0
  fi
fi

# 记录提示时间
date +%s > "$LAST_PROMPT_FILE"

# 输出提醒到 stderr → Claude 会看到这条作为 system 上下文
cat >&2 <<EOF
[memory-audit reminder] ${REASON}。建议在合适的时机运行 \`/memory-audit\` 检查记忆库是否仍与系统现状一致。这条提醒每 ${PROMPT_COOLDOWN_HOURS} 小时最多触发一次，不强制立即处理。
EOF

exit 0
