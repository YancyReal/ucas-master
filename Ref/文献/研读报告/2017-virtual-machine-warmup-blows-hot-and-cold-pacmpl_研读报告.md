# Virtual Machine Warmup Blows Hot and Cold 双模式研读报告

---

## Part A: 深度专业学术速读报告

## 结构化摘要 (Structured Abstract)

| 维度 | 内容 |
|---|---|
| **背景/目标** | 论文挑战 JVM 基准研究中的默认前提：benchmark 会快速进入“稳定且峰值”的稳态（steady state of peak performance）。作者要验证该前提是否在严格控制实验中仍成立。 |
| **方法** | 设计可重复实验框架 Krun，在高度受控环境下运行 2000 次 in-process iteration、30 次 process execution；使用 changepoint analysis 自动检测性能阶段变化并分类 warmup/flat/slowdown/no steady state。 |
| **结果** | 关键发现是：在最受控条件下，许多常用微基准仍无法稳定达到峰值稳态。文中报告 3 台机器上“稳定达到峰值稳态”的 ⟨VM,benchmark⟩ 对最多仅 43.5%；并指出有些场景 warmup 差异可达 100–1000x。 |
| **结论** | 传统“丢掉前几轮后只报稳态均值”的方法存在系统性风险。论文建议必须报告分类、达到稳态所需迭代、以及稳态性能区间，而不是只给单一 steady-state 数字。 |

---

## 1. 引言 (Introduction)

### 1.1. 研究背景与核心问题 (Research Background & Problem Statement)

JIT 运行时通常被描述为“两阶段”：先 warmup，再进入峰值稳态。几乎所有 VM 评测方法都默认这一点并丢弃前几轮数据。作者提出的核心问题是：这个前提到底是事实，还是习惯性假设？如果假设不成立，许多已有 VM 结论可能被系统性扭曲。

### 1.2. 文献综述与研究缺口 (Literature Review & Research Gap)

论文肯定了 Georges 等与 Kalibera/Jones 等工作对基准方法学的推进，但指出现有方法仍存在两类缺口：第一，很多流程仍依赖人工判定“何时 warmup 结束”；第二，即使找到稳态，也很少判断该稳态是否真是峰值。换言之，研究社区对“稳态质量”缺少自动化、可重复、可规模化的判别机制。

### 1.3. 研究目标与核心假设/命题 (Objectives & Hypotheses/Propositions)

论文以可证伪方式提出假设 H1（小型确定性程序会达到峰值稳态）和 H2（中等硬件/OS 差异影响较小），再通过系统实验检验。其目标不是给某个 VM 贴标签，而是验证评测前提本身是否可靠。

---

## 2. 研究设计与方法 (Methodology)

### 2.1. 研究范式与方法论 (Research Paradigm & Methodology)

研究采用“实验基础设施 + 统计分类算法”双层方法。基础设施是 Krun（重启、温控、频率/调度控制、环境隔离、自动采集）；算法层使用 changepoint analysis 自动分段时间序列，并对每次执行做行为分类。

### 2.2. 数据来源与样本 (Data Source & Sample)

主实验覆盖 7 类语言运行时与多类微基准，核心数据规模是 3660 次 process execution、7,320,000 次 in-process iteration。补充实验还把方法应用到 DaCapo/Octane，证明该分析流程并不限于微基准。

### 2.3. 操作化与测量 (Operationalization & Measurement)

关键操作化非常清晰：

- 单次执行分类为 `flat`、`warmup`、`slowdown`、`no steady state`；
- 组合级别再分类为一致或不一致（含 good/bad inconsistency）；
- 稳态性能用 bootstrap 计算 99% CI（100,000 次重采样）；
- 默认稳态判断窗口与尾段长度参数显式公开，便于复现。

---

## 3. 结果与发现 (Results & Findings)

### 3.1. 主要发现概述 (Overview of Key Findings)

论文最冲击性的结果是“稳态神话”并不稳。文中给出：在 3 台机器上，最多仅 43.5% 的 ⟨VM,benchmark⟩ 对能一致达到峰值稳态；很多组合出现 slowdown 或 no steady state。即使同一 ⟨VM,benchmark⟩，不同 process execution 的轨迹也可能显著不同。

