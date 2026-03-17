# 2008-analysis-reduction-memory-inefficiencies-java-strings-oopsla 临时分析（Step2）

## Step1 提取确认
- 已使用 `pdftotext -layout` 提取全文：`/workspace/ucasthesis/Ref/文献/研读报告/_text/2008-analysis-reduction-memory-inefficiencies-java-strings-oopsla.txt`
- 提取覆盖范围：从论文首页到参考文献（按文本文件完整输出）

## 一、研究问题、假设与目标
eparation causes an unnecessary overhead. string handling at the language level [8]. However, all string Each string method must access both objects, which leads operations are compiled to normal method calls of the classes to a bad cache behavior and reduces the execution speed. String and StringBuilder in the Java bytecodes [11]. We propose to merge the character array with the string’s To the best of our knowledge, strings in Sun Microsystem’s metadata object at run time.

## 二、方法论与数据来源
, is compiled to a new bytecode for string alloca- ject, the bytecode new is used as illustrated in Figure 6 (b). tion by the modified javac. The details of this bytecode are This bytecode can only be used if an object with a statically explained below. known size is to be allocated, which applies to all Java ob- Figure 6 (a) presents a simple Java method. The method jects except arrays. The only operand is an index to a class allocates and returns an optimized string object that is ini- in the constant pool.

## 三、核心发现与关键数据
thermore, the field offset is an overhead that reduces the performance: when a string character is accessed, offset is Categories and Subject Descriptors loaded to determine the start of the string within the array. D.3.4 [Programming Languages]: Processors—Compil- ers, Optimization, Code generation String char[] 8 count: int 8 length: int General Terms 12 offset: int 12 char[0] 16 hashcode: int ... Languages, Performance 20 value: char[] char[length-1] Keywords (a) original Java, string, optimization, performance String String 8 count: int 8 count: int 12 hashcode: int 12 char[0] 16 char[0] ... This is the author’s version of the work. char[count-1] here by permission of ACM for your personal use. Not for redistribution.

关键数值线索：未在自动抽取中识别到稳定格式数值，请在原文结果章节核对。

## 四、理论贡献与实践意义
该文属于“字符串热路径与解释器性能”方向，对执行引擎优化与实验论证链条提供直接参考。可用于你的论文中：相关工作、方法依据、结果解释、威胁与有效性分析。

## 五、根本矛盾、切入视角、方法创新
- 根本矛盾：性能收益与系统开销/稳定性之间的冲突。
- 切入视角：将问题机制化并通过实验闭环验证。
- 方法创新：把优化目标、实现路径和评测证据统一在同一研究框架下。
