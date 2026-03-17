# 2017-virtual-machine-warmup-blows-hot-and-cold-pacmpl 临时分析（Step2）

## Step1 提取确认
- 已使用 `pdftotext -layout` 提取全文：`/workspace/ucasthesis/Ref/文献/研读报告/_text/2017-virtual-machine-warmup-blows-hot-and-cold-pacmpl.txt`
- 提取覆盖范围：从论文首页到参考文献（按文本文件完整输出）

## 一、研究问题、假设与目标
Virtual Machine Warmup Blows Hot and Cold∗ EDD BARRETT, King’s College London, UK CARL FRIEDRICH BOLZ-TEREICK, King’s College London, UK REBECCA KILLICK, Lancaster University, UK arXiv:1602.00602v6 [cs.PL] 6 Oct 2017 SARAH MOUNT, King’s College London, UK LAURENCE TRATT, King’s College London, UK Virtual Machines (VMs) with Just-In-Time (JIT) compilers are traditionally thought to execute programs in two phases: the initial warmup phase determines which parts of a program would most benefit from dynamic compilation, before JIT compiling those parts into machine code; subsequently the program is said to be at a steady state of peak performance. Measurement methodologies almost always discard data collected during the warmup phase such that reported measurements focus entirely on peak performance. We introduce a fully automated statistical approach, based on changepoint analysis, which allows us to deter Many modern languages are implemented as Virtual Machines (VMs) which use a Just-In-Time (JIT) compiler to translate ‘hot’ parts of a program into efficient machine code at run-time. Since it takes time to identify and JIT compile the ‘hot’ parts of a program, VMs using a JIT compiler are said to be subject to a warmup phase.

## 二、方法论与数据来源
described by Tukey [1977], conservatively defining an outlier as one that, within a sliding window of 200 in-process iterations, lies outside the median ±3 × (90%ile − 10%ile). In order that we avoid classifying slow warmup iterations at the start of an execution as outliers (when they are in fact likely to be important warmup data), we ignore the first 200 in-process iterations. Of the 7,320,000 in-process iterations, 0.3% are classified as outliers, with the most for any single process execution being 11.2% of in-process iterations. 4.2 Changepoint Analysis Intuitively, in order to uncover if/when warmup has completed, we need to determine when in- process iteration timings have ‘shifted’ in nature (i.e. become faster or slower). For example, for traditional warmup, we would expect to see a number of in-process iterations taking time t to be followed by a number at time t ′ (where t ′ < t).

## 三、核心发现与关键数据
such that, for each machine, each ⟨VM, benchmark⟩ has a consistent environment size. 3.5.2 Linux-specific Controls. On Linux, Krun controls several additional factors, sometimes by checking that the user has correctly set controls which can only be set manually. Krun uses cpufreq-set to set the CPU governor to performance mode (i.e. the highest non-overclocked frequency possible). To prevent the kernel overriding this setting, Krun verifies that the user has disabled Intel P-state support in the kernel by passing intel_pstate=disable as a kernel argument.

关键数值线索：50%

## 四、理论贡献与实践意义
该文属于“基准测试方法学与统计规范”方向，对执行引擎优化与实验论证链条提供直接参考。可用于你的论文中：相关工作、方法依据、结果解释、威胁与有效性分析。

## 五、根本矛盾、切入视角、方法创新
- 根本矛盾：性能收益与系统开销/稳定性之间的冲突。
- 切入视角：将问题机制化并通过实验闭环验证。
- 方法创新：把优化目标、实现路径和评测证据统一在同一研究框架下。
