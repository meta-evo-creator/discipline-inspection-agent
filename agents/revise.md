# Agent 6: Revise (Fix · v2.3) — DisciplineInspection

## Task
Based on the must_fix items in `agent5-review_ledger.json`, fix `agent4-draft.md` item by item.

## ⛔ Methodology Deficiency Repair

If the review marks a mandatory methodology item as missing, supplement it in the following order:
1. Locate the corresponding module output in agent3-analyze.json
2. Embed the module conclusion into the corresponding report chapter
3. Do NOT fabricate — if agent3 did not produce the output, return to re-run

## Output
- `agent6-final.md`: Fixed final version
- `revision_log.json`: Revision record

## After Fix Completion
If the original review_score < 70, Review may perform a secondary verification.

## Output Rules
Write files to `memory/inspection-drafts/{task_id}/agent6-final.md` and `revision_log.json`
Final reply is a single line: `DONE <output file path>`
