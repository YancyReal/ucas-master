# 2018-sharejit-code-cache-sharing-arxiv 临时分析（Step2）

## Step1 提取确认
- 已使用 `pdftotext -layout` 提取全文：`/workspace/ucasthesis/Ref/文献/研读报告/_text/2018-sharejit-code-cache-sharing-arxiv.txt`
- 提取覆盖范围：从论文首页到参考文献（按文本文件完整输出）

## 一、研究问题、假设与目标
ShareJIT: JIT Code Cache Sharing across Processes and Its Practical Implementation XIAORAN XU, Rice University, USA arXiv:1810.09555v1 [cs.PL] 22 Oct 2018 KEITH COOPER, Rice University, USA JACOB BROCK, University of Rochester, USA YAN ZHANG, Futurewei Technologies, USA HANDONG YE, Futurewei Technologies, USA Just-in-time (JIT) compilation coupled with code caching are widely used to improve performance in dynamic programming language implementations. These code caches, along with the associated profiling data for the hot code, however, consume significant amounts of memory. Furthermore, they incur extra JIT compilation time for their creation. On Android, the current standard JIT compiler and its code caches are not shared among processes—that is, the runtime system maintains a private code cache, and its associated data, for each runtime process. H Runtime systems, execution engines and emulators for dynamic languages typically employ Just- in-Time (JIT) compilation on frequently executed sequences, and store the resulting compiled code in code caches for the use of subsequent executions.

## 二、方法论与数据来源
’s compiled code can be collected and freed. (See details in Section 3.4) The global JIT cache is divided into contiguous segments, each with a single writer, to simplify both management and synchronization. This scheme does not work for the global sharing map. Each process that uses the global sharing map needs the right to read and write it. Since Ashmem does not have a serialization mechanism for a multitude of readers and writers in a concurrent system, we use a semaphore to protect the global sharing map. 3.2 ShareJIT Workflow Figure 2 shows the main workflow of ShareJIT.

## 三、核心发现与关键数据
4.3 System-Wide Memory Utilization From the perspective of system-wide memory utilization, the effect of ShareJIT is conceptually simple. ShareJIT reduces system-wide memory use for compiled-code in proportion to the amount of sharing and the size of those methods. In practice, we can measure total memory use for compiled code with the standard Android JIT and with ShareJIT and subtract. To make predictions, however, is difficult because the actual savings depend on how different apps overlap in time and how the eviction policy for the shared cache works. Publication date: November 2018. 124:14 Xiaoran Xu, Keith Cooper, Jacob Brock, Yan Zhang, and Handong Ye In practice, we measured this effect and found that ShareJIT reduced overall JIT cache use by roughly 16%.

关键数值线索：16%、32GB

## 四、理论贡献与实践意义
该文属于“ART执行引擎与JIT策略”方向，对执行引擎优化与实验论证链条提供直接参考。可用于你的论文中：相关工作、方法依据、结果解释、威胁与有效性分析。

## 五、根本矛盾、切入视角、方法创新
- 根本矛盾：性能收益与系统开销/稳定性之间的冲突。
- 切入视角：将问题机制化并通过实验闭环验证。
- 方法创新：把优化目标、实现路径和评测证据统一在同一研究框架下。
