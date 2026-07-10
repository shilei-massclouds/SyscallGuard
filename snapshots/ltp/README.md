# LTP 和 Starry 来源索引

本目录保存 SyscallGuard 批次可用的共享来源索引。它不默认保存外部 Starry/LTP
源码树。

当前 `source-index.yaml` 记录：

- 外部 `tgoskits` checkout 的路径、branch 和 commit。
- 当前 syscall 批次需要的关键 Starry 文件路径和 hash。
- 缺失或仅作为参考的外部规格材料。

后续批次不默认复制并提交外部 Starry/LTP 源码树。应优先在 `source-index.yaml`
中记录外部仓库路径或 URL、branch/tag、commit、相关文件路径和 hash。只有在来源
不可稳定恢复、review 必须离线自包含，或需要冻结很小的证据片段时，才复制最小文件
子集到本目录，并写明复制原因。
