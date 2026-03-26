# Errors

## [ERR-20260326-001] bibtex_comment_syntax

**Logged**: 2026-03-26T04:53:04Z
**Priority**: medium
**Status**: resolved
**Area**: docs

### Summary
在 `.bib` 条目上逐行使用 `%` 进行注释会触发 BibTeX 解析错误，不能作为安全的停用方式。

### Error
```text
You're missing a field name---line 262 of file Biblio/ref.bib
: 
: %     author  = {朱奇正},
(Error may have been on previous line)
I'm skipping whatever remains of this entry
```

### Context
- Command/operation attempted: `./artratex.sh xa Thesis`
- Intent: 将 `Zhu2025ARTOL` 保留在 `ref.bib` 中，但通过注释方式停用
- Environment details: TeX Live 2025, BibTeX 0.99d

### Suggested Fix
若需在 `.bib` 中保留原始条目但停用，应使用 BibTeX 可忽略的形式，例如移除条目起始 `@`，而不是逐行加 `%`。

### Metadata
- Reproducible: yes
- Related Files: Biblio/ref.bib, .learnings/ERRORS.md

### Resolution
- **Resolved**: 2026-03-26T04:53:04Z
- **Notes**: 已改为无 `@` 的保留块，并重新编译验证。

---
