# Thesis Structure Reorg Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将论文主线重排为“移植 -> 优化机制 -> 实验评估”，清除正文中的元话语、防御性写作和“材料筛选说明书”式叙述。

**Architecture:** 保留第 1-3 章总体定位不变，删除现有“筛选章”作为独立叙述层，将其可保留内容改写为新第 4 章“总体优化思路”的引子；从 `Chap_Cases.tex` 和 `Chap_SIMD.tex` 中抽出“问题定义、机制、实现边界”形成新机制章，再把“正式结果、重复测量、统一比较”并入新实验章。实验章只承担实验环境、正确性验证、评测方法和结果分析，不再解释“为何进正文、为何下沉附录、为何作为核心结论”。

**Tech Stack:** LaTeX、BibTeX、ArtraX 模板、`./artratex.sh xa Thesis.tex`

---

### Task 1: 固定新章节骨架与迁移边界

**Files:**
- Modify: `Tex/Mainmatter.tex`
- Create: `Tex/Chap_Optimization.tex`
- Create: `Tex/Chap_Evaluation.tex`
- Reference: `Tex/Chap_Verification.tex`
- Reference: `Tex/Chap_Selection.tex`
- Reference: `Tex/Chap_Cases.tex`
- Reference: `Tex/Chap_SIMD.tex`

- [ ] **Step 1: 将主文档章节顺序改为六章结构**

目标顺序：

```tex
\input{Tex/Chap_Intro}
\input{Tex/Chap_Related}
\input{Tex/Chap_Porting}
\input{Tex/Chap_Optimization}
\input{Tex/Chap_Evaluation}
\input{Tex/Chap_Conclusion}
```

- [ ] **Step 2: 明确旧内容到新章节的迁移规则**

迁移规则：

```text
Chap_Verification:
  保留 -> 实验环境 / 正确性验证 / benchmark 与指标 / 有效性威胁
  删除或重写 -> 准入规则 / 正文角色 / 快照用途解释 / “进入正文资格”

Chap_Selection:
  保留 -> 四类问题对象、主路径与成本类型映射
  删除或重写 -> 筛选框架 / 准入标准 / 角色分配 / 避免开发日志

Chap_Cases:
  机制章保留 -> 三个案例的问题定义、技术机理、实现边界、最小相关回归
  实验章保留 -> 三个案例的正式结果与边界分析
  删除或重写 -> “为何分开讨论”“为何核心结论转向”

Chap_SIMD:
  机制章保留 -> 向量化问题定义、最小 LSX 路径、IR 到 LSX lowering、实现边界
  实验章保留 -> 正式结果、重复测量、与完整 SIMD 边界比较、统一比较、叠加效应
  删除或重写 -> “核心结论”“正文正式方案”“为何作为全文核心结论”等元表述
```

- [ ] **Step 3: 约束写作原则，避免补丁式修辞替换**

执行规则：

```text
1. 不保留“正文/附录/核心结论/降级/准入/资格/为何这样安排章节”这类作者视角句式。
2. 机制章只回答“问题是什么、为什么出现、怎么实现、边界在哪里”。
3. 实验章只回答“怎么测、测到了什么、如何解释结果与边界”。
4. 附录引用仅用“详见附录 A.x”，不说明其“被放入附录的原因”。
```

### Task 2: 重写机制章

**Files:**
- Create: `Tex/Chap_Optimization.tex`
- Reference: `Tex/Chap_Selection.tex`
- Reference: `Tex/Chap_Cases.tex`
- Reference: `Tex/Chap_SIMD.tex`

- [ ] **Step 1: 写第 4 章骨架**

目标结构：

```tex
\chapter{面向 LoongArch 架构的 ART 性能优化策略}
\section{总体优化思路}
\section{启发式 JIT 编译触发时机调优}
\section{运行时高频数据操作路径优化}
\section{基于 LSX 的规则浮点循环自动向量化}
\section{本章小结}
```

- [ ] **Step 2: 将 `Chap_Selection.tex` 改写为“总体优化思路”的素材来源**

保留信息：

```text
- 成本对象：控制流/JIT 时机、运行时热路径数据搬移、规则浮点数值内核向量化、启动期 DEX 校验
- 主路径判断：热点必须能映射到 workload 主导成本
- 研究目标：围绕控制流、数据流、启动期路径和后端向量化四类问题展开
```

删除信息：

```text
- 筛选框架、正文角色、准入标准、避免退化为开发日志
- “进入正文主线/正交案例/降级附录”的分类叙述
```

- [ ] **Step 3: 抽取案例章中的机制内容**

写入新章时保留：

