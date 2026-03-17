# 2017-artist-android-runtime-instrumentation-arxiv 临时分析（Step2）

## Step1 提取确认
- 已使用 `pdftotext -layout` 提取全文：`/workspace/ucasthesis/Ref/文献/研读报告/_text/2017-artist-android-runtime-instrumentation-arxiv.txt`
- 提取覆盖范围：从论文首页到参考文献（按文本文件完整输出）

## 一、研究问题、假设与目标
In this paper, we present a compiler- We present ARTist, a compiler-based application instru- based solution that can not only be used to study the feasi- mentation solution for Android. ARTist is based on the bility of re-instantiating previous solutions such as dynamic, new ART runtime and the on-device dex2oat compiler of intra-application taint tracking and dynamic permission en- Android, which replaced the interpreter-based managed run- forcement, but, moreover, provides a more robust, reliable, time (DVM) from Android version 5 onwards. Since dex2oat and integrated application-layer instrumentation approach is yet uncharted, our approach required first and foremost than previously possible. Concretely, we make the following a thorough study of the compiler suite’s internals and in contributions in this paper. particular of the new default compiler backend Optimizing.

## 二、方法论与数据来源
Section 5 illustrates use cases for ARTist, followed by a more detailed case study on compiler-assisted taint tracking. We discuss limitations and future work of our Figure 1: A high-level overview of the dex2oat compiler us- ing Optimizing backend including the transformation to the IR, solution in Section 6 and conclude this paper in Section 7. optimizations, and native code generation. BACKGROUND ON ART AND DEX2OAT as the 65k method limit1 . In particular, Google made the We provide general background information on Android’s Optimizing compiler backend, which was introduced as opt-in managed runtime to set the context of our compiler ex- feature in Android 5, the default backend in Android 6. In tensions (Section 2.1), and afterwards present technical the following Sections 2.2 and 2.3, we will elaborate in more background information on the compiler suite dex2oat (Sec- technical details on this new compiler suite and in particular tion 2.2) and in particular on its Optimizing backend (Sec- on the Optimizing backend.

## 三、核心发现与关键数据
provide compelling arguments for preferring compiler- only allow us to implement compiler-based security solutions, based instrumentation over alternative bytecode or binary but also form expert knowledge that facilitates independent rewriting approaches. research on the topic. Compiler-based app instrumentation. We design and imple- ment a novel approach, called ARTist (ART Instrumentation and Security Toolkit), for application instrumentation based on an extended version of ART’s on-device compiler dex2oat. INTRODUCTION Our system leverages the compiler’s rich optimization frame- Google’s Android OS has become a popular subject of the work to safely optimize the newly instrumented application security research community over the last few years. The instrumentation process is guided by static analy- the different directions of research on improving Android’s sis that utilizes the compiler’s intermediate representation security, a dedicated line of work has successfully investigated of the app’s code as well as its static program information how instrumentation of the interpreter (i.e., Dalvik virtual in order to efficiently determine instrumentation targets.

关键数值线索：未在自动抽取中识别到稳定格式数值，请在原文结果章节核对。

## 四、理论贡献与实践意义
该文属于“ART执行引擎与JIT策略”方向，对执行引擎优化与实验论证链条提供直接参考。可用于你的论文中：相关工作、方法依据、结果解释、威胁与有效性分析。

## 五、根本矛盾、切入视角、方法创新
- 根本矛盾：性能收益与系统开销/稳定性之间的冲突。
- 切入视角：将问题机制化并通过实验闭环验证。
- 方法创新：把优化目标、实现路径和评测证据统一在同一研究框架下。
