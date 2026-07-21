# Agent 7: Publish (v2.6.0) — DisciplineInspection

## Task
After Agent 6 (Revise) completes, run post-pipeline steps:
1. **Step 7a — IMA Upload:** Upload `agent6-final.md` to the designated IMA knowledge base
2. **Step 7b — LESSON Collection:** Scan all agent output files for `[LESSON]` markers and append to `_lessons.json`. For P0 lessons, include patch-ready context (`target_file`, `old_text`, `new_text`, `confidence`).
3. **Step 7c — Quality Dashboard:** Update `_pipeline_quality_log.json` with quality metrics
4. **Step 7d — Self-Repair Handoff (v2.6.0 NEW):** Structure P0 lessons so the main session's Phase 8 can auto-patch via `skill_manage`. This step only prepares the data — the actual patching is executed by the main session orchestration.

## Input
All upstream agent outputs in `memory/inspection-drafts/{task_id}/`:
- `agent0-scope.json` through `agent6-final.md`
- `revision_log.json`
- `pipeline_failure_log.json` (if any)

## Output

### Step 7b — LESSON Output (v2.6.0)
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
      "confidence": "HIGH | MEDIUM | LOW",
      "lesson": "Human-readable description of what was learned",
      "action": "UPDATE_AGENT | ADD_CASE_TAG | UPDATE_REGULATION | UPDATE_KG | NOTE_ONLY",
      "target_file": "agents/analyze.md  (required for P0+UPDATE_AGENT)",
      "target_section": "## Step 5 — Responsibility Assessment  (for context)",
      "old_text": "The exact string to be replaced (for skill_manage patch)",
      "new_text": "The replacement string"
    }
  ]
}
```

**v2.6.0 NEW fields:**
- `confidence`: HIGH = the fix is unambiguously correct (auto-apply). MEDIUM = likely correct but verify. LOW = needs human review.
- `target_file` / `target_section` / `old_text` / `new_text`: Required when `urgency=P0` and `action=UPDATE_AGENT`. These enable the main session's Phase 8 to execute `skill_manage(action='patch')` without ambiguity.
- If the lesson is about a pattern rather than a specific text fix, set `action=NOTE_ONLY` and omit the patch fields.

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

## 🔵 Output Schema (v2.6.0)

```json
{
  "required": ["pipeline_id", "date", "complete", "lessons_collected", "scan_path"],
  "complete": { "type": "boolean" },
  "lessons_collected": { "type": "integer", "min": 0 },
  "lessons": {
    "items": {
      "required": ["source_agent", "category", "lesson"],
      "category": { "enum": ["methodology", "regulation", "case", "procedure", "kg"] },
      "urgency": { "enum": ["P0", "P1", "P2"] },
      "confidence": { "enum": ["HIGH", "MEDIUM", "LOW"] },
      "action": { "enum": ["UPDATE_AGENT", "ADD_CASE_TAG", "UPDATE_REGULATION", "UPDATE_KG", "NOTE_ONLY"] },
      "target_file": { "type": "string", "required_when": "urgency=P0 AND action=UPDATE_AGENT" },
      "old_text": { "type": "string", "required_when": "urgency=P0 AND action=UPDATE_AGENT" },
      "new_text": { "type": "string", "required_when": "urgency=P0 AND action=UPDATE_AGENT" }
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
