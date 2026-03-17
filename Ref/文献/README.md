# 文献调研报告（面向论文《基于LoongArch架构的ART虚拟机执行引擎适配与优化技术研究》）

## 1. 调研目标与实验对齐

本批文献围绕你的两条“已验证有效/重点分析”实验主线组织：

- 主线A：`JIT 分层热度阈值调整`（对 `DaCapo/pmd` 有正收益，对 `SPECjvm2008/mpegaudio` 无稳定正收益）
- 主线B：`运行时字符串搬运批量化`（对 `DaCapo/pmd` 有稳定小幅收益，对 `mpegaudio` 无稳定正收益）

文献已落地到以下目录：

- `01-ART-JIT/`：ART/JIT与运行时策略
- `02-String-Interpreter/`：字符串热路径、解释器快路径、复制/转码优化
- `03-Benchmark-Methodology/`：DaCapo/SPEC/Renaissance 与评测方法学
- `04-Official-Docs/`：AOSP官方配置与LoongArch手册

---

## 2. ART/JIT 方向文献（`01-ART-JIT`）

### 2.1 `2011-cases-method-based-aot-android.pdf`

- 文献：A Method-Based Ahead-of-Time Compiler for Android Applications（CASES 2011）
- 核心价值：讨论 Android 上 AOT/JIT 的协同边界与热点方法处理策略。
- 在论文中的用法：
- 放在“相关工作：Android运行时编译策略”小节。
- 用于论证“不是单纯追求更早编译，而是要平衡编译开销与收益”。

### 2.2 `2012-cases-hybrid-jit-android.pdf`

- 文献：A Hybrid Just-In-Time Compiler for Android（CASES 2012）
- 核心价值：比较不同JIT策略与协作方式，强调阈值和触发机制的重要性。
- 在论文中的用法：
- 用于支撑你的 `warmup_threshold` 调整动机。
- 在实验章节解释“为何 pmd 受益而 mpegaudio 不受益”的机制差异。

### 2.3 `2017-artist-android-runtime-instrumentation-arxiv.pdf`

- 文献：ARTist: The Android Runtime Instrumentation and Security Toolkit（2017）
- 核心价值：展示基于 ART 编译链路做插桩/观测的方法。
- 在论文中的用法：
- 放在“工具链与可观测性”小节。
- 说明你使用 flamegraph/perf 追踪热点是符合 ART 生态研究范式的。

### 2.4 `2018-sharejit-code-cache-sharing-arxiv.pdf`

- 文献：ShareJIT（OOPSLA/PACMPL 2018）
- 核心价值：ART 场景下 JIT code cache 复用，降低重复编译成本。
- 在论文中的用法：
- 放在“JIT固定成本优化相关工作”。
- 用于对照你当前阈值优化仍受固定成本约束的问题。

### 2.5 `2020-end-the-senseless-killing-atc20.pdf`

- 文献：End the Senseless Killing（USENIX ATC 2020）
- 核心价值：移动系统内存管理优化与运行时协同，涉及 ART interpreter/compiler 路径。
- 在论文中的用法：
- 放在“运行时系统协同优化”。
- 可用于讨论“执行引擎优化不仅是JIT参数，还受系统层行为影响”。

### 2.6 `2022-hubble-jit-method-tracing-osdi22.pdf`

- 文献：Hubble（OSDI 2022）
- 核心价值：生产环境的 JIT 方法级追踪与性能调试。
- 在论文中的用法：
- 可作为“未来工作”引用：后续可引入更细粒度方法级追踪来收敛阈值参数。

---

## 3. 字符串/解释器方向文献（`02-String-Interpreter`）

### 3.1 `2003-structure-and-performance-of-efficient-interpreters-jilp.pdf`

- 文献：The Structure and Performance of Efficient Interpreters（JILP 2003）
- 核心价值：解释器分派、分支、局部性等经典性能规律。
- 在论文中的用法：
- 放在“执行引擎基础理论”。
- 支撑你对解释器热点下降与收益来源的解释。

### 3.2 `2004-java-jit-vm-improvements-usenix-vm.pdf`

- 文献：Java JIT Compiler and VM Improvements for Server and Middleware Applications（USENIX VM 2004）
- 核心价值：讨论 `arraycopy` 等复制热路径优化。
- 在论文中的用法：
- 对应你的“字符串搬运批量化”方案背景。
- 引用其“固定开销+长度分布”视角解释微优化收益上限。

