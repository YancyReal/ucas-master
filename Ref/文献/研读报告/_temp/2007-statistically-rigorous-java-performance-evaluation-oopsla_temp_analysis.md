# 2007-statistically-rigorous-java-performance-evaluation-oopsla 临时分析（Step2）

## Step1 提取确认
- 已使用 `pdftotext -layout` 提取全文：`/workspace/ucasthesis/Ref/文献/研读报告/_text/2007-statistically-rigorous-java-performance-evaluation-oopsla.txt`
- 提取覆盖范围：从论文首页到参考文献（按文本文件完整输出）

## 一、研究问题、假设与目标
General Terms Experimentation, Measurement, Perfor- Java performance is far from being trivial to benchmark because mance it is affected by various factors such as the Java application, its input, the virtual machine, the garbage collector, the heap size, etc. Keywords Java, benchmarking, data analysis, methodol- In addition, non-determinism at run-time causes the execution time ogy, statistics of a Java program to differ from run to run. There are a number of sources of non-determinism such as Just-In-Time (JIT) compilation 1. Introduction and optimization in the virtual machine (VM) driven by timer- based method sampling, thread scheduling, garbage collection, and Benchmarking is at the heart of experimental computer sci- various system effects. ence research and development.

## 二、方法论与数据来源
for dealing with the non-determinism in managed • We advocate adding statistical rigor to performance eval- runtime systems. uation studies of managed runtime systems, and in partic- The pitfall in using a prevalent method is illustrated in ular Java systems. The motivation for statistically rigor- Figure 1 which compares the execution time for running ous data analysis is that statistics, and in particular con- Jikes RVM with five garbage collectors (CopyMS, GenCopy, fidence intervals, enable one to determine whether dif- GenMS, MarkSweep and SemiSpace) for the SPECjvm98 ferences observed in measurements are due to random db benchmark with a 120MB heap size — the experi- fluctuations in the measurements or due to actual differ- mental setup will be detailed later. This graph compares ences in the alternatives compared against each other. We the prevalent ‘best’ method which reports the best perfor- discuss how to compute confidence intervals and discuss mance number (or smallest execution time) among 30 mea- techniques to compare multiple alternatives. surements against a statistically rigorous method which re- ports 95% confidence intervals;

## 三、核心发现与关键数据
others report the best or second best performance ob- search ideas. As such, it is absolutely crucial to have a rig- served; yet others report the worst. Some iterate the benchmark orous benchmarking methodology. A non-rigorous method- multiple times within a single VM invocation; others consider mul- ology may skew the overall picture, and may even lead to tiple VM invocations and iterate a single benchmark execution;

关键数值线索：95%、90%、100%、99%、1%、2%、50%、8%

## 四、理论贡献与实践意义
该文属于“基准测试方法学与统计规范”方向，对执行引擎优化与实验论证链条提供直接参考。可用于你的论文中：相关工作、方法依据、结果解释、威胁与有效性分析。

## 五、根本矛盾、切入视角、方法创新
- 根本矛盾：性能收益与系统开销/稳定性之间的冲突。
- 切入视角：将问题机制化并通过实验闭环验证。
- 方法创新：把优化目标、实现路径和评测证据统一在同一研究框架下。
