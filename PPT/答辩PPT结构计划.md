# 硕士论文答辩 PPT 结构计划（15 分钟强主线版）

论文题目：基于 LoongArch 架构的 ART 执行引擎适配与优化技术研究  
建议模板：`/Users/yanxi/code/Latex/ucas-master/PPT/鄢玺毕业答辩.pptx`  
建议主线页数：16 页  
建议答辩时长：15 分钟  

## 总体叙事

15 分钟答辩不宜按论文六章顺序复述，应围绕一条更尖锐的主线展开：

**AOSP 15 官方缺少 LoongArch 平台 ART 执行引擎后端，Android 应用层真正运行的瓶颈集中在 ART 的解释、编译、JNI 与运行时入口闭合上。本文先补齐执行链，再建立可信实验基线，最后围绕真实瓶颈做定向优化并给出收益边界。**

建议把全文压缩为三句话：

1. 背景问题：LoongArch 平台缺少 AOSP 15 ART 执行引擎后端，应用执行链不闭合。
2. 方法路径：先建立可运行的执行底座，再从工作负载主路径中识别优化瓶颈。
3. 结果结论：适配具备工程可行性，优化收益具有工作负载边界，其中 LSX 向量化在规则浮点内核上收益最显著。

## 时间分配

| 模块 | 页数 | 建议时长 | 讲述重点 |
|---|---:|---:|---|
| 开场与问题定义 | 3 页 | 2 分钟 | 题目、主线、背景缺口 |
| 基础执行框架适配 | 4 页 | 3 分钟 | 当前问题、技术难点、适配方案、基线结果 |
| 优化瓶颈与方案设计 | 6 页 | 7 分钟 | 瓶颈来源、三类实现方案与对比 |
| 实验结果与结论 | 3 页 | 3 分钟 | 综合结果、收益边界、创新点与展望 |

## 主线页面结构

| 页码 | 页面标题 | 核心观点 | 建议展示形式 |
|---:|---|---|---|
| 1 | 标题页 | 本文研究对象是 AOSP 15 ART 在 LoongArch 平台上的执行引擎适配与优化。 | 使用学校模板封面；保留题目、姓名、导师、时间；不放技术细节。 |
| 2 | 一句话主线 | 本文从“执行链缺失”出发，完成 LoongArch 平台 ART 适配，并在统一基线上分析和优化关键瓶颈。 | 用一条横向路线：缺后端 -> 建执行链 -> 找瓶颈 -> 做优化 -> 给边界。 |
| 3 | 背景与缺口：Android 应用迁移卡在 ART 执行链 | LoongArch 具备基础系统条件，但 AOSP 15 缺少 LoongArch ART 执行引擎后端；应用层真正运行需要 ART 的解释、编译、JNI 和运行时入口闭合。 | 一张三层图：Android 应用层 / ART / LoongArch；在 ART 层标红“后端缺失、执行链不闭合”。 |
| 4 | 当前问题：不是单点移植，而是执行系统闭合 | ART 后端适配难点不在某一个文件，而在解释器、JIT、JNI、quick entrypoints、异常和 GC 可见性之间保持一致语义。 | 左侧列“缺失模块”，右侧列“必须闭合的语义”：调用约定、栈帧、返回通道、异常、对象引用。 |
| 5 | 基础适配方案：补齐 LoongArch ART 执行链 | 本文以执行路径为主线补齐 C++ 解释器、Nterp、JIT 后端、JNI 桥接和运行时快速入口。 | 使用 `Img/porting/art-porting-overview.pdf`，高亮本文覆盖模块。 |
| 6 | 实现难点：栈帧、调用约定与浮点语义 | Nterp、调用桩、JNI 与 JIT 必须共享栈帧约定；同时需要处理 LoongArch64 浮点 NaN 分类与 DEX 语义对齐。 | 使用 `Img/porting/nterp-frame-layout.pdf`；右侧只放 3 个关键词：栈帧、调用边界、NaN 语义。 |
| 7 | 可运行性与基线：执行模式形成性能阶梯 | 适配后，switch-interpreter、Nterp、JIT 与 JIT-on-first-use 在 LoongArch 上形成清晰性能层次；正确性验证作为后续实验的前置背书。 | 使用 `Img/mybenchmark/art-mode-comparison-speedup.pdf`；角落小字标注“run-test/libcore 已作为前置验证，详见备份页”。 |
| 8 | 优化瓶颈来源：从热点收缩为四类问题 | 本文只保留命中主路径、边界清晰、能统一对比的优化方向；最终聚焦 JIT 时机、字符串搬移、DEX 校验、LSX lowering 四类问题。 | 四象限矩阵：瓶颈类型、代表 workload、主导成本线索。 |
| 9 | 方案一：自适应 baseline JIT 提前触发 | 短生命周期负载的矛盾是热点方法尚未进入 baseline JIT 程序就结束；本文通过提前触发窗口缩短解释器驻留时间。 | 使用 `Img/optimization/scheme1-tiered-jit-flow.pdf`；口头讲“默认阈值偏晚 -> 提前窗口 -> 资源 Veto”。 |
| 10 | JIT 方案结果：启动期收益明显，突发负载受 Veto 约束 | 自适应 JIT 在 startup.crypto.aes/rsa/signverify 上分别提升 34.29%、21.48%、19.02%，在 mpegaudio 上 3 轮均值提升 14.95%；pmd 收益较小，说明资源否决机制限制激进编译。 | 数字卡片 + 小柱状图；主讲 startup.crypto 和 mpegaudio，pmd 作为边界说明。 |
| 11 | 方案二：字符串与 DEX 固定成本压缩 | 字符串路径针对小长度高频复制做 8 路批量搬移；DEX verifier 针对启动期主链做阶段化精简，二者都属于固定成本压缩。 | 左右双栏：左侧 `Img/optimization/scheme2-string-copy-paths.pdf`，右侧 `Img/optimization/dexverifier-phase-chain-mechanism.pdf`。 |
| 12 | 字符串与 DEX 结果：定向微优化，有明确边界 | 批量搬移在 pmd、mpegaudio 上分别提升 0.86%、0.71%；DEX 阶段化在 startup.helloworld 上最高提升 5.46%。这类机制收益不大，但能说明固定成本来源。 | 两组结果卡片；强调“小收益但边界清楚”，不要把它讲成主贡献。 |
| 13 | 方案三：LSX 向量化 lowering | 硬件有 LSX 不等于 ART 能自动用上，关键是补齐从向量 IR 到 LoongArch64 LSX 指令的后端 lowering 链路。 | 使用 `Img/optimization/scheme3-lsx-lowering.pdf`；口头强调“前端能形成向量 IR，后端必须能落到目标指令”。 |
| 14 | LSX 结果：规则浮点内核收益最显著 | `scimark.lu.small` 吞吐量由 46.22 提升到 66.74 ops/m，相对提升 44.40%，是本文最强单项结果；但它主要命中规则浮点循环。 | 大数字图：`46.22 -> 66.74 ops/m`、`+44.40%`；可配 `Img/mybenchmark/loongarch64-lsx-full-simd-ablation-geomean.pdf` 或简化柱状图。 |
| 15 | 综合结果与收益边界 | 三类方案命中不同主路径；单项机制有效不等于可以全局叠加，性能会受代码缓存、内存带宽和 JIT 代码生成相互制约。 | 使用 `Img/mybenchmark/final-comparison-heatmap.pdf`；重点讲“收益依赖 workload，不能简单外推”。 |
| 16 | 创新点、结论与展望 | 本文贡献集中在 LoongArch ART 执行链适配、统一实验基线和主路径优化边界分析；后续可推进 AOT、LSX/LASX 扩展和应用级验证。 | 总结页：三条创新点 + 三条结论 + 三条展望；最后接“感谢聆听，请各位老师批评指正”。 |

