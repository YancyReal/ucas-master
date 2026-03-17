# Repository Guidelines

## Project Structure & Module Organization
本仓库用于维护硕士论文源码。主入口是 `Thesis.tex`；章节内容放在 `Tex/`，其中 `Mainmatter.tex` 串联 `Chap_*.tex`；样式和模板类在 `Style/`；参考文献在 `Biblio/ref.bib`；图片在 `Img/`；编译产物输出到 `Tmp/`。`Report/ucasproposal/` 是独立仓库，用于中期报告，不应与主论文改动混在一次提交中。

## External Code & Experiment Sources
论文涉及的实际项目代码不在本仓库内，而在 `/workspace/aosp/art`；benchmark、实验结果和方案报告在 `/workspace/aosp/tmp/MyBenchMark`。修改论文中的实现细节、实验流程、性能结论前，先核对这两个目录下的说明文档与现有数据，不要把 `ucasthesis/` 误当成源码或结果归档仓库。

## Build, Test, and Development Commands
- `cd /workspace/ucasthesis && ./artratex.sh xa Thesis.tex`：编译主论文。

## Coding Style & Naming Conventions
LaTeX 文件沿用现有入口拆分方式，新增章节优先使用 `Tex/Chap_*.tex` 命名。只修改必要文件，不手工编辑 `Tmp/` 生成物。ART 代码风格遵循 `/workspace/aosp/art/.clang-format`、`CPPLINT.cfg` 和既有命名习惯；run-test 目录使用 `NNN-Name`，gtest 文件以 `*_test.cc` 结尾。

## Testing Guidelines
论文仓库本身没有单元测试，验收以成功编译、目录/引用/文献无错误为准。实验数据统一放在 `/workspace/aosp/tmp/MyBenchMark/test-data/`，方案报告放在 `/workspace/aosp/tmp/MyBenchMark/reports/`。`DaCapo` 的 `msec` 越小越好，`SPECjvm2008` 的 `ops/m` 越大越好；`scheme3/` 只保留正式方案3，其余候选或失败数据归档到 `scheme3-archive/`。

## Commit & Pull Request Guidelines
本仓库历史提交多为短标题、单主题，如 `封面`、`minor updates`、`Update Backmatter.tex`。继续保持一次提交只做一类变更，避免混入 `Tmp/` 产物或无关图片。若论文内容依赖外部 ART 或 benchmark 修改，提交说明中应写清对应目录、验证命令和结果来源。

## Agent-Specific Instructions
- 错误纠正规则：当论文内容涉及实现代码、benchmark 或实验数据时，必须先检查 `/workspace/aosp/art` 与 `/workspace/aosp/tmp/MyBenchMark` 的说明文件，不能默认认为相关信息全部位于当前论文仓库。
