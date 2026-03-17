# 2006-dacapo-benchmarks-oopsla 临时分析（Step2）

## Step1 提取确认
- 已使用 `pdftotext -layout` 提取全文：`/workspace/ucasthesis/Ref/文献/研读报告/_text/2006-dacapo-benchmarks-oopsla.txt`
- 提取覆盖范围：从论文首页到参考文献（按文本文件完整输出）

## 一、研究问题、假设与目标
When SPEC introduced these benchmarks, their evaluation Since benchmarks drive computer science research and industry rules and the community’s evaluation metrics glossed over some of product development, which ones we use and how we evaluate the key questions for Java benchmarking. For example, (1) SPEC them are key questions for the community. Despite complex run- reporting of the “best” execution time is taken from multiple it- time tradeoffs due to dynamic compilation and garbage collection erations of the benchmark within a single execution of the virtual required for Java programs, many evaluations still use methodolo- machine, which will typically eliminate compile time. (2) In ad- gies developed for C, C++, and Fortran. SPEC, the dominant pur- dition to steady state application performance, a key question for veyor of benchmarks, compounded this problem by institutionaliz- Java virtual machines (JVMs) is the tradeoff between compile and ing these methodologies for their Java benchmark suite.

## 二、方法论与数据来源
We first modify the compiler to record its sam- pling information and optimization decisions for each method, This experiment explores the space-time tradeoff of two full heap execute the benchmark n times, and select the best plan. We collectors: SemiSpace and MarkSweep as implemented in Jikes then execute the benchmark with the plan, measuring the first RVM [1] with MMTk [4, 5] across four architectures. We exper- iteration (mix) or the second (stable) depending on the experi- imentally determine the minimum heap size for each program us- ment. ing MarkCompact in MMTk. (These heap sizes, which are specific to MMTk and Jikes RVM version 2.4.4+, can be seen in the top The deterministic methodology produces a code base with opti- x-axes of Figures 2(a)–(d).) The virtual machine triggers collec- mized hot methods and baseline compiled code. Compiling all the tion when the application exhausts the heap space.

## 三、核心发现与关键数据
than C, C++, and Fortran which stress (4) much less, and of course do vary and report these metrics, but many do not. We use and introduce new value, time-series, This paper introduces the DaCapo benchmarks, a set of gen- and statistical metrics for static and dynamic properties such as eral purpose, realistic, freely available Java applications. This pa- code complexity, code size, heap composition, and pointer muta- per also recommends a number of methodologies for choosing and tions. No benchmark suite is definitive, but these metrics show that evaluating Java benchmarks, virtual machines, and their memory DaCapo improves over SPEC Java in a variety of ways, including management systems. Some of these methodologies are already in more complex code, richer object behaviors, and more demanding use. For example, Eeckhout et al.

关键数值线索：未在自动抽取中识别到稳定格式数值，请在原文结果章节核对。

## 四、理论贡献与实践意义
该文属于“基准测试方法学与统计规范”方向，对执行引擎优化与实验论证链条提供直接参考。可用于你的论文中：相关工作、方法依据、结果解释、威胁与有效性分析。

## 五、根本矛盾、切入视角、方法创新
- 根本矛盾：性能收益与系统开销/稳定性之间的冲突。
- 切入视角：将问题机制化并通过实验闭环验证。
- 方法创新：把优化目标、实现路径和评测证据统一在同一研究框架下。