### 3.3 `2005-optimizing-indirect-branch-prediction-vm-interpreters-toplas.pdf`

- 文献：Optimizing Indirect Branch Prediction Accuracy in Virtual Machine Interpreters（TOPLAS 2005）
- 核心价值：解释器间接分支预测对吞吐影响显著。
- 在论文中的用法：
- 作为“为何解释器阶段开销会主导短生命周期 workload”的理论依据。

### 3.4 `2008-analysis-reduction-memory-inefficiencies-java-strings-oopsla.pdf`

- 文献：Analysis and Reduction of Memory Inefficiencies in Java Strings（OOPSLA 2008）
- 核心价值：字符串对象冗余与复制成本分析。
- 在论文中的用法：
- 放在“字符串对象与搬运成本”相关工作。
- 直接支撑你对 `DoReplace/DoConcat/AllocFromUtf16` 作为热点的论证。

### 3.5 `2008-simd-text-processing-utf8-to-utf16-ppopp.pdf`

- 文献：A Case Study in SIMD Text Processing with Parallel Bit Streams（PPoPP 2008）
- 核心价值：UTF-8/UTF-16 转码中的批量并行思路。
- 在论文中的用法：
- 放在“未来优化方向（向量化/ISA特化）”。
- 与 LoongArch 向量扩展结合，提出后续可行路线。

### 3.6 `2010-compact-efficient-strings-for-java-scp.pdf`

- 文献：Compact and Efficient Strings for Java（SCP 2010）
- 核心价值：字符串布局与访问效率优化。
- 在论文中的用法：
- 解释为何“数据布局+复制实现”会共同影响字符串热点性能。

### 3.7 `2010-efficient-interpretation-using-quickening-dls.pdf`

- 文献：Efficient Interpretation using Quickening（DLS 2010）
- 核心价值：quickening 降低解释器分派成本。
- 在论文中的用法：
- 可在“执行引擎演化路径”中与你的JIT阈值优化形成对照：一个优化触发时机，一个优化解释执行本体。

### 3.8 `2010-inline-caching-meets-quickening-ecoop.pdf`

- 文献：Inline Caching Meets Quickening（ECOOP 2010）
- 核心价值：IC 与 quickening 结合优化热路径。
- 在论文中的用法：
- 放在“解释器/JIT协同”相关工作，补足你方案中的执行阶段协同视角。

### 3.9 `2021-validating-utf8-less-than-one-instruction-arxiv.pdf`

- 文献：Validating UTF-8 In Less Than One Instruction Per Byte（2021）
- 核心价值：UTF-8 校验极致吞吐优化。
- 在论文中的用法：
- 作为你“字符串批量化”方向的近期前沿支撑。
- 可引用于未来工作：将字符校验与搬运路径一体化优化。

### 3.10 `2022-transcoding-billions-unicode-simd-arxiv.pdf`

- 文献：Transcoding Billions of Unicode Characters per Second with SIMD Instructions（2022）
- 核心价值：超高吞吐字符转码工程实践。
- 在论文中的用法：
- 说明“批量化 + ISA 特化”路径在工程上可落地。

### 3.11 `2023-transcoding-unicode-avx512-arxiv.pdf`

- 文献：Transcoding Unicode Characters with AVX-512 Instructions（2023）
- 核心价值：更强向量指令下的转码优化上限。
- 在论文中的用法：
- 用作“上限参考”和“平台迁移讨论”：指出后续可探索 LoongArch 向量扩展上的对应实现。

---

## 4. 基准与评测方法文献（`03-Benchmark-Methodology`）

### 4.1 `2006-dacapo-benchmarks-oopsla.pdf`

- 文献：The DaCapo Benchmarks（OOPSLA 2006）
- 在论文中的用法：
- 实验平台与基准介绍的主引用。
- 说明你选择 `pmd` 的合理性与代表性。

### 4.2 `2006-dacapo-extended-tr-cs-06-01.pdf`

- 文献：DaCapo Extended Technical Report（TR-CS-06-01）
- 在论文中的用法：
- 补充 DaCapo 细节（工作负载结构、测量注意事项）。

### 4.3 `2007-statistically-rigorous-java-performance-evaluation-oopsla.pdf`

- 文献：Statistically Rigorous Java Performance Evaluation（OOPSLA 2007）
- 在论文中的用法：
- 直接用于定义重复实验、均值/方差、显著性报告规范。
- 强烈建议在正式论文实验章节落实该文建议。

### 4.4 `2016-dont-get-caught-in-the-cold-warmup-your-jvm-osdi.pdf`