```text
4.2 JIT 时机优化:
- 问题定义
- 分层 JIT 阈值机理
- 仅调整 warmup_threshold 的实现边界
- JIT 相关最小回归

4.3 运行时路径优化:
- 字符串热路径批量搬移问题定义
- 8 路批量搬移的核心循环
- length < 8 边界修复
- DexFileVerifier 四阶段机制、主调用链、关键钩子

4.4 LSX 向量化:
- 规则浮点循环问题定义
- 最小可用 LSX 路径边界
- Loop Vectorization -> LSX Lowering 关键链路
- 实现边界与保守启用策略
```

- [ ] **Step 4: 移除所有作者视角标题**

必须删除或重命名：

```text
“问题来源与正文角色”
“为何将其与核心结论分开讨论”
“局部案例的共同规律与核心结论路标”
“为何核心结论转向最小可用 LSX 路径”
“核心结论与综合讨论”
```

### Task 3: 重写实验章

**Files:**
- Create: `Tex/Chap_Evaluation.tex`
- Reference: `Tex/Chap_Verification.tex`
- Reference: `Tex/Chap_Cases.tex`
- Reference: `Tex/Chap_SIMD.tex`

- [ ] **Step 1: 写第 5 章骨架**

目标结构：

```tex
\chapter{实验评估与结果分析}
\section{实验环境与评估方法}
\section{基础移植正确性验证}
\section{局部优化策略评估}
\section{浮点循环自动向量化性能评估}
\section{综合性能对比与讨论}
\section{本章小结}
```

- [ ] **Step 2: 从 `Chap_Verification.tex` 只保留方法论和正确性验证**

保留信息：

```text
- 实验平台、硬件、Android 版本、debug JIT 设置
- 编译/部署/回归/benchmark 的实验流程
- run-test、libcore、最小相关回归
- benchmark 集、指标方向、speedup 计算公式
- 有效性威胁
```

删除或重写：

```text
- 准入规则
- 正文实验快照命名与归档映射
- “在本文中的角色”
- “进入正式图表的资格”
```

- [ ] **Step 3: 将结果数据归并到实验章**

结果来源：

```text
5.3 局部优化策略评估:
- JIT 时机优化的正式结果与波动分析
- 字符串热路径优化的正式结果与边界分析
- DexFileVerifier 阶段结果与机制解释

5.4 浮点循环自动向量化性能评估:
- 方案三正式对比结果
- lu.small 重复测量稳定性
- 与完整 SIMD 候选版边界比较

5.5 综合性能对比与讨论:
- 三项正式方案统一比较
- 叠加效应与不可简单组合的结论
```

- [ ] **Step 4: 统一结果叙述口径**

统一改写：

```text
- 不写“该方案构成全文核心结论”
- 不写“正文正式方案/候选增强版/降级附录”
- 改为“在当前实验设置下”“对该类工作负载表现为”“说明其适用范围”
```

### Task 4: 修订绪论、结论与附录衔接

**Files:**
- Modify: `Tex/Chap_Intro.tex`
- Modify: `Tex/Chap_Conclusion.tex`
- Modify: `Tex/Appendix.tex`

- [ ] **Step 1: 更新绪论中的研究内容与论文组织结构**

目标：

```text
- 全文共六章，不再写七章结构
- 研究内容改成“移植、机制设计、实验评估”三层
- 删除 Snapshot-A~E 作为研究内容主体的写法
```

- [ ] **Step 2: 更新结论中的贡献表述**

目标：

```text
- 删除“优化筛选机制”贡献点
- 保留移植贡献、实验验证贡献、三类优化机制贡献、LSX SIMD 核心性能结论
- 用客观术语总结适用边界，不再强调“核心结论/正文主线”
```

- [ ] **Step 3: 清理附录中的元话语**

处理原则：

```text
- 删去“未进入正文主线的原因”“为何列入附录”“作为辅助对照”
- 改写为“补充对比结果”“扩展实验结果”“边界分析”
- 检查重复节与标签冲突
```

### Task 5: 编译验证与残留元话语清理

**Files:**
- Modify: `Tex/*.tex`
- Verify: `Thesis.tex`

- [ ] **Step 1: 全局搜索残留元话语**

运行：

```bash
rg -n '正文|核心结论|附录|准入|资格|降级|为何|开发日志|流水账|退化为' Tex/Chap_*.tex Tex/Appendix.tex
```

预期：

```text
仅保留必要的附录引用与客观术语，不再出现作者视角的结构说明。
```

- [ ] **Step 2: 编译全文**

运行：

```bash
./artratex.sh xa Thesis.tex
```

预期：

```text
Thesis.tex 成功编译，目录、交叉引用、图表编号和文献引用无阻断性错误。
```

- [ ] **Step 3: 人工检查最终验收点**

检查清单：

```text
1. 第 4 章只讲机制，不贴主结果导向的结论性语言。
2. 第 5 章只讲实验与结果，不解释“为何写成这样”。
3. 绪论和结论中的章节描述与正文一致。
4. 附录只承担补充证据，不再自我辩护。
5. 用词用语规范，避免欧化、空泛连接词和防御性句式。
```
