# 工具接入

当前来源 adapter 为仓库内置 `ltp`，外部 LTP checkout 只读。识别行为由
`sources/adapters/ltp/recognition-rules.yaml` 唯一配置。Adapter 只暴露 `discover`、`prescan`
和 `extract`；syscall 始终按规范化名字典序处理。

新增 adapter 必须产生 source/recognition fingerprint，并遵守 report-only 增量状态、证据全量
解析门槛和失败无落盘契约。不要增加 raw evidence、spec、index 或独立 state 持久化。

Starry 静态检查与动态测试继续使用 `targets/starry/` 下的共享分片和 index。新增 checker 必须
使用 mapping manifest 的 `rule_syscalls`，不能重新引入 ingest report 或 syscall spec 依赖。
