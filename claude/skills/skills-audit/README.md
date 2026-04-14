# Skills Audit Workflow

## 轻审计（每周）

1. 阅读 `~/.claude/SKILLS_REGISTRY.md`
2. 扫描 `~/.claude/skills/` 与常用项目 `.claude/skills/`
3. 找出：
   - 最近新增但未登记的 skill
   - 明显重复能力
   - 应补文档但未补的 skill
4. 输出一份基于 `TEMPLATE.md` 的简短报告
5. 至少执行一个修复动作

## 深审计（每月）

1. 复查角色层、路由层、执行技能层、记忆层、研究层
2. 检查 project skills 是否该抽象为全局能力
3. 检查 `knowledge-base` 与 `knowledge-wikis` 的边界是否漂移
4. 检查长期不用的技能是否应归档
5. 更新 registry 与 wiki

## 推荐落地产物

- `~/.claude/SKILLS_REGISTRY.md`
- `~/knowledge-wikis/agent-systems/`
- 审计报告文件（建议放项目目录或 `knowledge-base`）
