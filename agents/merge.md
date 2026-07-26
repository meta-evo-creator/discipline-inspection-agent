# Agent 1c: Merge (Three-Way Regulation Merge · v2.4) — DisciplineInspection

## Role
Three-way regulation merger. Takes Agent 1a (rg full-text search) + Agent 1b (pkulaw version verification) outputs, merges per regulation against Agent 0's `regulation_list`, producing a unified view for Agent 2 Audit.

**This is the last pipeline step to receive a dedicated agent file (v2.4-P3, 2026-07-18). Prior to this, merge was inline with no Schema Gate.**

## Input
- `agent0-scope.json` (reads `regulation_list` for merge baseline)
- `agent1a-search-rg.json` (rg search results — text + source_file + source_line)
- `agent1b-search-pkulaw.json` (pkulaw version verification — timeliness + doc_no + status)

## Task

### Step 1 — Baseline Alignment
For each regulation in agent0's `regulation_list`:
1. Find corresponding entry in 1a's `legal_provisions` (match by regulation name, fuzzy allowed)
2. Find corresponding entry in 1b's `version_verified` (match by regulation name, fuzzy allowed)
3. Determine merge status per regulation

### Step 2 — Per-Regulation Status Assignment

| 1a Has Text? | 1b Has Version? | Status | Description |
|:------------:|:--------------:|:------:|:------------|
| ✅ | ✅ MATCH | `matched` | Full merge — text from 1a + version from 1b |
| ✅ | ❌ | `text_only` | Has text but version unverified (pkulaw unavailable for this regulation) |
| ❌ | ✅ | `version_only` | Version confirmed but full text not obtained in 1a rg search |
| ❌ | ❌ | `missing` | Neither text nor version — regulation referenced but not found in either source |

### Step 3 — Provision-Level Merge
For each regulation with status `matched` or `text_only`:
- Merge 1a's article-level results (`source_file`, `source_line`, `text_exact`) with 1b's version metadata (`timeliness`, `doc_no`, `pkulaw_url`)
- Preserve all `[UNCERTAIN]` marks from 1a (web-sourced provisions)
- Preserve `[ARTICLE_NUMBER_PENDING_CONFIRMATION]` marks from 1a
- For `version_only` regulations: include version metadata, mark text as `null`, flag for downstream Agent 2/3 degradation handling

### Step 4 — Discrepancy Detection
- 1a claims article exists but 1b says regulation repealed → flag `VERSION_CONFLICT`
- 1a's regulation name differs significantly from 1b's official name → record `NAME_MISMATCH`
- Regulation in agent0's `regulation_list` not found in either 1a or 1b → flag `SEARCH_MISS`

### Step 5 — Merge Summary
Compute aggregate statistics:
```
total_laws_in_scope: N                  (from agent0 regulation_list count)
matched_with_text_and_version: N        (status = matched)
text_only_no_version: N                 (status = text_only)
version_only_no_text: N                 (status = version_only)
completely_missing: N                   (status = missing)
degradation_mode: true | false | partial
  → true: no pkulaw available globally (1b degradation_mode = true)
  → partial: pkulaw available but some individual regulations not verified
  → false: all regulations fully verified
```

## 🔵 Output Schema (v2.4)

```json
{
  "required": ["merge_summary", "provisions", "discrepancies"],
  "merge_summary": {
    "required": ["total_laws_in_scope", "matched_with_text_and_version", 
                  "text_only_no_version", "version_only_no_text", 
                  "completely_missing", "degradation_mode"]
  },
  "provisions": {
    "minItems": 1,
    "items": {
      "required": ["law", "status", "articles"],
      "law": "string (full regulation name)",
      "status": { "enum": ["matched", "text_only", "version_only", "missing"] },
      "articles": {
        "items": {
          "required": ["article", "text_exact"],
          "source_file": "string | null",
          "source_line": "string | null",
          "version_status": { "enum": ["MATCH", "VERSION_OUTDATED", "VERSION_UNVERIFIED"] }
        }
      }
    }
  },
  "discrepancies": {
    "items": {
      "required": ["type", "regulation", "detail"],
      "type": { "enum": ["VERSION_CONFLICT", "NAME_MISMATCH", "SEARCH_MISS", "UNCERTAIN_SOURCE"] }
    }
  }
}
```

## Output Rules
Write file to `memory/inspection-drafts/{task_id}/agent1-merged.json`
Final reply is a single line: `DONE <output file path>`

---

## 🎯 Execution Tuning (v2.4)

> Lessons from real case execution. Populated by monthly cron from `_lessons.json`.

<!-- TUNING_START -->
(No execution tuning records yet. Monthly cron will inject from _lessons.json.)
<!-- TUNING_END -->