此外，作者指出实际实验中可出现“warmup 成本差异 100–1000x”，而这部分恰恰常被传统方法直接丢弃。若只报告 steady-state 单值，会把对用户真实体验很重要的信息抹平。

### 3.2. 关键数据与图表解读 (Interpretation of Key Data & Figures)

Figure 1 展示典型 warmup 与 slowdown；Figure 2/Table 结果给出不同分类占比；Figure 9/11 进一步分析“若减少迭代或进程次数，结论会偏离多少”。论文据此给出实操建议：不少场景 5 或 10 次迭代远不足以支撑稳健结论。

---

## 4. 讨论 (Discussion)

### 4.1. 结果的深度解读 (In-depth Interpretation of Results)

这篇论文改变的是“报告语义”而不只是“分析工具”。它告诉我们：即便统计上有稳态，也要问“这个稳态是不是峰值”“是否一致出现”“达到它要多长时间”。这些问题与你当前 ART 优化实验高度相关，尤其是短 workload 对 warmup 极端敏感的场景。

### 4.2. 理论贡献 (Theoretical Contributions)

理论贡献在于把 warmup 从经验概念提升为可操作分类体系，并提供自动化判别流程。它把“是否可比”变成可计算问题，为 VM/JIT 评测建立了更严格的因果边界。

### 4.3. 实践启示 (Practical Implications)

对你的论文，建议直接落地为实验规范：

1. 对每个 benchmark 报告 warmup 分类，而非只报最终分数；  
2. 明确“达到稳态所需迭代/时间”；  
3. 为波动项增加 process execution 次数，不用固定 1 次或 3 次；  
4. 对短负载单独讨论“warmup 成本是否盖过优化收益”。  

### 4.4. 局限性与未来研究 (Limitations & Future Research)

论文主要用微基准验证方法，外推到大型应用需谨慎；但作者附录已证明方法可迁移到 DaCapo/Octane。你可以在此基础上将同样流程迁移到 DaCapo pmd 与 SPEC mpegaudio 的 LoongArch 实验中，形成“分类+统计”双证据链。

---

## 5. 结论 (Conclusion)

该文的核心结论是：JVM 基准并不天然“先热后稳”，也不必然“稳即峰值”。因此，严谨评测必须同时描述行为分类、稳态到达成本与稳态性能区间。它是你论文中“实验有效性与统计方法”章节的关键支撑文献。

---

## 6. 核心参考文献 (Core References)

1. Barrett, E., Bolz-Tereick, C., Killick, R., Mount, S., Tratt, L. Virtual Machine Warmup Blows Hot and Cold. PACMPL/OOPSLA 2017.
2. Georges, A., et al. Statistically Rigorous Java Performance Evaluation. OOPSLA 2007.
3. Kalibera, T., Jones, R. Rigorous Benchmarking in Reasonable Time. ISMM 2013.
4. DaCapo benchmark suite.
5. Octane benchmark suite.

---

## Part B: 核心逻辑链与根本价值提炼

## 核心四要素

| 要素 | 内容 |
|---|---|
| **根本问题** | “丢前几轮、报稳态”这个行业惯例可能在大量场景下不成立。 |
| **切入视角** | 不靠人工目测 warmup 曲线，而是用 changepoint 自动分段并分类行为。 |
| **关键方法** | Krun 受控实验 + 2000×30 长序列采样 + 分类规则（warmup/flat/slowdown/no steady state）+ bootstrap CI。 |
| **核心发现** | 很多组合达不到稳定峰值；即使达到了，不同执行之间也不一致。传统方法因此可能部分或整体误导。 |

---

## 方法公式化

`可置信VM评测 = 受控实验环境 × 自动阶段分类 × 稳态到达成本 + 稳态性能区间`

---

## 最终双重总结

**一句话总结（核心价值）**：该论文证明了 VM 评测不能再把 warmup 当噪声丢弃，而必须把 warmup 行为本身作为一等研究对象。  

**一句话总结（大白话版）**：先热身再稳定这件事，很多程序根本没按剧本来。
