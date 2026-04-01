# 第4章总览图重画 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将第 4 章“正确性验证与性能评测的组织流程”从工程执行流样式重画为学术论文式两阶段总览图，并导出新的 PDF 供正文直接引用。

**Architecture:** 保留 [Tex/Chap_Verification.tex](Tex/Chap_Verification.tex) 中现有 `\includegraphics` 路径不变，只重写 [Img/verification/experiment-validation-workflow.svg](Img/verification/experiment-validation-workflow.svg) 的图形结构，再用 `rsvg-convert` 导出同名 PDF 覆盖正文引用版本。图面采用“第一阶段容器 + 约束带 + 第二阶段容器 + 结果层”的四层纵向结构，并以白底、浅色块、细黑线、圆角卡片统一视觉语言。

**Tech Stack:** SVG XML, `rsvg-convert`, `xmllint`, XeLaTeX/artratex

---

## File Map

- Modify: `Img/verification/experiment-validation-workflow.svg`
  - 责任：承载新的两阶段总览图结构、全部图内文案、颜色、箭头和层级。
- Modify: `Img/verification/experiment-validation-workflow.pdf`
  - 责任：由新的 SVG 导出，供 [Tex/Chap_Verification.tex](Tex/Chap_Verification.tex) 现有 `\includegraphics` 直接使用。
- Verify only: `Tex/Chap_Verification.tex`
  - 责任：确认引用路径仍为 `verification/experiment-validation-workflow.pdf`，本计划不改动正文。
- Temporary preview only: `/tmp/experiment-validation-workflow-preview.png`
  - 责任：用于本地快速检查 SVG 渲染结果，不纳入版本控制。

### Task 1: 重写画布骨架与四层分区

**Files:**
- Modify: `Img/verification/experiment-validation-workflow.svg`
- Verify: `Tex/Chap_Verification.tex`
- Preview: `/tmp/experiment-validation-workflow-preview.png`

- [ ] **Step 1: 确认正文引用路径保持不变**

Run:

```bash
rg -n "experiment-validation-workflow\\.pdf" Tex/Chap_Verification.tex
```

Expected:

```text
20:    \includegraphics[width=0.95\textwidth]{verification/experiment-validation-workflow.pdf}
```

- [ ] **Step 2: 把旧的单列流程骨架替换成四层纵向分区骨架**

