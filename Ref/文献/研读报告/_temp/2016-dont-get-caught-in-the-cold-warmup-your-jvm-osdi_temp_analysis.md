# 2016-dont-get-caught-in-the-cold-warmup-your-jvm-osdi 临时分析（Step2）

## Step1 提取确认
- 已使用 `pdftotext -layout` 提取全文：`/workspace/ucasthesis/Ref/文献/研读报告/_text/2016-dont-get-caught-in-the-cold-warmup-your-jvm-osdi.txt`
- 提取覆盖范围：从论文首页到参考文献（按文本文件完整输出）

## 一、研究问题、假设与目标
SQL [10, 64, 65], Hive on Tez [37], and Impala [36]. Many widely used, latency sensitive, data-parallel dis- Numerous improvements have been made to the per- tributed systems, such as HDFS, Hive, and Spark choose formance of these systems. These works mostly fo- to use the Java Virtual Machine (JVM), despite debate cused on scheduling [2, 4, 31, 38, 56, 84], shuffling on the overhead of doing so. This paper analyzes the ex- overhead [17, 19, 40, 45, 81], and removing redundant tent and causes of the JVM performance overhead in the computations [61]. Performance characteristics stud- above mentioned systems.

## 二、方法论与数据来源
and Implementation is sponsored by USENIX. Don’t Get Caught In the Cold, Warm-up Your JVM Understand and Eliminate JVM Warm-up Overhead in Data-parallel Systems David Lion, Adrian Chiu, Hailong Sun*, Xin Zhuang, Nikola Grcevski†, Ding Yuan University of Toronto, *Beihang University, †Vena Solutions Abstract SQL [10, 64, 65], Hive on Tez [37], and Impala [36]. Many widely used, latency sensitive, data-parallel dis- Numerous improvements have been made to the per- tributed systems, such as HDFS, Hive, and Spark choose formance of these systems. These works mostly fo- to use the Java Virtual Machine (JVM), despite debate cused on scheduling [2, 4, 31, 38, 56, 84], shuffling on the overhead of doing so. This paper analyzes the ex- overhead [17, 19, 40, 45, 81], and removing redundant tent and causes of the JVM performance overhead in the computations [61]. Performance characteristics stud- above mentioned systems.

## 三、核心发现与关键数据
overhead heavily depends 1 Introduction on the characteristics of the application. For example, whether an interpreted method is compiled to machine A large number of data-parallel distributed systems are instructions by the just-in-time (JIT) compiler depends built on the Java Virtual Machine (JVM) [25]. These sys- on how frequently it has been invoked. With all these dif- tems include distributed file systems such as HDFS [28], ferent perspectives, a clear understanding of the JVM’s data analytic platforms such as Hadoop [27], Spark [64], performance when running these systems is needed. Tez [62, 76], Hive [32, 77], Impala [13, 36], and key- This research asks a simple question: what is the per- value stores such as HBase [29] and Cassandra [15]. A formance overhead introduced by the JVM in latency- recent trend is to process latency-sensitive, interactive sensitive data-parallel systems?

关键数值线索：33%、36%、1.8X、21 seconds、29 seconds、1GB、100GB、1MB

## 四、理论贡献与实践意义
该文属于“基准测试方法学与统计规范”方向，对执行引擎优化与实验论证链条提供直接参考。可用于你的论文中：相关工作、方法依据、结果解释、威胁与有效性分析。

## 五、根本矛盾、切入视角、方法创新
- 根本矛盾：性能收益与系统开销/稳定性之间的冲突。
- 切入视角：将问题机制化并通过实验闭环验证。
- 方法创新：把优化目标、实现路径和评测证据统一在同一研究框架下。