- 文献：Don’t Get Caught in the Cold, Warm-up Your JVM（OSDI 2016）
- 在论文中的用法：
- 用于解释“短时 benchmark 对 warmup 敏感，可能出现误判”。
- 对你的 `mpegaudio` 波动解释非常关键。

### 4.5 `2017-comprehensive-java-benchmark-gc-behavior-icpe.pdf`

- 文献：A Comprehensive Java Benchmark Study on Memory and GC Behavior（ICPE 2017）
- 在论文中的用法：
- 对照 DaCapo/SPEC 子项差异（内存分配/GC行为），解释跨套件收益不一致。

### 4.6 `2017-virtual-machine-warmup-blows-hot-and-cold-pacmpl.pdf`

- 文献：Virtual Machine Warmup Blows Hot and Cold（PACMPL 2017）
- 在论文中的用法：
- 支撑“JIT warmup 非稳定且可能多峰”的结论。
- 强化你“至少 3~5 次重复实验”的方法学必要性。

### 4.7 `2019-renaissance-benchmarking-suite-pldi.pdf`

- 文献：Renaissance: Benchmarking Suite for Parallel Applications on the JVM（PLDI 2019）
- 在论文中的用法：
- 作为未来扩展基准集合的主要引用。
- 支撑你后续补充并发/现代JVM负载评测的计划。

### 4.8 `2019-evaluating-renaissance-variety-performance-complexity-arxiv.pdf`

- 文献：On Evaluating the Renaissance Benchmarking Suite（2019）
- 在论文中的用法：
- 用于说明基准“多样性/复杂度”与结果解释的关系，避免单一 workload 结论外推。

---

## 5. 官方资料与实现对照（`04-Official-Docs`）

### 5.1 `aosp-art-jit-compiler.html`

- 资料：AOSP 官方 ART JIT 文档
- 在论文中的用法：
- 用于“技术背景”章节说明 ART 的 JIT/AOT 协同机制。

### 5.2 `aosp-art-configure.html`

- 资料：AOSP 官方 ART 配置文档
- 在论文中的用法：
- 对应 `jit threshold`、`jitprithreadweight` 等参数解释。

### 5.3 `aosp-art-service-configure.html`

- 资料：AOSP ART Service 配置文档
- 在论文中的用法：
- 用于描述系统级 dexopt/编译策略与运行时性能关系。

### 5.4 `aosp-art-jit.cc`

- 资料：AOSP `runtime/jit/jit.cc` 源码快照
- 在论文中的用法：
- 方法实现细节引用（阈值触发、分层编译路径）。
- 可用于附录“关键代码定位索引”。

### 5.5 `LoongArch-Vol1-v1.10-CN.pdf`

- 资料：龙芯架构参考手册（卷一）
- 在论文中的用法：
- 用于架构背景与 ISA 特性介绍，支撑“为何做 LoongArch 特化优化”。

---

## 6. 可直接落到论文的写法建议

### 6.1 写作结构建议

- 第2章（背景与相关工作）：
- ART/JIT 机制（2.1）
- 解释器与字符串热路径优化（2.2）
- Java 基准评测方法学（2.3）
- 第3章（设计与实现）：
- 方案A：JIT阈值调优设计（3.1）
- 方案B：字符串搬运批量化设计（3.2）
- 第4章（实验与分析）：
- 基准设置与统计方法（4.1）
- `pmd`/`mpegaudio` 结果与反例分析（4.2）
- 威胁与有效性（4.3）

### 6.2 结合你当前实验结果的引用建议

- 当说明“阈值下调并非普适收益”时，优先引 `Hybrid JIT (2012)` + `VM Warmup Blows Hot and Cold (2017)`。
- 当说明“字符串微优化收益依赖负载特征”时，优先引 `Memory Inefficiencies in Java Strings (2008)` + `Compact Strings (2010)`。
- 当说明“实验必须多轮统计”时，优先引 `Statistically Rigorous (2007)` + `OSDI’16 Warmup`。

---

## 7. 后续可选增强（建议）

- 增补 1~2 篇 LoongArch/跨ISA JIT 后端公开论文（若获取到开放PDF）用于强化“架构适配”相关工作。
- 将本目录文献同步生成 `Biblio/ref.bib` 条目，后续可直接 `\\cite{}`。
- 对 `pmd/mpegaudio` 当前结果补齐 3~5 次重复实验后，再固定最终图表与结论措辞。