将 [Img/verification/experiment-validation-workflow.svg](Img/verification/experiment-validation-workflow.svg) 顶部骨架替换为以下内容，先只落画布、样式、四个大分区和标题，不写内部卡片：

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="760" viewBox="0 0 1200 760">
  <defs>
    <marker id="arrow" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto" markerUnits="userSpaceOnUse">
      <path d="M0,0 L12,6 L0,12 z" fill="#4a4a4a"/>
    </marker>
    <style>
      .cn { font-family: "Songti SC", "STSong", "Noto Serif CJK SC", serif; fill: #2c2c2c; }
      .section-title { font-size: 28px; font-weight: 700; }
      .card-title { font-size: 22px; font-weight: 700; }
      .card-sub { font-size: 16px; fill: #575757; }
      .rule-main { font-size: 24px; font-weight: 700; fill: #7a5a00; }
      .rule-sub { font-size: 16px; fill: #7a5a00; }
      .tag { font-size: 16px; font-weight: 700; fill: #4b4b4b; }
      .panel { stroke: #222222; stroke-width: 1.6; }
      .card { fill: #ffffff; stroke: #222222; stroke-width: 1.4; }
      .connector { fill: none; stroke: #4a4a4a; stroke-width: 2; marker-end: url(#arrow); }
    </style>
  </defs>

  <rect x="0" y="0" width="1200" height="760" fill="#ffffff"/>

  <rect x="50" y="50" width="1100" height="250" rx="28" ry="28" fill="#dfeef2" class="panel"/>
  <text x="80" y="94" class="cn section-title">一致性构建与正确性闭环</text>

  <rect x="230" y="322" width="740" height="86" rx="18" ry="18" fill="#f5d8bf" class="panel"/>
  <text x="600" y="358" text-anchor="middle" class="cn rule-main">先正确性，后性能</text>
  <text x="600" y="384" text-anchor="middle" class="cn rule-sub">仅在正确性约束成立后进入性能评测</text>

  <rect x="50" y="430" width="1100" height="190" rx="28" ry="28" fill="#d9e4c2" class="panel"/>
  <text x="80" y="474" class="cn section-title">性能评测与证据组织</text>

  <rect x="210" y="650" width="780" height="76" rx="20" ry="20" fill="#ffffff" class="panel"/>
  <text x="600" y="682" text-anchor="middle" class="cn card-title">结果归档与分析证据</text>
  <text x="600" y="708" text-anchor="middle" class="cn card-sub">运行日志 / 性能数据 / 剖析报告 / 可视化分析结果</text>
</svg>
```

- [ ] **Step 3: 校验 SVG 语法无误**

Run:

```bash
xmllint --noout Img/verification/experiment-validation-workflow.svg
```

Expected:

```text
无输出，退出码为 0
```

- [ ] **Step 4: 生成第一版预览图检查整体层级**

Run:

```bash
rsvg-convert -o /tmp/experiment-validation-workflow-preview.png Img/verification/experiment-validation-workflow.svg
```

Expected:

```text
命令成功退出，并生成 /tmp/experiment-validation-workflow-preview.png
```

- [ ] **Step 5: 提交骨架阶段变更**

Run:

```bash
git add Img/verification/experiment-validation-workflow.svg
git commit -m "redesign verification workflow figure scaffold"
```

Expected:

```text
提交成功，输出首行包含新 commit SHA，标题为 "redesign verification workflow figure scaffold"
```

### Task 2: 落第一阶段卡片与阶段内连接

**Files:**
- Modify: `Img/verification/experiment-validation-workflow.svg`
- Preview: `/tmp/experiment-validation-workflow-preview.png`

- [ ] **Step 1: 在第一阶段容器内添加四张横向卡片**

在 `一致性构建与正确性闭环` 分区内加入以下卡片与文案：

```svg
  <rect x="85" y="128" width="230" height="124" rx="18" ry="18" class="card"/>
  <text x="200" y="168" text-anchor="middle" class="cn card-title">固定源码状态与实验基线</text>
  <text x="200" y="198" text-anchor="middle" class="cn card-sub">统一 LoongArch64 目标环境</text>

  <rect x="350" y="128" width="230" height="124" rx="18" ry="18" class="card"/>
  <text x="465" y="168" text-anchor="middle" class="cn card-title">完整构建 ART 实验产物</text>
  <text x="465" y="198" text-anchor="middle" class="cn card-sub">保持产物与源码状态一致</text>

  <rect x="615" y="128" width="230" height="124" rx="18" ry="18" class="card"/>
  <text x="730" y="168" text-anchor="middle" class="cn card-title">一致性部署到目标设备</text>
  <text x="730" y="198" text-anchor="middle" class="cn card-sub">统一部署顺序与运行条件</text>

  <rect x="880" y="128" width="235" height="124" rx="18" ry="18" class="card"/>
  <text x="997.5" y="164" text-anchor="middle" class="cn card-title">分层正确性验证</text>
  <text x="997.5" y="194" text-anchor="middle" class="cn card-sub">宿主机侧测试 / 目标机 run-test</text>
  <text x="997.5" y="218" text-anchor="middle" class="cn card-sub">/ libcore 测试</text>
```

- [ ] **Step 2: 为第一阶段卡片补齐横向连接和进入约束带的纵向连接**

在同一文件中加入以下连接线，替换旧图的编号圆点和单列箭头：

```svg
  <path d="M315 190 L350 190" class="connector"/>
  <path d="M580 190 L615 190" class="connector"/>
  <path d="M845 190 L880 190" class="connector"/>
  <path d="M600 300 L600 322" class="connector"/>
```

- [ ] **Step 3: 再次渲染预览并确认第一阶段卡片在 1200px 宽度下不拥挤**

Run:

```bash
rsvg-convert -o /tmp/experiment-validation-workflow-preview.png Img/verification/experiment-validation-workflow.svg
identify -format '%wx%h\n' /tmp/experiment-validation-workflow-preview.png
```

Expected:

```text
1200x760
```

- [ ] **Step 4: 用正文术语人工复核第一阶段文案**

Run:

```bash
rg -n "正确性验证|目标机 run-test|libcore|实验基线|目标设备" Tex/Chap_Verification.tex Img/verification/experiment-validation-workflow.svg
```

Expected:

```text
输出同时覆盖正文与 SVG 中的对应术语，且不再出现日期、目录名、命令行
```

- [ ] **Step 5: 提交第一阶段卡片变更**

Run:

```bash
git add Img/verification/experiment-validation-workflow.svg
git commit -m "add stage one cards to verification workflow figure"
```

Expected:

```text
提交成功，输出首行包含新 commit SHA，标题为 "add stage one cards to verification workflow figure"
```

### Task 3: 落第二阶段卡片、结果层衔接与学术化快照文案

**Files:**
- Modify: `Img/verification/experiment-validation-workflow.svg`
- Preview: `/tmp/experiment-validation-workflow-preview.png`

- [ ] **Step 1: 在第二阶段容器内加入基准测试评测与两类快照卡片**

在 `性能评测与证据组织` 分区内加入以下卡片：

```svg
  <rect x="110" y="506" width="255" height="88" rx="18" ry="18" class="card"/>
  <text x="237.5" y="542" text-anchor="middle" class="cn card-title">基准测试评测</text>
  <text x="237.5" y="570" text-anchor="middle" class="cn card-sub">DaCapo / SPECjvm2008</text>

  <rect x="445" y="506" width="255" height="88" rx="18" ry="18" class="card"/>
  <text x="572.5" y="538" text-anchor="middle" class="cn card-title">正式对比快照</text>
  <text x="572.5" y="564" text-anchor="middle" class="cn tag">Snapshot-A</text>

  <rect x="780" y="506" width="255" height="88" rx="18" ry="18" class="card"/>
  <text x="907.5" y="538" text-anchor="middle" class="cn card-title">统计验证快照</text>
  <text x="907.5" y="564" text-anchor="middle" class="cn tag">Snapshot-B</text>
```

- [ ] **Step 2: 用“基准测试评测”分别连接两类快照，并让第二阶段汇入结果层**

在同一文件中加入第二阶段的连接线：

```svg
  <path d="M365 538 L445 538" class="connector"/>
  <polyline points="365,562 392,562 392,612 760,612 760,562 780,562" class="connector"/>
  <path d="M600 408 L600 430" class="connector"/>
  <path d="M600 620 L600 650" class="connector"/>
```

- [ ] **Step 3: 删除旧图中所有不学术的现场信息**

在 [Img/verification/experiment-validation-workflow.svg](Img/verification/experiment-validation-workflow.svg) 中确认以下字符串不再存在：

```text
2026-03-13
2026-03-14
final-comparison/
statistical-validation-20260314/
buildbot-build.sh --target
```

Run:

```bash
rg -n "2026-03|final-comparison/|statistical-validation|buildbot-build\\.sh" Img/verification/experiment-validation-workflow.svg || true
```

Expected:

```text
无输出
```

- [ ] **Step 4: 渲染预览并人工确认“章节总览图”气质已经成立**

Run:

```bash
rsvg-convert -o /tmp/experiment-validation-workflow-preview.png Img/verification/experiment-validation-workflow.svg
```

Expected:

```text
命令成功退出；预览图中呈现“阶段容器 + 约束带 + 证据组织 + 结果层”的四层结构
```

- [ ] **Step 5: 提交第二阶段与清理后的最终 SVG**

Run:

```bash
git add Img/verification/experiment-validation-workflow.svg
git commit -m "finish academic redesign of verification workflow figure"
```

Expected:

```text
提交成功，输出首行包含新 commit SHA，标题为 "finish academic redesign of verification workflow figure"
```

### Task 4: 导出 PDF、检查版心可读性并完成论文编译验证

**Files:**
- Modify: `Img/verification/experiment-validation-workflow.pdf`
- Modify: `Img/verification/experiment-validation-workflow.svg`
- Verify: `Tex/Chap_Verification.tex`

- [ ] **Step 1: 从新的 SVG 导出正文引用用的同名 PDF**

Run:

```bash
rsvg-convert -f pdf -o Img/verification/experiment-validation-workflow.pdf Img/verification/experiment-validation-workflow.svg
pdfinfo Img/verification/experiment-validation-workflow.pdf | sed -n '1,12p'
```

Expected:

```text
Pages:           1
Page size:       900 x 570 pts
```

- [ ] **Step 2: 再生成一份缩放预览，检查 0.95\textwidth 下的文字密度**

Run:

```bash
rsvg-convert -w 950 -o /tmp/experiment-validation-workflow-950w.png Img/verification/experiment-validation-workflow.svg
identify -format '%wx%h\n' /tmp/experiment-validation-workflow-950w.png
```

Expected:

```text
950x602
```

- [ ] **Step 3: 用仓库标准命令编译整篇论文**

Run:

```bash
./artratex.sh xa Thesis.tex
```

Expected:

```text
命令成功退出，并重新生成 Thesis.pdf / Tmp 下对应产物；编译过程中不出现该图相关的 includegraphics 错误
```

- [ ] **Step 4: 只检查与目标图直接相关的编译结果**

Run:

```bash
rg -n "experiment-validation-workflow|includegraphics|not found|Error" Thesis.log Tmp/Thesis.log 2>/dev/null || true
```

Expected:

```text
不存在 experiment-validation-workflow 相关错误；若有普通日志命中，需要人工确认不是图文件缺失或格式错误
```

- [ ] **Step 5: 提交最终导出文件**

Run:

```bash
git add Img/verification/experiment-validation-workflow.svg Img/verification/experiment-validation-workflow.pdf
git commit -m "update chapter four verification workflow figure assets"
```

Expected:

```text
提交成功，输出首行包含新 commit SHA，标题为 "update chapter four verification workflow figure assets"
```

## Self-Review

- Spec coverage: 两阶段结构、约束带、学术化术语、配色方向、PDF 导出、编译验证都已映射到 Task 1-4。
- Placeholder scan: 已移除常见占位词、泛化表述和“后续再补”类描述，所有命令与文本都已写死。
- Type consistency: SVG 中固定使用 `section-title / card-title / card-sub / tag / connector` 五类样式名，避免实施时前后命名漂移。
