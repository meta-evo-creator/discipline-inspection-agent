# Agent 6: Revise (Fix · v2.4) — DisciplineInspection

## Task
Based on the must_fix items in `agent5-review_ledger.json`, fix `agent4-draft.md` item by item.

## v2.4 核查报告标准增强检查清单

修订时必须逐条确认：

| # | 检查项 | 要求 |
|:-:|:-----|:-----|
| 1 | 调查过程章节 | 包含具体调查方法+证据数量 |
| 2 | 逐条指控回应 | 每个违规点独立一节，不可合并 |
| 3 | "经查→认为"链路 | 每个指控先列证据再给结论 |
| 4 | 瑕疵不遗漏 | 程序问题即使不影响定性也要列明 |
| 5 | 结论克制 | "经调查，认为构成"而非"构成"；"未发现"而非"不存在" |
| 6 | 涉案财物处置 | 单独章节，区分消费性/可追缴/已退还 |
| 7 | 溯源标注 | 每项事实断言必须有 `[溯源路径]` |

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

## 🔵 Output Schema (v2.4)

```json
{
  "required_files": ["agent6-final.md", "revision_log.json"],
  "revision_log.json": {
    "required": ["review_score_before", "review_score_after", "fixes_applied"],
    "fixes_applied": { "minItems": 1 }
  }
}
```

Both files must exist and be non-empty. Either missing → mark Agent 6 FAILED.

---

## 🎯 Execution Tuning (v2.4)

> Lessons from real case execution. Populated by monthly cron from `_lessons.json`.

<!-- TUNING_START -->
(No execution tuning records yet. Monthly cron will inject from _lessons.json.)
<!-- TUNING_END -->

---

## Output Rules
Write files to `memory/inspection-drafts/{task_id}/agent6-final.md` and `revision_log.json`
Final reply is a single line: `DONE <output file path>`
