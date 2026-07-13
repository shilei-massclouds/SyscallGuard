# 步骤 08 - Fix Plan And Apply Outside Harness

批次：`001-syscall-batch-ioctl-renameat2`
状态：`pending_human_review`

## 目的

根据第 07 步 triage，产出第 09 步要执行的动态测试用例清单，并生成 Starry
`qemu-smp1/system` 动态测试补丁作为中间结果。本步不直接修改 tgoskits/Starry 仓库，
不运行动态测试，也不生成 Starry 修复 patch；修复候选仍由第 09 步根据第 06 步静态
检查/审计结果和第 09 步动态执行结果生成。

## 输入

- `manifest.yaml`
- `steps/07-gap-triage.md`
- `outputs/validation-cases.yaml` 的既有 7 类 runtime risk
- tgoskits 样板：`test-suit/starryos/qemu-smp1/system/syscall-test-ltp-pilot-min/`
- tgoskits 公共框架：`test-suit/starryos/qemu-smp1/system/common/test_framework.h`
- tgoskits 聚合入口：`test-suit/starryos/qemu-smp1/system/CMakeLists.txt`
- 外部 Starry source ref：`tgoskits-local`，branch `dev-ltp-spec-2`，commit
  `4f30e12d17e4da175233bb3a51889efe747a45f9`

## 执行内容

- 确认 `qemu-smp1/system/CMakeLists.txt` 会自动发现带 `CMakeLists.txt` 的子目录。
- 确认 system 子用例形态为 `system/<subcase>/CMakeLists.txt` 加 `system/<subcase>/src/main.c`。
- 确认单个 system 子用例可通过 `cargo xtask starry test qemu --arch riscv64 -c qemu-smp1/<subcase>` 选择。
- 生成 `outputs/starry-dynamic-tests.patch`，其中包含 7 个 Starry system C 子用例。
- 生成 `outputs/starry-dynamic-tests.yaml`，记录每个子用例的 test source、riscv64 命令和预期日志路径。
- 更新 `outputs/validation-cases.yaml`，把 7 个动态 case 从 missing command 改为 `generated_pending_step08_review`。
- 将本步 sign-off 重新置为 `pending_human_review`，等待确认新生成的 patch 和命令绑定。

## 外部修改结论

| Area | Decision | Evidence / reason |
| --- | --- | --- |
| tgoskits test patch | `generated_for_review` | `outputs/starry-dynamic-tests.patch` 只作为中间补丁保存，未应用到外部仓库。 |
| Dynamic command binding | `generated_for_review` | `outputs/starry-dynamic-tests.yaml` 和 `outputs/validation-cases.yaml` 为 7 个 case 绑定 riscv64 命令。 |
| Starry patch generation | `deferred_to_step09` | 修复候选需要结合第 06 步静态检查/审计结果和第 09 步动态测试结果生成。 |
| Spec/tool refresh | `planned_later` | `T07-SOURCE-SPEC-GAP` 和 `T07-IOCTL-REQUEST-SPLIT` 需要后续 spec/refinement 决策。 |
| Static checker integration | `planned_later` | `T07-STATIC-CHECKER-GAP` 需要后续把外部 checker 参数化后再接入。 |

## 第 07 步 triage 处置表

| Triage ID | Step 08 disposition | Apply now | Follow-up owner |
| --- | --- | --- | --- |
| `T07-IOCTL-REQUEST-SPLIT` | 作为 spec refinement 计划保留；本轮不拆分当前批次范围 | no | future spec refresh / later ioctl sub-batch |
| `T07-DYNAMIC-PERMISSION` | 生成 `syscallguard-b001-permission-matrix` 动态测试补丁和 riscv64 命令 | no | Step 09 validation |
| `T07-DYNAMIC-FS-SIDE-EFFECT` | 生成 `syscallguard-b001-fs-side-effect` 动态测试补丁和 riscv64 命令 | no | Step 09 validation |
| `T07-DYNAMIC-DIRENT` | 生成 `syscallguard-b001-dirent-enumeration` 动态测试补丁和 riscv64 命令 | no | Step 09 validation |
| `T07-FD-TYPE-MATRIX` | 生成 `syscallguard-b001-fd-type-matrix` 动态测试补丁和 riscv64 命令 | no | Step 09 validation |
| `T07-PATH-ERRNO-PRIORITY` | 生成 `syscallguard-b001-path-errno-priority` 动态测试补丁和 riscv64 命令 | no | Step 09 validation |
| `T07-USERPTR-EFAULT` | 生成 `syscallguard-b001-userptr-efault` 动态测试补丁和 riscv64 命令 | no | Step 09 validation |
| `T07-MODE-UID-GID` | 生成 `syscallguard-b001-mode-uid-gid` 动态测试补丁和 riscv64 命令 | no | Step 09 validation |
| `T07-SOURCE-SPEC-GAP` | 本轮不回滚重做 Step 02/03；作为 closeout 前需明确接受或刷新项目保留 | no | closeout review / future extractor run |
| `T07-STATIC-CHECKER-GAP` | 本轮不接入 checker；保留人工审计结论并禁止声称 automated checker coverage | no | future checker integration |

