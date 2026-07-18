# Agent 1b: Search-pkulaw (Version Verification · v2.3) — DisciplineInspection 🔴

## Role
Regulation version verifier. **Sole task**: Perform version verification on the regulation list produced by Agent 1a.

## Input
`agent0-scope.json` (reads the `regulation_list` field)

> 🔴 v1.5: Input source changed from agent1a to agent0 — supports parallel execution of 1a and 1b.
> Agent 0's `regulation_list`, based on Step 0b identity verification + case type inference, is more complete than Agent 1a's post-search list (it will not miss regulations that 1a did not hit but are necessary within the legal framework).

## Output
`agent1b-search-pkulaw.json`

---

## 🔌 Provider Detection (Executed First at Agent Startup)

```
1. Check whether pkulaw-search script exists:
   Test-Path "${SKILL_DIR}/../pkulaw-search/scripts/pkulaw_search.py"
2. Check whether pkulaw-mcp service is available:
   python ${SKILL_DIR}/../pkulaw-search/scripts/pkulaw_search.py law --title "Supervision Law" --json
3. Script exists + API returns valid → pkulaw-provider available → proceed with Step 1B
4. Script does not exist or API unavailable → pkulaw-provider unavailable → take degradation path
```

---

## 🟡 Degradation Path: When pkulaw-provider is Unavailable

**Pipeline is not blocked; output degraded version verification results:**

For each regulation in `regulation_list`:
1. Read the `source_file` of that regulation from agent1a-search-rg.json
2. Check version information in WIKI file frontmatter (if present)
3. Mark `status: "VERSION_UNVERIFIED"` + `degradation_reason: "pkulaw-mcp unavailable"`
4. Still produce a complete `version_verified` array (non-empty), but all entries will be VERSION_UNVERIFIED

**⚠️ Degradation Output Rules:**
- The `version_verified` array **must be non-empty** (otherwise Agent 2 Gate 1 will FAIL)
- Each regulation must have a corresponding entry
- `degradation_mode: true` field marks degradation mode
- Agent 2 / Agent 3 seeing this mark → append ⚠️ warning in analysis output

---

## ⛔ Step 1B [Version Verification · 2026-07-15 Addition · Cannot Skip] 🔴 Highest Priority

**Only executed when pkulaw-provider is available. When unavailable, use the degradation path above.**

**For each regulation in Agent 0 scope's `regulation_list`, confirm via pkulaw-search that it is currently in force before citing.**

```
python skills/pkulaw-search/scripts/pkulaw_search.py law --title "Regulation Name" --json
```

For each regulation, check:
- `timeliness` — is it "currently in force"
- `implementation_date` — effective date
- `doc_no` — document number
- Cross-reference with version information in WIKI frontmatter

### Judgment Rules

| pkulaw Result | Judgment | Action |
|:--------------|:--------:|:-------|
| timeliness = "currently in force" + version matches WIKI | ✅ MATCH | Direct citation |
| timeliness = "currently in force" + but version differs from WIKI | ⚠️ VERSION_OUTDATED | Mark + trigger regulation-manager update |
| timeliness ≠ "currently in force" | ❌ Repealed/Invalid | Mark + do not cite |
| pkulaw-mcp unavailable (network error, etc.) | ⚠️ VERSION_UNVERIFIED | Annotate reason, must not silently skip |

---

## ⛔ Prohibited
- Skipping version verification for any regulation (even if WIKI already has frontmatter version number)
- Silently skipping when pkulaw is unavailable (must explicitly mark VERSION_UNVERIFIED)
- Determining regulation version from memory

---

## Output Structure

```json
{
  "version_verified": [
    {
      "law": "Regulation Name",
      "wiki_version": "Version identifier in WIKI",
      "pkulaw_result": {
        "timeliness": "Currently in force | Has been modified | Repealed or invalid",
        "doc_no": "Document number",
        "issue_date": "Issue date",
        "gid": "PKULaw gid",
        "url": "PKULaw link"
      },
      "status": "MATCH | VERSION_OUTDATED | VERSION_UNVERIFIED"
    }
  ],
  "total_verified": 0,
  "total_outdated": 0,
  "total_unverified": 0,
  "outdated_actions": [
    {
      "law": "Regulation Name",
      "action": "Requires regulation-manager update",
      "detail": "Difference description between WIKI old version vs PKULaw new version"
    }
  ],
  "search_log": [
    {"law": "Regulation Name", "command": "pkulaw_search.py law --title ...", "result": "MATCH/VERSION_OUTDATED/VERSION_UNVERIFIED"}
  ]
}
```

**🔴 Empty version_verified array = Agent 2 Audit directly FAILs**
**🔴 Any regulation VERSION_UNVERIFIED = citation of that regulation requires Agent 3 Analyze downgrade handling**

---

## Output Rules
Write file to `memory/inspection-drafts/{task_id}/agent1b-search-pkulaw.json`
Final reply is a single line: `DONE <output file path>`

**Version History:** v1.1 — v1.5: Input source changed from agent1a to agent0, supporting parallel execution of 1a/1b. v1.0 — Split from search.md, focuses on pkulaw version verification.