## 备份页建议

以下内容不进入 15 分钟主线，但建议放在 PPT 末尾备用，以应对老师追问：

| 备份页 | 标题 | 适用追问 |
|---:|---|---|
| B1 | 正确性验证流程 | 老师追问“性能结果是否建立在正确运行基础上”。使用 `Img/verification/experiment-validation-workflow.pdf`。 |
| B2 | run-test 与 libcore 验证结果 | 老师追问“到底跑了哪些测试”。放 1033 个 run-test、7 类 compiler 变体、6801 个实际执行组合。 |
| B3 | 阶段化适配路线 | 老师追问“适配过程如何推进”。使用 `Img/porting/art-porting-stages.pdf`。 |
| B4 | Nterp 细节：invoke 与栈帧切换 | 老师追问“实现难点具体在哪里”。放 Nterp-to-Nterp、Nterp-to-managed ABI、JNI 过渡。 |
| B5 | JIT 阈值与 Veto 条件 | 老师追问“为什么 pmd 收益不明显”。解释 pending compilation、Code Cache 与 profiling info 约束。 |
| B6 | 字符串 8 路批量搬移伪代码 | 老师追问“如何保证短字符串不越界”。展示 `i + 8 <= length` 主循环和尾部复制。 |
| B7 | DEX verifier 四阶段消融 | 老师追问“5.46% 来自哪一步”。展示 phase1、phase12、phase123、phase1234。 |
| B8 | LSX IR 到指令映射表 | 老师追问“具体 lowering 了哪些节点”。展示 `VecLoad/Store/Add/Sub/Mul/Cnv` 到 `vld/vst/vfadd/vfsub/vfmul/vffint`。 |
| B9 | 完整 SIMD 候选版消融 | 老师追问“为什么不做更完整 SIMD”。展示完整覆盖候选版并不在全局几何平均上天然更优。 |
| B10 | 多机制叠加冲突数据 | 老师追问“为什么不把所有优化打开”。展示 pmd、mpegaudio、lu.small 的非线性变化。 |
| B11 | 候选方案筛选关系 | 老师追问“为什么这些方案进入正文”。使用 `Img/optimization/candidate-schemes-screening-map.pdf`。 |

## 建议保留的原图素材

