# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 仓库定位

这是一个基于 `ucasthesis` 模板维护的硕士论文源码仓库，不是实际实现代码仓库。当前论文主题聚焦 **AOSP 15 ART 在 LoongArch 平台上的适配、验证与优化**。

- 论文主入口：`Thesis.tex`
- 正文章节入口：`Tex/Mainmatter.tex`
- 前置部分：`Tex/Frontmatter.tex`、`Tex/Frontinfo.tex`、`Tex/Prematter.tex`
- 附录与后置部分：`Tex/Appendix.tex`、`Tex/Backmatter.tex`
- 参考文献：`Biblio/ref.bib`
- 图片资源：`Img/`
- 图生成脚本：`tools/`
- 编译输出目录：`Tmp/`

## 常用命令

### 编译主论文

优先使用仓库自带脚本：

```bash
./artratex.sh xa Thesis.tex
```

含义：

- `x` = `xelatex`
- `a` = `bibtex`

脚本会把编译产物输出到 `Tmp/`，并自动创建 `Tmp/Tex/` 层级。

### 其他编译方式

仅编译、不跑文献：

```bash
./artratex.sh x Thesis.tex
```

如果需要切换引擎，脚本支持：

```bash
./artratex.sh pa Thesis.tex   # pdflatex + bibtex
./artratex.sh la Thesis.tex   # lualatex + bibtex
```

### 重新生成论文插图

仓库中的部分图不是手工绘制，而是由 Python 脚本直接生成 SVG/PDF/PNG：

```bash
python3 tools/generate_porting_figures.py
python3 tools/generate_statistical_validation_figure.py
```

这些脚本依赖本机可执行的 `rsvg-convert`，当前脚本里使用的是：

```bash
/opt/homebrew/bin/rsvg-convert
```

### 选择性编译章节

`Thesis.tex` 里保留了 `\includeonly{...}` 注释位。若只想聚焦某些章节排版，可临时在 `Thesis.tex` 中启用 `\includeonly`，再运行完整编译命令。

### 验收标准

本仓库没有单元测试或 lint。对本仓库改动的主要验收方式是：

```bash
./artratex.sh xa Thesis.tex
```

确认：

- 能成功生成 PDF
- 目录、交叉引用、图片、公式编号正常
- 文献引用无明显错误

## 文档结构与大图景

### 1. 这是“总装入口 + 分章节内容”结构

`Thesis.tex` 只负责装配论文：

- 加载 `Style/ucasthesis` 文档类与 `Style/artratex` 配置
- `\input{Tex/Frontinfo}` 注入封面元信息
- 依次组织 frontmatter / mainmatter / appendix / backmatter
- 根据 `artratex` 的配置选择 `bibtex` 或 `biber` 处理参考文献

也就是说，**实际内容修改通常不在 `Thesis.tex`，而在 `Tex/` 下各个分文件中完成**。

### 2. 正文采用线性章节串联

`Tex/Mainmatter.tex` 按顺序串联正文：

- `Tex/Chap_Intro.tex`
- `Tex/Chap_Related.tex`
- `Tex/Chap_Porting.tex`
- `Tex/Chap_Verification.tex`
- `Tex/Chap_Selection.tex`
- `Tex/Chap_Cases.tex`
- `Tex/Chap_SIMD.tex`
- `Tex/Chap_Conclusion.tex`

这篇论文的论证主线是递进式的：

1. 研究背景与问题定义
2. 相关工作
3. **LoongArch 平台 ART 执行能力构建**
4. **实验设计与正确性验证**
5. 候选问题筛选
6. 代表性案例分析
7. **主结论：LoongArch64 最小可用 LSX 浮点 SIMD 路径**
8. 总结与展望

因此，跨章节修改时要注意论证链的一致性：第 3 章建立“能力闭环”，第 4 章建立“证据闭环”，第 7 章给出全文主结论。

### 3. 论文关注的是“执行能力构建 → 统一验证链 → 受约束的性能结论”

从现有章节内容看，仓库中的核心叙事不是泛泛而谈的移植记录，而是三层结构：

- **执行能力构建**：解释器、Nterp、JIT 后端、JNI、运行时入口点、Intrinsic 基础能力
- **统一验证链**：编译、部署、目标机 run-test、libcore、benchmark 的固定顺序
- **正式结论约束**：只有共享验证链、共享正式对比设置的数据，才能进入正文主结论

改动正文时应尽量保持这三个层次分离，不要把“实现细节”“实验流程”“正式结论”混写成操作手册。

### 4. 图片不是装饰，而是论证结构的一部分

`tools/generate_porting_figures.py` 和 `tools/generate_statistical_validation_figure.py` 表明，仓库中部分图片是程序化生成的，用于表达：

- ART 执行引擎适配范围
- 阶段化移植闭环
- 运行时路径协同
- 统计验证结果

如果用户要求修改这些图，优先检查对应 Python 生成脚本，而不是只替换导出的 PDF/PNG。

### 5. 外部代码与实验数据不在本仓库

根据仓库现有约束，论文涉及的真实实现代码和实验归档在外部目录，而不是本仓库：

- 实际代码：`/workspace/aosp/art`
- benchmark / 实验结果：`/workspace/aosp/tmp/MyBenchMark`

在当前机器上，这些路径对应远端主机 `la55:/home/yanxi/loongson/aosp15.la/...`。

**结论：**

- 本仓库负责论文写作、结构组织、图表与文献
- 不应把 `ucasthesis` 仓库误当成 AOSP/ART 源码仓库
- 若论文内容要核对实现细节、实验流程或结果来源，应先回到外部代码/数据目录核实

## 修改约束

- 优先修改 `Tex/*.tex`、`Biblio/ref.bib`、`tools/*.py`、图片源文件；不要手工编辑 `Tmp/` 下生成物。
- 新增章节时，沿用 `Tex/Chap_*.tex` 命名，并在 `Tex/Mainmatter.tex` 中接入。
- 若只是调整封面、摘要、致谢、作者简历等，通常应改 `Tex/Frontinfo.tex`、`Tex/Frontmatter.tex`、`Tex/Backmatter.tex`，而不是正文文件。
- 论文中的实现、benchmark、实验结论若涉及外部工程事实，先核对外部目录，再回写论文。
- 图表改动优先保持“白底 + 浅色分区 + 简洁箭头”的期刊风格，解释性结论放正文，不塞进图里。
