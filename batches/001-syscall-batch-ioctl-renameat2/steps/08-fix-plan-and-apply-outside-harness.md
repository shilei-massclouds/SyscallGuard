# 步骤 08 - Fix Plan And Apply Outside Harness

批次：`001-syscall-batch-ioctl-renameat2`
状态：`pending_human_review`

## 目的

根据第 07 步 triage，产出第 09 步要执行的动态测试用例清单。本步不生成 Starry patch，
也不询问是否应用 patch；Starry patch 候选由第 09 步根据第 06 步静态检查/审计结果和第 09 步
动态测试结果生成。

## 输入

- `manifest.yaml`
- `steps/07-gap-triage.md`
- `docs/tooling-roadmap.md`
- 外部 Starry source ref：`tgoskits-local`，branch `dev-ltp-spec-2`，commit
  `4f30e12d17e4da175233bb3a51889efe747a45f9`

## 外部修改结论

| Area | Decision | Evidence / reason |
| --- | --- | --- |
| Starry patch generation | `deferred_to_step09` | patch 候选需要结合第 06 步静态检查/审计结果和第 09 步动态测试结果生成。 |
| Spec/tool refresh | `planned_later` | `T07-SOURCE-SPEC-GAP` 和 `T07-IOCTL-REQUEST-SPLIT` 需要后续 spec/refinement 决策。 |
| Static checker integration | `planned_later` | `T07-STATIC-CHECKER-GAP` 需要后续把外部 checker 参数化后再接入。 |
| Dynamic validation cases | `generated_for_review` | 7 个 `risk` items 已转成第 09 步执行用例，等待人工确认。 |

## 第 07 步 triage 处置表

| Triage ID | Step 08 disposition | Apply now | Follow-up owner |
| --- | --- | --- | --- |
| `T07-IOCTL-REQUEST-SPLIT` | 作为 spec refinement 计划保留；本轮不拆分当前批次范围 | no | future spec refresh / later ioctl sub-batch |
| `T07-DYNAMIC-PERMISSION` | 交给 Step 09 动态权限验证或 limitation 接受 | no | Step 09 validation |
| `T07-DYNAMIC-FS-SIDE-EFFECT` | 交给 Step 09 文件系统状态验证或 limitation 接受 | no | Step 09 validation |
| `T07-DYNAMIC-DIRENT` | 交给 Step 09 目录枚举验证或 limitation 接受 | no | Step 09 validation |
| `T07-FD-TYPE-MATRIX` | 交给 Step 09 fd 类型矩阵验证或 limitation 接受 | no | Step 09 validation |
| `T07-PATH-ERRNO-PRIORITY` | 交给 Step 09 路径 errno 优先级验证或 limitation 接受 | no | Step 09 validation |
| `T07-USERPTR-EFAULT` | 交给 Step 09 bad-pointer 验证或 limitation 接受 | no | Step 09 validation |
| `T07-MODE-UID-GID` | 交给 Step 09 创建元数据验证或 limitation 接受 | no | Step 09 validation |
| `T07-SOURCE-SPEC-GAP` | 本轮不回滚重做 Step 02/03；作为 closeout 前需明确接受或刷新项目保留 | no | closeout review / future extractor run |
| `T07-STATIC-CHECKER-GAP` | 本轮不接入 checker；保留人工审计结论并禁止声称 automated checker coverage | no | future checker integration |

## 后续计划记录

### `P08-SPEC-IOCTL-REQUESTS`

- Source item：`T07-IOCTL-REQUEST-SPLIT`
- Plan：后续把 `ioctl` 从 syscall-level rule refs 拆成 request classes，或在规格中明确排除不覆盖的 request classes。
- Current batch boundary：不在当前 Step 08 修改规格表，不阻塞进入 Step 09。
- Closeout impact：阻塞 `ioctl` 的完整 closeout，除非 closeout review 接受当前 limitation。

### `P08-SPEC-EXTRACTOR-REFRESH`

- Source item：`T07-SOURCE-SPEC-GAP`
- Plan：未来可用 spec extraction 工具抽取候选行为，再映射到 SyscallGuard 的 syscall table、reusable rule table 和 target mapping。
- Current batch boundary：本轮按已审核的从头 draft/reference 模型继续；不继承旧处理进度。
- Closeout impact：最终 closeout 必须明确接受当前 source basis，或在后续批次/返工中刷新 spec。

