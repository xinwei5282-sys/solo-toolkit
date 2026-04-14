# Retro — 周度工程复盘

## 参数
- `/retro` — 默认 7 天
- `/retro 24h` — 过去 24 小时
- `/retro 14d` — 过去 14 天

## 数据收集（并行）
```bash
git log --oneline --since="{start}" --until="{end}" --shortstat --format="%H|%an|%aI|%s"
```

## 核心指标

| 指标 | 计算方式 |
|------|----------|
| 提交数 | git log count |
| 贡献者 | unique authors |
| 插入/删除 | shortstat sum |
| 测试占比 | test files LOC / total LOC |
| 工作会话 | 45 分钟间隔切分 |
| 每小时 LOC | insertions / active hours |

## 分析维度

1. **提交时间分布** — 按小时柱状图，识别高峰时段
2. **工作会话** — deep(>2h) / medium(1-2h) / micro(<1h)
3. **提交类型** — feat/fix/refactor/test/chore 占比，fix > 50% 告警
4. **热点文件** — 变更最频繁的 Top 10 文件
5. **PR 大小** — small/medium/large/XL 分布
6. **专注度** — 提交集中在哪个目录
7. **连续天数** — 团队 + 个人 streak

## 个人深度分析
- 提交数、LOC、专注领域
- 提交类型分布
- 会话模式 + 高峰时段
- 测试纪律
- 本周最大 ship

## 输出结构
```
## 一句话总结（可发推的长度）
## 指标总表
## 时间 & 会话模式
## 交付速度
## 代码质量信号
## 测试健康度
## 你的这周
## Top 3 本周成就
## 3 个改进方向
## 3 个下周习惯
```

## 历史对比
- 保存 JSON 快照到 `.context/retros/`
- 下次运行时加载对比，显示指标变化趋势
