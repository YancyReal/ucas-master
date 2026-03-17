# 2020-end-the-senseless-killing-atc20 临时分析（Step2）

## Step1 提取确认
- 已使用 `pdftotext -layout` 提取全文：`/workspace/ucasthesis/Ref/文献/研读报告/_text/2020-end-the-senseless-killing-atc20.txt`
- 提取覆盖范围：从论文首页到参考文献（按文本文件完整输出）

## 一、研究问题、假设与目标
as mobile OSes replace desktop ones (e.g., Android is now To ensure low-latency memory allocation, mobile operating the most used OS in the world) and mobile apps replace systems kill applications instead of swapping memory to disk. desktop counterparts (e.g., Google Docs and Word Online This design choice shifts the burden of managing over-utilized replacing Microsoft Word). Today’s apps already do not fit memory to application programmers, requiring them to con- into their memory allocation, so they manually swap objects stantly checkpoint their application state to disk. This paper between memory and local storage or use libraries to meet presents Marvin, a new memory manager for mobile plat- their needs [11]. Because apps are increasingly likely to be forms that efficiently supports swapping while meeting the killed due to memory pressure, they must also continuously strict performance requirements of mobile apps.

## 二、方法论与数据来源
based on that release. Both our Marvin imple- objects with live JNI global references or directly accessing a mentation and our baseline Android build included a change reclaimable array’s memory through JNI. to the Android framework to increase a hard-coded cap on Our implementation of object access interposition in the the number of concurrently running apps. MRT compiler is unoptimized, and the per-object-access over- Our experiments used a mix of synthetic apps for bench- head of compiled code could be reduced with deeper compiler marking and real-world apps. We built several synthetic work- integration. We modified the ARM64 assembler, which trans- loads that simulate various memory footprints and working set lates intermediate representation (IR) instructions to ARM64 sizes to measure their effect on Marvin compared to Android.

## 三、核心发现与关键数据
other operating systems, mo- more complex [28], far outpacing increases in mobile de- bile OSes run all of their apps in a common language runtime. This trend has increased memory pressure For example, all apps running on Android must run in the on mobile operating systems as apps compete for limited Android Runtime (ART). This difference lets us co-design the space. Going forward, mobile OSes must more efficiently language runtime to assist the mobile OS in optimizing mem- share memory across demanding apps, or user experience ory management instead of hindering it. Due to its knowledge will suffer. of memory usage, the language runtime becomes an ideal Unfortunately, while mobile apps have become more so- place for mechanisms that can better manage memory.

关键数值线索：2x、60x、1.4GB、512MB

## 四、理论贡献与实践意义
该文属于“ART执行引擎与JIT策略”方向，对执行引擎优化与实验论证链条提供直接参考。可用于你的论文中：相关工作、方法依据、结果解释、威胁与有效性分析。

## 五、根本矛盾、切入视角、方法创新
- 根本矛盾：性能收益与系统开销/稳定性之间的冲突。
- 切入视角：将问题机制化并通过实验闭环验证。
- 方法创新：把优化目标、实现路径和评测证据统一在同一研究框架下。