### `P08-STATIC-CHECKER-INTEGRATION`

- Source item：`T07-STATIC-CHECKER-GAP`
- Plan：未来可把静态检查工具改造成读取 reusable rules / batch mappings 的参数化 checker，并输出结构化 audit result。
- Current batch boundary：本轮保留第 06 步人工静态审计；不声明自动静态 checker 已覆盖。
- Closeout impact：不阻塞进入 Step 09；阻塞任何 automated checker coverage claim。

### `P08-DYNAMIC-VALIDATION-MATRIX`

- Source items：`T07-DYNAMIC-PERMISSION`、`T07-DYNAMIC-FS-SIDE-EFFECT`、`T07-DYNAMIC-DIRENT`、`T07-FD-TYPE-MATRIX`、`T07-PATH-ERRNO-PRIORITY`、`T07-USERPTR-EFAULT`、`T07-MODE-UID-GID`
- Plan：Step 08 生成动态测试用例清单；Step 09 在本步被批准后自动执行这些用例，并结合第 06 步静态检查/审计结果生成 Starry patch 候选。
- Current batch boundary：Step 08 不运行测试，不制造 validation 结果。
- Closeout impact：这些 risk items 在 Step 09 执行并确认前仍阻塞 closeout。

## Dynamic validation cases for Step 09

结构化用例文件：`outputs/validation-cases.yaml`。

| Case ID | Source triage | Scope | Step 08 status | Step 09 expectation |
| --- | --- | --- | --- | --- |
| `V09-PERMISSION-MATRIX` | `T07-DYNAMIC-PERMISSION` | permission-sensitive path mutation syscalls | `planned_pending_review` | execute or record execution blocker |
| `V09-FS-SIDE-EFFECT` | `T07-DYNAMIC-FS-SIDE-EFFECT` | cwd/root updates and filesystem mutations | `planned_pending_review` | execute or record execution blocker |
| `V09-DIRENT-ENUMERATION` | `T07-DYNAMIC-DIRENT` | `getdents64` directory entry enumeration | `planned_pending_review` | execute or record execution blocker |
| `V09-FD-TYPE-MATRIX` | `T07-FD-TYPE-MATRIX` | `ioctl`, `fchdir`, `getdents64` fd type matrix | `planned_pending_review` | execute or record execution blocker |
| `V09-PATH-ERRNO-PRIORITY` | `T07-PATH-ERRNO-PRIORITY` | pathname, dirfd, and `*at` errno priority | `planned_pending_review` | execute or record execution blocker |
| `V09-USERPTR-EFAULT` | `T07-USERPTR-EFAULT` | bad user pointer behavior | `planned_pending_review` | execute or record execution blocker |
| `V09-MODE-UID-GID` | `T07-MODE-UID-GID` | mode, uid, gid, and node metadata | `planned_pending_review` | execute or record execution blocker |

当前用例清单定义了场景和 scope，但没有绑定可直接运行的命令。第 09 步进入执行阶段时，
如果仍没有命令、环境或日志路径，就应把结果记录为 execution blocker，而不是重新询问
是否要运行。

## Human review checklist

| No. | Question | Current answer |
| --- | --- | --- |
| 1 | 是否接受这 7 类动态测试用例清单？ | pending human review |
| 2 | 是否看清当前执行命令/环境仍缺失，若不补充，第 09 步会记录 execution blocker？ | pending human review |
| 3 | 是否确认进入第 09 步后自动执行已绑定用例，并基于第 06 步静态检查/审计结果和第 09 步动态结果生成 Starry patch 候选？ | pending human review |

## 缺口和风险

- 第 08 步没有关闭第 07 步的 7 个 runtime `risk` items；这些项目已转成 Step 09 待执行用例。
- 第 08 步没有关闭 `T07-SOURCE-SPEC-GAP`；closeout 前仍需明确接受当前 source basis，或刷新 spec。
- 第 08 步没有关闭 `T07-STATIC-CHECKER-GAP`；本批不能声称 automated static checker coverage。
- Step 09 可能因为缺少执行命令或环境而无法运行动态用例；届时必须记录为 execution blocker。

## 输出

- 动态测试用例清单记录在本文件。
- 动态测试用例：`outputs/validation-cases.yaml`
- 审核门禁：`reviews/08-fix-plan-and-apply-outside-harness-signoff.yaml`。
