# LTP 和 Starry 历史来源索引

本目录保存迁移 run `spec-migrated-batch-001` 引用的历史来源索引。它不保存外部
Starry/LTP 源码树，也不参与新运行的增量选择。

当前 `source-index.yaml` 记录：

- 外部 `tgoskits` checkout 的路径、branch 和 commit。
- 迁移实体引用的关键 Starry 文件路径和 hash。
- 缺失或仅作为参考的外部规格材料。

新规格来源由 `source=<source-descriptor>` 定义并记录在 spec run。需要冻结历史证据时，
只保存无法从不可变 commit 恢复的最小子集，并明确复制原因。
