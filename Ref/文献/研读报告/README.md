# 研读报告总览（paper-parse）

本目录基于 `paper-parse` 工作流，为 `Ref/文献` 下全部 PDF 生成双模研读报告（Part A + Part B）与临时分析文件（Step2）。

- 报告总数：26
- 临时分析总数：26
- 提取全文目录：`_text/`
- 临时分析目录：`_temp/`

你的论文题目为《基于LoongArch架构的ART虚拟机执行引擎适配与优化技术研究》，本 README 的重点是：逐篇给出“这篇文献讲什么”以及“如何落到你现有论文章节与实验口径”。

## 1. 逐篇文献简介与论文使用方式

| 分组 | 文献（对应报告） | 一句话简介 | 在毕业论文中的使用方式（建议章节） |
|---|---|---|---|
| ART/JIT | `2011-cases-method-based-aot-android_研读报告.md` | 讨论 Android 方法级 AOT 的实现与收益边界。 | 用于 `Tex/Chap_Related.tex` 的 JIT/AOT 背景与 `Tex/Chap_Conclusion.tex` 的“完善AOT支持”展望。 |
| ART/JIT | `2012-cases-hybrid-jit-android_研读报告.md` | 比较并融合不同 JIT 形态，强调分层与协作策略。 | 用于 `Tex/Chap_Optimization.tex` 的方案一（热度阈值）理论依据与参数讨论。 |
| ART/JIT | `2017-artist-android-runtime-instrumentation-arxiv_研读报告.md` | Android Runtime 插桩框架，强调可观测性与安全性。 | 用于 `Tex/Chap_Verification.tex` 的辅助调试/数据采集方法说明。 |
| ART/JIT | `2018-sharejit-code-cache-sharing-arxiv_研读报告.md` | 跨进程共享 JIT 代码缓存，减少重复编译与缓存占用。 | 用于 `Tex/Chap_Related.tex` 的相关工作补充；可作为后续“跨进程复用”扩展方向写入 `Tex/Chap_Conclusion.tex`。 |
| ART/JIT | `2020-end-the-senseless-killing-atc20_研读报告.md` | Marvin 通过运行时-内核协同改进移动端内存管理。 | 用于 `Tex/Chap_Related.tex` 的运行时内存管理讨论，并支撑你对“移动端时延约束下为何难以依赖传统swap”的论证。 |
| ART/JIT | `2022-hubble-jit-method-tracing-osdi22_研读报告.md` | 生产环境低开销方法级 tracing 的系统化设计。 | 用于 `Tex/Chap_Verification.tex` 的性能数据采集方法学与显著性分析口径。 |
| 解释器/字符串 | `2003-structure-and-performance-of-efficient-interpreters-jilp_研读报告.md` | 系统梳理高效解释器结构与性能主因。 | 用于 `Tex/Chap_Related.tex` 的解释器/Nterp 技术背景。 |
| 解释器/字符串 | `2004-java-jit-vm-improvements-usenix-vm_研读报告.md` | Java VM 与 JIT 的工程改进案例。 | 用于 `Tex/Chap_Related.tex` 的执行引擎演进脉络。 |
| 解释器/字符串 | `2005-optimizing-indirect-branch-prediction-vm-interpreters-toplas_研读报告.md` | 解释器分派中间接分支预测优化。 | 用于 `Tex/Chap_Porting.tex` 解释器/Nterp 分派路径设计讨论。 |
| 解释器/字符串 | `2008-analysis-reduction-memory-inefficiencies-java-strings-oopsla_研读报告.md` | 字符串布局优化减少内存冗余并改善性能。 | 用于 `Tex/Chap_Optimization.tex` 的方案二（字符串路径）背景与对照。 |
| 解释器/字符串 | `2008-simd-text-processing-utf8-to-utf16-ppopp_研读报告.md` | SIMD 加速 UTF-8/UTF-16 文本处理。 | 用于 `Tex/Chap_Conclusion.tex` 的“LoongArch 向量扩展优化”展望。 |
| 解释器/字符串 | `2010-compact-efficient-strings-for-java-scp_研读报告.md` | 合并 String 元数据与字符存储，降低 GC 与访问开销。 | 直接用于 `Tex/Chap_Optimization.tex` 方案二的机制来源与收益解释模板。 |
| 解释器/字符串 | `2010-efficient-interpretation-using-quickening-dls_研读报告.md` | quickening 驱动的解释器组合优化（含引用计数冗余消除）。 | 用于 `Tex/Chap_Related.tex` 的解释器优化理论；也可用于 `Tex/Chap_Optimization.tex` 失败方案反思。 |
| 解释器/字符串 | `2010-inline-caching-meets-quickening-ecoop_研读报告.md` | 无 JIT 场景下将 inline cache 与 quickening 结合。 | 用于解释器热点优化可行性分析，建议写入 `Tex/Chap_Related.tex` 与 `Tex/Chap_Optimization.tex` 对照段。 |
| 解释器/字符串 | `2021-validating-utf8-less-than-one-instruction-arxiv_研读报告.md` | 极致 UTF-8 验证吞吐优化。 | 用于 `Tex/Chap_Conclusion.tex` 的字符串/编码向量化潜在方向。 |
| 解释器/字符串 | `2022-transcoding-billions-unicode-simd-arxiv_研读报告.md` | 大规模 Unicode 转码的 SIMD 方法。 | 用于后续 LoongArch LSX/LASX 在字符串路径上的可迁移性讨论。 |
| 解释器/字符串 | `2023-transcoding-unicode-avx512-arxiv_研读报告.md` | AVX-512 下 Unicode 转码优化。 | 用于“跨 ISA 优化思路迁移”的展望，放在 `Tex/Chap_Conclusion.tex`。 |
| 基准方法学 | `2006-dacapo-benchmarks-oopsla_研读报告.md` | DaCapo 基准设计原则与代表性。 | 直接用于 `Tex/Chap_Verification.tex` 的 benchmark 选择依据。 |
| 基准方法学 | `2006-dacapo-extended-tr-cs-06-01_研读报告.md` | DaCapo 扩展技术报告，补充子项与方法细节。 | 用于 `Tex/Chap_Verification.tex` 的 workload 覆盖说明。 |
| 基准方法学 | `2007-statistically-rigorous-java-performance-evaluation-oopsla_研读报告.md` | Java 性能评测的统计严谨性框架。 | 直接用于 `Tex/Chap_Verification.tex` 的重复实验与显著性检验口径。 |
| 基准方法学 | `2016-dont-get-caught-in-the-cold-warmup-your-jvm-osdi_研读报告.md` | JVM warmup 影响性能判断。 | 用于 `Tex/Chap_Verification.tex` 的预热策略与采样窗口设置。 |
| 基准方法学 | `2017-comprehensive-java-benchmark-gc-behavior-icpe_研读报告.md` | Java benchmark 的 GC 行为画像。 | 用于 `Tex/Chap_Verification.tex` 的 GC 指标采集解释。 |
| 基准方法学 | `2017-virtual-machine-warmup-blows-hot-and-cold-pacmpl_研读报告.md` | warmup 不稳定性与结果波动风险。 | 用于 `Tex/Chap_Verification.tex` 与 `Tex/Chap_Optimization.tex` 的结果可信度讨论。 |
| 基准方法学 | `2019-evaluating-renaissance-variety-performance-complexity-arxiv_研读报告.md` | Renaissance 的复杂度与多样性评估。 | 用于 `Tex/Chap_Conclusion.tex` 的“benchmark覆盖仍有限”论证。 |
| 基准方法学 | `2019-renaissance-benchmarking-suite-pldi_研读报告.md` | 面向并发/并行 JVM 工作负载的新基准套件。 | 用于 `Tex/Chap_Conclusion.tex` 的后续 benchmark 扩展计划。 |
| 架构文档 | `LoongArch-Vol1-v1.10-CN_研读报告.md` | LoongArch 基础架构、调用约定、访存与控制转移规则。 | 直接支撑 `Tex/Chap_Related.tex` 与 `Tex/Chap_Porting.tex` 的架构约束分析与实现说明。 |

