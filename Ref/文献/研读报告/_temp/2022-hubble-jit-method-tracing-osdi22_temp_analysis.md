# 2022-hubble-jit-method-tracing-osdi22 临时分析（Step2）

## Step1 提取确认
- 已使用 `pdftotext -layout` 提取全文：`/workspace/ucasthesis/Ref/文献/研读报告/_text/2022-hubble-jit-method-tracing-osdi22.txt`
- 提取覆盖范围：从论文首页到参考文献（按文本文件完整输出）

## 一、研究问题、假设与目标
experience an intermittent performance problem, they quickly assume that their device is at fault, simply because they could Hubble is a method-tracing system shipped on all supported not immediately reproduce the issue on another device. How- and upcoming Android devices manufactured by Huawei, in ever, the root cause could be in the application itself, only order to aid in debugging performance problems. Hubble in- triggered under specific conditions or inputs. To combat these struments every non-inlined bytecode method’s entry and exit assumptions, device vendors are forced to devote ample engi- to record the method’s name and a timestamp. Instead of per- neering and support resources to these issues.

## 二、方法论与数据来源
July 11–13, 2022 • Carlsbad, CA, USA 978-1-939133-28-1 Open access to the Proceedings of the 16th USENIX Symposium on Operating Systems Design and Implementation is sponsored by Hubble: Performance Debugging with In-Production, Just-In-Time Method Tracing on Android Yu Luo Kirk Rodrigues Cuiqin Li University of Toronto University of Toronto Huawei Technologies Co., Ltd. Feng Zhang Lijin Jiang Bing Xia Huawei Technologies Co., Ltd. Huawei Technologies Co., Ltd. Huawei Technologies Co., Ltd. David Lion Ding Yuan University of Toronto University of Toronto Abstract experience an intermittent performance problem, they quickly assume that their device is at fault, simply because they could Hubble is a method-tracing system shipped on all supported not immediately reproduce the issue on another device. How- and upcoming Android devices manufactured by Huawei, in ever, the root cause could be in the application itself, only order to aid in debugging performance problems.

## 三、核心发现与关键数据
divided by two, since each method call contains effects on the cache. MM is a classic workload that can either a method-entry and method-exit trace point. To ensure the benefit heavily from caching or suffer ample cache misses [8]. method is compiled by the JIT compiler before evaluation, we When multiplying large matrices, a naïve implementation 798 16th USENIX Symposium on Operating Systems Design and Implementation USENIX Association Time Per Element (μs) 300 250 Trace On Mean 1400 1400 8% Startup Time (ms) Tracing Overhead 200 Baseline Mean 1200 1200 6% 150 Trace Off Mean 1000 1000 4% 100 800 800 2% 600 600 0% 50 400 400 -2% 0 200 200 -4% 6 2 64 28 56 12 24 48 x1 x3 x x1 x2 x5 10 20 Of Donald Beaver, [59] Xu Zhao, Kirk Rodrigues, Yu Luo, Michael Stumm, Saul Jaspan, and Chandan Shanbhag. Dapper, a Large- Ding Yuan, and Yuanyuan Zhou. Log20: Fully Au- Scale Distributed Systems Tracing Infrastructure.

关键数值线索：8%、6%、4%、2%、0%

## 四、理论贡献与实践意义
该文属于“ART执行引擎与JIT策略”方向，对执行引擎优化与实验论证链条提供直接参考。可用于你的论文中：相关工作、方法依据、结果解释、威胁与有效性分析。

## 五、根本矛盾、切入视角、方法创新
- 根本矛盾：性能收益与系统开销/稳定性之间的冲突。
- 切入视角：将问题机制化并通过实验闭环验证。
- 方法创新：把优化目标、实现路径和评测证据统一在同一研究框架下。