## Dynamic validation cases for Step 09

结构化用例文件：`outputs/validation-cases.yaml`。
补丁文件：`outputs/starry-dynamic-tests.patch`。
命令清单：`outputs/starry-dynamic-tests.yaml`。

| Case ID | Source triage | Starry subcase | Step 08 status | Step 09 command |
| --- | --- | --- | --- | --- |
| `V09-PERMISSION-MATRIX` | `T07-DYNAMIC-PERMISSION` | `syscallguard-b001-permission-matrix` | `generated_pending_review` | `cargo xtask starry test qemu --arch riscv64 -c qemu-smp1/syscallguard-b001-permission-matrix` |
| `V09-FS-SIDE-EFFECT` | `T07-DYNAMIC-FS-SIDE-EFFECT` | `syscallguard-b001-fs-side-effect` | `generated_pending_review` | `cargo xtask starry test qemu --arch riscv64 -c qemu-smp1/syscallguard-b001-fs-side-effect` |
| `V09-DIRENT-ENUMERATION` | `T07-DYNAMIC-DIRENT` | `syscallguard-b001-dirent-enumeration` | `generated_pending_review` | `cargo xtask starry test qemu --arch riscv64 -c qemu-smp1/syscallguard-b001-dirent-enumeration` |
| `V09-FD-TYPE-MATRIX` | `T07-FD-TYPE-MATRIX` | `syscallguard-b001-fd-type-matrix` | `generated_pending_review` | `cargo xtask starry test qemu --arch riscv64 -c qemu-smp1/syscallguard-b001-fd-type-matrix` |
| `V09-PATH-ERRNO-PRIORITY` | `T07-PATH-ERRNO-PRIORITY` | `syscallguard-b001-path-errno-priority` | `generated_pending_review` | `cargo xtask starry test qemu --arch riscv64 -c qemu-smp1/syscallguard-b001-path-errno-priority` |
| `V09-USERPTR-EFAULT` | `T07-USERPTR-EFAULT` | `syscallguard-b001-userptr-efault` | `generated_pending_review` | `cargo xtask starry test qemu --arch riscv64 -c qemu-smp1/syscallguard-b001-userptr-efault` |
| `V09-MODE-UID-GID` | `T07-MODE-UID-GID` | `syscallguard-b001-mode-uid-gid` | `generated_pending_review` | `cargo xtask starry test qemu --arch riscv64 -c qemu-smp1/syscallguard-b001-mode-uid-gid` |

每个子用例都包含 `CMakeLists.txt` 和 `src/main.c`，并通过 CMake include path 复用
`system/common/test_framework.h`，不复制自定义 CHECK 框架。

## Human review checklist

| No. | Question | Current answer |
| --- | --- | --- |
| 1 | 是否接受这 7 类 Starry 动态测试类别？ | pending human review |
| 2 | 是否接受每个类别覆盖的 syscall/行为范围？ | pending human review |
| 3 | 是否接受 `outputs/starry-dynamic-tests.patch` 作为第 9 步可应用的 tgoskits 测试补丁？ | pending human review |
| 4 | 是否确认第 9 步应先应用该测试补丁，再逐个运行已绑定的 riscv64 命令并记录日志/结果？ | pending human review |

## 缺口和风险

- 第 08 步仍不运行测试，不产生 runtime pass/fail 结论。
- `readonly filesystem or mount state` 没有在首轮 patch 中强制构造；若第 09 步环境没有 readonly mount fixture，应记录为 skipped/limitation。
- 第 08 步没有关闭第 07 步的 runtime `risk` items；这些项目需要第 09 步执行并确认。
- 第 08 步没有关闭 `T07-SOURCE-SPEC-GAP`；closeout 前仍需明确接受当前 source basis，或刷新 spec。
- 第 08 步没有关闭 `T07-STATIC-CHECKER-GAP`；本批不能声称 automated static checker coverage。

## 输出

- 动态测试用例：`outputs/validation-cases.yaml`
- Starry 动态测试补丁：`outputs/starry-dynamic-tests.patch`
- Starry 动态测试命令清单：`outputs/starry-dynamic-tests.yaml`
- 审核门禁：`reviews/08-fix-plan-and-apply-outside-harness-signoff.yaml`
