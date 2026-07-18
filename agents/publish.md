# Agent 7: Publish (v2.5.1) — DisciplineInspection

## Task
After Agent 6 (Revise) completes, run post-pipeline steps:
1. **Step 7a — IMA Upload:** Upload `agent6-final.md` to the designated IMA knowledge base
2. **Step 7b — LESSON Collection:** Scan all agent output files for `[LESSON]` markers and append to `_lessons.json`
3. **Step 7c — Quality Dashboard:** Update `_pipeline_quality_log.json` with quality metrics

## Input
All upstream agent outputs in `memory/inspection-drafts/{task_id}/`:
- `agent0-scope.json` through `agent6-final.md`
- `revision_log.json`
- `pipeline_failure_log.json` (if any)

## Output

### Step 7b — LESSON Output
```json
{
  "pipeline_id": "DI-YYYYMMDD-seq",
  "date": "ISO-8601",
  "complete": true,
  "lessons_collected": 0,
  "urgent_lessons": [],
  "scan_path": "memory/inspection-drafts/{task_id}/",
  "lessons": [
    {
      "source_agent": "agentN",
      "category": "methodology | regulation | case | procedure | kg",
      "urgency": "P0 | P1 | P2",
      "lesson": "...",
      "action": "UPDATE_AGENT | ADD_CASE_TAG | UPDATE_REGULATION | UPDATE_KG | NOTE_ONLY"
    }
  ]
}
```

### Step 7c — Quality Entry
```json
{
  "pipeline_id": "DI-YYYYMMDD-seq",
  "timestamp": "ISO-8601",
  "quality": {
    "agent2_audit": "PASS | PASS_WITH_WARNINGS | FAIL",
    "agent5_score": 0-100,
    "agent5_dimensions": { ... },
    "upstream_feedback": [],
    "lessons_generated": 0,
    "retries": 0
  }
}
```

## Execution Protocol

### Step 7a — IMA Upload
Execute from main session:
```
node skills/solo-file-transfer/scripts/ima_upload.cjs <agent6-final.md> <KB_ID>
```
KB_ID is the target knowledge base ID (configurable per deployment).

### Step 7b — LESSON Collection
1. `rg "\[LESSON\]" memory/inspection-drafts/{task_id}/` across all json/md files
2. For each match, extract structured lesson
3. Append to `memory/inspection-drafts/_lessons.json`
4. P0 urgency → IMMEDIATE wecom notification to domain owner:
   `"⚡ DI URGENT LESSON | {task_id} | {source_agent} | {lesson_summary_first_80_chars}"`

### Step 7c — Quality Dashboard
1. Read `agent2-audit.json` for audit conclusion
2. Read `agent5-review_ledger.json` for quality score + dimensions
3. Read `pipeline_failure_log.json` for retry count
4. Count `[LESSON]` markers for `lessons_generated`
5. Collect upstream feedback from all agents
6. Append entry to `memory/inspection-drafts/_pipeline_quality_log.json`
7. Compare current score with last 3 runs' average → deviation >15 → flag for review

## 🔵 Output Schema (v2.5.1)

```json
{
  "required": ["pipeline_id", "date", "complete", "lessons_collected", "scan_path"],
  "complete": { "type": "boolean" },
  "lessons_collected": { "type": "integer", "min": 0 },
  "lessons": {
    "items": {
      "required": ["source_agent", "category", "lesson"],
      "category": { "enum": ["methodology", "regulation", "case", "procedure", "kg"] },
      "urgency": { "enum": ["P0", "P1", "P2"] }
    }
  }
}
```

## 🎯 Execution Tuning (v2.5.1)

> Lessons from real case execution. Populated by monthly cron from `_lessons.json`.

<!-- TUNING_START -->
(No execution tuning records yet. Monthly cron will inject from _lessons.json.)
<!-- TUNING_END -->

---

## Output Rules
Write to `memory/inspection-drafts/{task_id}/agent7-publish-report.json` (normal case) or `pipeline_failure_log.json` (failure).
Final reply is a single line: `DONE <report path>`