| 用途 | 建议图片 |
|---|---|
| 适配范围 | `Img/porting/art-porting-overview.pdf` |
| 阶段化适配 | `Img/porting/art-porting-stages.pdf` |
| Nterp 栈帧 | `Img/porting/nterp-frame-layout.pdf` |
| 执行路径协同 | `Img/porting/art-porting-runtime-paths.pdf` |
| 验证流程 | `Img/verification/experiment-validation-workflow.pdf` |
| 执行模式基线 | `Img/mybenchmark/art-mode-comparison-speedup.pdf` |
| 方案筛选 | `Img/optimization/candidate-schemes-screening-map.pdf` |
| JIT 进入时机 | `Img/optimization/scheme1-tiered-jit-flow.pdf` |
| 字符串搬移 | `Img/optimization/scheme2-string-copy-paths.pdf` |
| DEX 校验阶段链 | `Img/optimization/dexverifier-phase-chain-mechanism.pdf` |
| LSX lowering 链路 | `Img/optimization/scheme3-lsx-lowering.pdf` |
| LSX 能力边界 | `Img/optimization/scheme3-vectorization-boundary.pdf` |
| 综合结果 | `Img/mybenchmark/final-comparison-heatmap.pdf` |
| 结论收束 | `Img/conclusion/conclusion-layered-summary.pdf` |

## 口头表达原则

1. 不按论文段落复述，优先用“问题 -> 难点 -> 方案 -> 对比 -> 结果 -> 边界”的答辩语言。
2. 背景只讲到“为什么 ART 执行链是关键缺口”，不要展开国产生态大背景。
3. 验证流程只作为可信度背书，主线不展开 run-test 细表。
4. 每个优化方案都要讲清楚“瓶颈来源、我的方案、对比方案/边界、实验结果”。
5. LSX 向量化是最强结果，但不要外推成所有数值程序都提升；它命中的是规则浮点循环。
6. 批量搬移和 DEX verifier 不要包装成大贡献，应讲成“固定成本压缩的定向证据”。
7. JIT 机制要强调 Veto 的意义：pmd 上收益不大并非完全失败，而是说明突发负载下系统保护条件会主动限制激进编译。

## GitHub 源码复核摘要

目标服务器不可达时，可使用 GitHub 仓库 `https://github.com/android-la64/platform-art/tree/a15_larch` 作为源码复核入口。本轮已通过浅层稀疏检出核对 `a15_larch` 与 `optimize/All` 分支：

1. `a15_larch` 分支可访问，当前 HEAD 为 `0621c6a6a2d5f5a8b9cf6fbf8cb21af8cdba05e6`，提交信息为 `[compiler] complete and stabilize LoongArch64 SIMD coverage`。
2. LoongArch64 基础适配代码可在 `compiler/utils/loongarch64/`、`compiler/optimizing/code_generator_loongarch64.*`、`compiler/jni/quick/loongarch64/`、`runtime/arch/loongarch64/`、`runtime/interpreter/mterp/loongarch64/` 中对应到，覆盖汇编器、JIT 后端、JNI calling convention、quick entrypoints 和 Nterp。
3. Nterp 相关文件中可见 `ExecuteNterpImpl`、`NTERP_SIZE_SAVE_CALLEE_SAVES`、`NterpToNterpInstance`、`fclass`、`fcmp.cle/clt` 等实现痕迹，可支撑“栈帧/调用约定/浮点语义对齐”的答辩表述。
4. `optimize/All` 相对 `Base` 的差异覆盖 `runtime/jit/jit.cc`、`runtime/mirror/string-alloc-inl.h`、`runtime/mirror/string.cc`、`libdexfile/dex/dex_file_verifier.cc`、`compiler/optimizing/code_generator_loongarch64.cc` 等文件，可对应 JIT 阈值、字符串批量搬移、DEX verifier 阶段化和 LSX lowering 这几类优化。
5. 源码中可见 LSX 向量指令发射与 lowering 相关实现，如 `vld/vst`、`vreplgr2vr.*`、`vfadd.s/d`、`vfsub.s/d`、`vfmul.s/d`、`vffint.s.w`、`vffint.d.l`，可用于支撑“硬件 LSX 需要通过 ART 后端 lowering 链路才能转化为性能”的表述。

## 下一步制作建议

1. 按 16 页主线制作正式 PPT，备份页只在老师追问时使用。
2. 第 8 页开始进入优化主线，不再单独展开验证流程。
3. 候选方案筛选图放备份页，不进入主线，避免答辩现场显得像解释论文组织。
4. 制作 PPT 时同步准备每页 1-2 句讲稿，确保页面文字少，细节由口头说明承担。

## 复核备注

本结构基于当前论文仓库中的 `Thesis.tex`、`Tex/Chap_*.tex`、`Tex/Frontmatter.tex` 与图片目录整理，并已使用 GitHub 仓库 `android-la64/platform-art` 的公开分支补充复核源码侧实现痕迹。按仓库规则尝试访问外部 ART 与 benchmark 目录时，本机未挂载 `/workspace/aosp/...`，并且 `ssh la55` 在本轮连接超时，因此实验归档数据仍建议在最终 PPT 制作前复核 `/home/yanxi/loongson/aosp15.la/tmp/MyBenchMark`。