## 2. 报告索引（PDF -> 报告 -> 临时分析）

| 源文献 | 双模报告 | 临时分析 |
|---|---|---|
| `01-ART-JIT/2011-cases-method-based-aot-android.pdf` | `2011-cases-method-based-aot-android_研读报告.md` | `_temp/2011-cases-method-based-aot-android_temp_analysis.md` |
| `01-ART-JIT/2012-cases-hybrid-jit-android.pdf` | `2012-cases-hybrid-jit-android_研读报告.md` | `_temp/2012-cases-hybrid-jit-android_temp_analysis.md` |
| `01-ART-JIT/2017-artist-android-runtime-instrumentation-arxiv.pdf` | `2017-artist-android-runtime-instrumentation-arxiv_研读报告.md` | `_temp/2017-artist-android-runtime-instrumentation-arxiv_temp_analysis.md` |
| `01-ART-JIT/2018-sharejit-code-cache-sharing-arxiv.pdf` | `2018-sharejit-code-cache-sharing-arxiv_研读报告.md` | `_temp/2018-sharejit-code-cache-sharing-arxiv_temp_analysis.md` |
| `01-ART-JIT/2020-end-the-senseless-killing-atc20.pdf` | `2020-end-the-senseless-killing-atc20_研读报告.md` | `_temp/2020-end-the-senseless-killing-atc20_temp_analysis.md` |
| `01-ART-JIT/2022-hubble-jit-method-tracing-osdi22.pdf` | `2022-hubble-jit-method-tracing-osdi22_研读报告.md` | `_temp/2022-hubble-jit-method-tracing-osdi22_temp_analysis.md` |
| `02-String-Interpreter/2003-structure-and-performance-of-efficient-interpreters-jilp.pdf` | `2003-structure-and-performance-of-efficient-interpreters-jilp_研读报告.md` | `_temp/2003-structure-and-performance-of-efficient-interpreters-jilp_temp_analysis.md` |
| `02-String-Interpreter/2004-java-jit-vm-improvements-usenix-vm.pdf` | `2004-java-jit-vm-improvements-usenix-vm_研读报告.md` | `_temp/2004-java-jit-vm-improvements-usenix-vm_temp_analysis.md` |
| `02-String-Interpreter/2005-optimizing-indirect-branch-prediction-vm-interpreters-toplas.pdf` | `2005-optimizing-indirect-branch-prediction-vm-interpreters-toplas_研读报告.md` | `_temp/2005-optimizing-indirect-branch-prediction-vm-interpreters-toplas_temp_analysis.md` |
| `02-String-Interpreter/2008-analysis-reduction-memory-inefficiencies-java-strings-oopsla.pdf` | `2008-analysis-reduction-memory-inefficiencies-java-strings-oopsla_研读报告.md` | `_temp/2008-analysis-reduction-memory-inefficiencies-java-strings-oopsla_temp_analysis.md` |
| `02-String-Interpreter/2008-simd-text-processing-utf8-to-utf16-ppopp.pdf` | `2008-simd-text-processing-utf8-to-utf16-ppopp_研读报告.md` | `_temp/2008-simd-text-processing-utf8-to-utf16-ppopp_temp_analysis.md` |
| `02-String-Interpreter/2010-compact-efficient-strings-for-java-scp.pdf` | `2010-compact-efficient-strings-for-java-scp_研读报告.md` | `_temp/2010-compact-efficient-strings-for-java-scp_temp_analysis.md` |
| `02-String-Interpreter/2010-efficient-interpretation-using-quickening-dls.pdf` | `2010-efficient-interpretation-using-quickening-dls_研读报告.md` | `_temp/2010-efficient-interpretation-using-quickening-dls_temp_analysis.md` |
| `02-String-Interpreter/2010-inline-caching-meets-quickening-ecoop.pdf` | `2010-inline-caching-meets-quickening-ecoop_研读报告.md` | `_temp/2010-inline-caching-meets-quickening-ecoop_temp_analysis.md` |
| `02-String-Interpreter/2021-validating-utf8-less-than-one-instruction-arxiv.pdf` | `2021-validating-utf8-less-than-one-instruction-arxiv_研读报告.md` | `_temp/2021-validating-utf8-less-than-one-instruction-arxiv_temp_analysis.md` |
| `02-String-Interpreter/2022-transcoding-billions-unicode-simd-arxiv.pdf` | `2022-transcoding-billions-unicode-simd-arxiv_研读报告.md` | `_temp/2022-transcoding-billions-unicode-simd-arxiv_temp_analysis.md` |
| `02-String-Interpreter/2023-transcoding-unicode-avx512-arxiv.pdf` | `2023-transcoding-unicode-avx512-arxiv_研读报告.md` | `_temp/2023-transcoding-unicode-avx512-arxiv_temp_analysis.md` |
| `03-Benchmark-Methodology/2006-dacapo-benchmarks-oopsla.pdf` | `2006-dacapo-benchmarks-oopsla_研读报告.md` | `_temp/2006-dacapo-benchmarks-oopsla_temp_analysis.md` |
| `03-Benchmark-Methodology/2006-dacapo-extended-tr-cs-06-01.pdf` | `2006-dacapo-extended-tr-cs-06-01_研读报告.md` | `_temp/2006-dacapo-extended-tr-cs-06-01_temp_analysis.md` |
| `03-Benchmark-Methodology/2007-statistically-rigorous-java-performance-evaluation-oopsla.pdf` | `2007-statistically-rigorous-java-performance-evaluation-oopsla_研读报告.md` | `_temp/2007-statistically-rigorous-java-performance-evaluation-oopsla_temp_analysis.md` |
| `03-Benchmark-Methodology/2016-dont-get-caught-in-the-cold-warmup-your-jvm-osdi.pdf` | `2016-dont-get-caught-in-the-cold-warmup-your-jvm-osdi_研读报告.md` | `_temp/2016-dont-get-caught-in-the-cold-warmup-your-jvm-osdi_temp_analysis.md` |
| `03-Benchmark-Methodology/2017-comprehensive-java-benchmark-gc-behavior-icpe.pdf` | `2017-comprehensive-java-benchmark-gc-behavior-icpe_研读报告.md` | `_temp/2017-comprehensive-java-benchmark-gc-behavior-icpe_temp_analysis.md` |
| `03-Benchmark-Methodology/2017-virtual-machine-warmup-blows-hot-and-cold-pacmpl.pdf` | `2017-virtual-machine-warmup-blows-hot-and-cold-pacmpl_研读报告.md` | `_temp/2017-virtual-machine-warmup-blows-hot-and-cold-pacmpl_temp_analysis.md` |
| `03-Benchmark-Methodology/2019-evaluating-renaissance-variety-performance-complexity-arxiv.pdf` | `2019-evaluating-renaissance-variety-performance-complexity-arxiv_研读报告.md` | `_temp/2019-evaluating-renaissance-variety-performance-complexity-arxiv_temp_analysis.md` |
| `03-Benchmark-Methodology/2019-renaissance-benchmarking-suite-pldi.pdf` | `2019-renaissance-benchmarking-suite-pldi_研读报告.md` | `_temp/2019-renaissance-benchmarking-suite-pldi_temp_analysis.md` |
| `04-Official-Docs/LoongArch-Vol1-v1.10-CN.pdf` | `LoongArch-Vol1-v1.10-CN_研读报告.md` | `_temp/LoongArch-Vol1-v1.10-CN_temp_analysis.md` |

