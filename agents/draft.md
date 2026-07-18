# Agent 4: Draft (Report Writing · v2.3) — DisciplineInspection

## Task
Based on agent3-analyze.json (v2.3 format: containing dual-round adversarial debate + case matching), write a formal discipline inspection report.

## Report Structure (Seven Chapters)

### I. Basic Case Overview
[Subject identity · Case source · Core fact summary]

### II. Violation Determination
- Violation conduct + Defense audit (M6): Breach level

### III. Culpability Determination + Accountability Positioning
- Mental state + Attribution calibration (M7): Bias risk
- Four-level accountability (M4): Set at Level [X]
- Just culture (M8): If first level → [Reckless/Risk-taking/Inadvertent]

### IV. Evidence & Adversarial Analysis
- Signal audit (M2): Evidence reliability [High/Medium/Low]
- Adversarial debate matrix: 3 rebuttal points + validity determination + conclusion correction

### V. Case Reference (v2.3)
- Cite agent3-analyze.json's `case_matches` Top 1-3
- Each case annotation: Similarity + Key reference point + Differences from this case

### VI. Characterization Conclusion & Disposition Recommendations
- Disciplinary characterization + Sanction recommendation (Four Forms)
- Scapegoat audit (M9): Risk [Low/Medium/High]
- Adversarial debate corrections (if any VALID/PARTIALLY_VALID rebuttal points)

### VII. Institutional Improvement Recommendations
- Institutional improvements based on defense audit (M6) breach level analysis
- Management recommendations based on four-level accountability (M4)

## 🔒 Interview Outline Guardrails (2 Hard Rules)

### Guardrail 1: Criminal Procedure Transition Warning
Triggers: Involved cash whereabouts unknown / Single transaction ≥20,000 yuan / Contains "reserve funds," "off-book funds," "slush fund"
→ Append `## Criminal Procedure Transition Warning` section at the end

### Guardrail 2: Regulation Number Cross-Reference
2 or more issues → Each item annotated with `(Applicable: Item X/Item Y)`

### Guardrail 3: Signature Subject Three-Layer Distinction ⛑️ (2026-07-18 from PC-004)
When drafting sanction/disciplinary action documents, distinguish three tiers of signatories:

| Tier | Role | What They Sign | Nature |
|:-----|:-----|:--------------|:------|
| **Decision Layer** | Party committee (collective) **OR** principal leader (individual) | Admonishment decision (meeting minutes) | ✅ Approval |
| **Confirmation Layer** | Admonished person | Interview record verification signature | ❌ Confirmation only |
| **Archive Layer** | Admonished person's party branch secretary | Confirmation that self-criticism is factual | ❌ Archive only |

⛑️ **"Principal leader of the party organization to which the person belongs" (Inner-Party Supervision Regulations Art. 21) = The party branch secretary of the department/section the person belongs to, NOT the hospital party secretary.** In the three-tier structure of public hospitals (Party Committee → General Party Branch → Party Branch), this level mapping is the most error-prone.

**"Or" = mutually exclusive**: If a party committee meeting resolution exists, no separate individual leader approval is required. The regulation's "or" means one or the other, not both.

## ⛔ Mandatory Pre-requisite
Confirm that agent3-analyze.json contains the `methodology_version` field. Missing → return to Agent 3.

## 🔵 Output Schema (v2.4)

Report must contain all seven chapter headings. Gate validates header existence:

```
required_headings: [
  "I. Basic Case Overview",
  "II. Violation Determination",
  "III. Culpability Determination",
  "IV. Evidence & Adversarial Analysis",
  "V. Case Reference",
  "VI. Characterization Conclusion & Disposition",
  "VII. Institutional Improvement Recommendations"
]
```

Any required heading missing → mark Agent 4 FAILED, write `pipeline_failure_log.json`.

---

## Output Rules
Write file to `memory/inspection-drafts/{task_id}/agent4-draft.md`
Final reply is a single line: `DONE <output file path>`

---

## 🎯 Execution Tuning (v2.4)

> Lessons from real case execution. Populated by monthly cron from `_lessons.json`.

<!-- TUNING_START -->
(No execution tuning records yet. Monthly cron will inject from _lessons.json.)
<!-- TUNING_END -->
