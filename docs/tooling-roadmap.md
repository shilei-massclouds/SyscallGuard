# 工具接入

当前来源 adapter 为 `ltp-extractor`，调用来源仓库中的 `tools/syscall_spec_extract.py` API。
adapter 读取 descriptor 的 location、revision、tool 和可选稳定 syscall 顺序；它只读取 LTP，
所有产物写入 SyscallGuard run 和共享库。

Starry 静态检查使用共享 `targets/starry/static-checks/*.yaml` 中的参数化路径与 regex。动态
测试使用 `targets/starry/dynamic-tests/*.yaml` 中的补丁、构建、命令和 blocker pattern。
增加 adapter 或 checker 时保持相同实体和 hash 契约，不增加高层流程命令。
