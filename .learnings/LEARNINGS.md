# Learnings

## [LRN-20260326-001] correction

**Logged**: 2026-03-26T02:13:06Z
**Priority**: high
**Status**: promoted
**Promoted**: AGENTS.md
**Area**: docs

### Summary
处理本仓库文献相关任务时，使用任何文献前必须先验证其事实存在，并在用户纠正流程后同步走 self-improvement 的记录与提升流程。

### Details
本次对话中，用户新增了“使用任何文献前都需要验证它事实存在”的规则，并进一步指出该规则应按 self-improvement skill 先记录到项目 learnings，再提升到项目级 AGENTS 规则。此前只口头承诺写入 AGENTS.md，没有先在项目内建立 learnings 记录，也没有及时匹配到该 skill 的触发条件，流程不完整。

### Suggested Action
1. 在项目级 AGENTS.md 中固化“文献使用前必须先做存在性验证”的规则。
2. 后续凡是用户纠正工作流、验证标准或长期规则时，先记入 `.learnings/LEARNINGS.md`，再决定是否提升到 AGENTS.md。
3. 文献存在性验证至少依赖一种权威来源，不以本地 PDF 或二手转述作为充分依据。

### Metadata
- Source: user_feedback
- Related Files: AGENTS.md, .learnings/LEARNINGS.md
- Tags: citations, workflow, self-improvement, verification
- Pattern-Key: workflow.citation_existence_verification
- Recurrence-Count: 1
- First-Seen: 2026-03-26
- Last-Seen: 2026-03-26

### Resolution
- **Resolved**: 2026-03-26T02:13:06Z
- **Commit/PR**: 未提交
- **Notes**: 已在项目内建立 learning 记录，并将文献存在性验证规则提升到 AGENTS.md。

---

## [LRN-20260326-002] correction

**Logged**: 2026-03-26T04:51:54Z
**Priority**: medium
**Status**: resolved
**Area**: docs

### Summary
当用户要求“不要继续使用某条参考文献”但又明确希望保留原始条目时，应优先注释停用，而不是直接删除。

### Details
本次处理中，原计划在清理朱奇正相关工作时直接删除 `Biblio/ref.bib` 中的 `Zhu2025ARTOL` 条目。用户随后明确更正为“我希望只是注释掉 不删除这一条”。这说明在文献清理任务里，“停用引用”和“物理删除条目”不是同一个操作；若用户希望保留痕迹、便于后续恢复或对照，应采用注释方式停用。

### Suggested Action
1. 若用户仅要求当前论文不再使用某文献，先确认是“删除”还是“注释停用”。
2. 在未得到进一步确认前，优先采用可逆的最小改动，例如对 `ref.bib` 条目逐行注释。
3. 注释后仍需完整编译，确认不存在残留的未解析引用。

### Metadata
- Source: user_feedback
- Related Files: Biblio/ref.bib, .learnings/LEARNINGS.md
- Tags: bibliography, deletion-vs-comment, self-improvement, workflow
- Pattern-Key: workflow.bibliography_disable_by_comment
- Recurrence-Count: 1
- First-Seen: 2026-03-26
- Last-Seen: 2026-03-26

### Resolution
- **Resolved**: 2026-03-26T04:51:54Z
- **Commit/PR**: 未提交
- **Notes**: 本次对 `Zhu2025ARTOL` 采用注释停用而非删除。

---