## 3. 人工精修状态

已完成高质量精修（已覆盖全部 26 篇，重点对齐你的 LoongArch ART 论文）：

- `2011-cases-method-based-aot-android_研读报告.md`
- `2012-cases-hybrid-jit-android_研读报告.md`
- `2006-dacapo-benchmarks-oopsla_研读报告.md`
- `2007-statistically-rigorous-java-performance-evaluation-oopsla_研读报告.md`
- `2017-virtual-machine-warmup-blows-hot-and-cold-pacmpl_研读报告.md`
- `2019-renaissance-benchmarking-suite-pldi_研读报告.md`
- `2008-analysis-reduction-memory-inefficiencies-java-strings-oopsla_研读报告.md`
- `LoongArch-Vol1-v1.10-CN_研读报告.md`
- `2018-sharejit-code-cache-sharing-arxiv_研读报告.md`
- `2022-hubble-jit-method-tracing-osdi22_研读报告.md`
- `2010-compact-efficient-strings-for-java-scp_研读报告.md`
- `2020-end-the-senseless-killing-atc20_研读报告.md`
- `2010-efficient-interpretation-using-quickening-dls_研读报告.md`
- `2010-inline-caching-meets-quickening-ecoop_研读报告.md`
- `2003-structure-and-performance-of-efficient-interpreters-jilp_研读报告.md`
- `2004-java-jit-vm-improvements-usenix-vm_研读报告.md`
- `2005-optimizing-indirect-branch-prediction-vm-interpreters-toplas_研读报告.md`
- `2006-dacapo-extended-tr-cs-06-01_研读报告.md`
- `2008-simd-text-processing-utf8-to-utf16-ppopp_研读报告.md`
- `2016-dont-get-caught-in-the-cold-warmup-your-jvm-osdi_研读报告.md`
- `2017-artist-android-runtime-instrumentation-arxiv_研读报告.md`
- `2017-comprehensive-java-benchmark-gc-behavior-icpe_研读报告.md`
- `2019-evaluating-renaissance-variety-performance-complexity-arxiv_研读报告.md`
- `2021-validating-utf8-less-than-one-instruction-arxiv_研读报告.md`
- `2022-transcoding-billions-unicode-simd-arxiv_研读报告.md`
- `2023-transcoding-unicode-avx512-arxiv_研读报告.md`

## 4. 使用建议（与你当前实验数据对齐）

- 正式结论优先引用 `MyBenchMark/test-data/final-baseline/`、`scheme1/`、`scheme2/` 的结果，不使用 `screening/` 作为主结论证据。
- 统计学与 warmup 风险统一由 `2007`、`2016`、`2017 warmup` 三篇支撑，避免“只报均值”。
- 字符串路径优化的论证链建议固定为：`2008 strings` + `2010 compact strings` + 你自己的 `scheme2` 数据。
- JIT 阈值方案的论证链建议固定为：`2012 hybrid jit` + `ShareJIT`（阈值与缓存）+ 你自己的 `scheme1` 数据。
