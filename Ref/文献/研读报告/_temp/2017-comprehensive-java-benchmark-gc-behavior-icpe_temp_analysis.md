# 2017-comprehensive-java-benchmark-gc-behavior-icpe 临时分析（Step2）

## Step1 提取确认
- 已使用 `pdftotext -layout` 提取全文：`/workspace/ucasthesis/Ref/文献/研读报告/_text/2017-comprehensive-java-benchmark-gc-behavior-icpe.txt`
- 提取覆盖范围：从论文首页到参考文献（按文本文件完整输出）

## 一、研究问题、假设与目标
Considerable effort has been put into building benchmark Benchmark suites are an indispensable part of scientific re- suites to represent diverse and real-world applications. The search to compare different approaches against each another. most widely used Java benchmark suites are DaCapo1 in- The diversity of benchmarks is an important asset to eval- troduced by Blackburn et al. [2], DaCapo Scala2 introduced uate novel approaches for effectiveness and weaknesses. [7], SPECjvm20083 analyzed by Shiv et al.

## 二、方法论与数据来源
sunflow 20 large 11.06 This section describes the research methodology, i.e., the tomcat 10 huge 17.02 benchmarks we used and their configuration, the hardware tradebeans 10 huge 278.42 setup, as well as the method of measurement. tradesoap 10 huge 110.81 xalan 20 large 5.16 Benchmarks. actors 5 gargantuan 17.02 Figure 1 shows all benchmarks of the DaCapo (version apparat 5 gargantuan 66.68 9.12), DaCapo Scala (version 0.1.0-20120216.103539-3) and factorie 5 gargantuan 558.27 DaCapo Scala SPECjvm2008 benchmark suite, i.e., all benchmarks we will kiama 40 default 6.45 examine in this paper. It also shows the input used, the scalac 20 large 71.86 number of warmups performed before measurement, and the scaladoc 20 large 68.44 live size of every benchmark. The live size is defined as the scalap 20 large 5.76 maximum number of bytes alive at any given point in time

## 三、核心发现与关键数据
We do not want to Keywords encourage cherry-picking benchmarks but rather enable re- searchers and reviewers to better evaluate the work of others. Java, Benchmarks, Memory Behavior, GC Behavior, Da- We will show important properties of popular Java bench- Capo, DaCapo Scala, SPECjvm2008 marks, as well as curiosities one should be aware of when using them and when evaluating other work based on these 1. INTRODUCTION benchmarks. Furthermore, we split the benchmarks into cat- Benchmarks are a state-of-the-art method to determine egories, depending on observed properties, such as allocated the quality of virtual machines, compiler optimizations, memory, survivor ratios, live sizes, and garbage collection garbage collection algorithms, and monitoring tools in terms times under different virtual machine configurations. We se- of performance. Results of such measurements are used, for lected DaCapo, DaCapo Scala and SPECjvm2008 because example, to argue the superiority of one garbage collection they are the most popular Java benchmark suites, they are algorithm over another, to demonstrate the benefits of a new free to use, and they are open source, which makes them optimization technique, or to evaluate the overhead of a new ideal for scientific evaluations.

关键数值线索：未在自动抽取中识别到稳定格式数值，请在原文结果章节核对。

## 四、理论贡献与实践意义
该文属于“基准测试方法学与统计规范”方向，对执行引擎优化与实验论证链条提供直接参考。可用于你的论文中：相关工作、方法依据、结果解释、威胁与有效性分析。

## 五、根本矛盾、切入视角、方法创新
- 根本矛盾：性能收益与系统开销/稳定性之间的冲突。
- 切入视角：将问题机制化并通过实验闭环验证。
- 方法创新：把优化目标、实现路径和评测证据统一在同一研究框架下。
