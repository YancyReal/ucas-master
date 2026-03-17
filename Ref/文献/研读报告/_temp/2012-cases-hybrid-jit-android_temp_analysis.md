# 2012-cases-hybrid-jit-android 临时分析（Step2）

## Step1 提取确认
- 已使用 `pdftotext -layout` 提取全文：`/workspace/ucasthesis/Ref/文献/研读报告/_text/2012-cases-hybrid-jit-android.txt`
- 提取覆盖范围：从论文首页到参考文献（按文本文件完整输出）

## 一、研究问题、假设与目标
compiled and translated into native instructions like classi- The Dalvik virtual machine is the main application plat- cal programming languages are. Instead, a program written form running on Google’s Android operating system for mo- using them is read line by line and executed by an inter- bile devices and tablets. It is a Java Virtual Machine run- mediate engine or virtual machine. The process of fetching ning a basic trace-based JIT compiler, unlike web browser each instruction and the execution of it can be much slower JavaScript engines that usually run a combination of both than how a native program is usually ran. This problem method and trace-based JIT types.

## 二、方法论与数据来源
and trace-based JIT types. We developed a method- has traditionally been dealt with by adding a Just-In-Time based JIT compiler based on the Low Level Virtual Machine (JIT) Compiler to the virtual machine [25] [4]. A JIT Com- framework that delivers performance improvement compa- piler is a compiler that takes a code sequence or code block rable to that of an Ahead-Of-Time compiler. We compared and translates it into native code during run time in order our method-based JIT against Dalvik’s own trace-based JIT to improve its execution time. using common benchmarks available in the Android Market. The Java language is an example of an interpreted lan- Our results show that our method-based JIT is better than guage which runs on top of Oracle’s JavaTM Virtual Machine a basic trace-based JIT, and that, by sharing profiling and (JVM).

## 三、核心发现与关键数据
brary compiled for the user’s hardware. ers, Interpreters, Code generation, Optimization, Parsing, The use of JNI to interface with the virtual machine is also Retargetable compilers a problem because of the overhead required to change from the interpreted to the native environment and back [20]. It General Terms is also possible to compile an application written in Java to a native binary file using Java to native compilers [9] [32] but Performance, Design, Experimentation, Languages the resulting binary and the libraries needed to execute it need to be compiled for the user’s platform as well, making Keywords this and the previous approaches less portable than the JVM Method-Based, Trace-Based, JIT, Android, Dalvik VM and Google’s Dalvik virtual machine. Because of these rea- sons most Java applications are written using mostly Java 1. INTRODUCTION and are therefore benefited by a VM’s JIT compiler. As of Java 1.3, the standard HotSpot became the default Sun Interpreted and Dynamic languages have been on the rise Java Virtual Machine [29].

关键数值线索：未在自动抽取中识别到稳定格式数值，请在原文结果章节核对。

## 四、理论贡献与实践意义
该文属于“ART执行引擎与JIT策略”方向，对执行引擎优化与实验论证链条提供直接参考。可用于你的论文中：相关工作、方法依据、结果解释、威胁与有效性分析。

## 五、根本矛盾、切入视角、方法创新
- 根本矛盾：性能收益与系统开销/稳定性之间的冲突。
- 切入视角：将问题机制化并通过实验闭环验证。
- 方法创新：把优化目标、实现路径和评测证据统一在同一研究框架下。
