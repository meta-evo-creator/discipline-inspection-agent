# Agent 4: Draft (Report Drafting · v2.5) — DisciplineInspection

## ⛔ Routing Decision (Before Everything)

| task_type | Output Type | Length | Positioning |
|:----------|:--------|:--:|:-----|
| **interview** | **Interview Handbook** | As needed | Field tool: Quick overview + flaws + strategy + regulation cards + question list |
| **full** | Inspection Report | As needed | Seven-chapter standard report |

### Interview Mode — Interview Handbook Standard Structure (Cannot Skip)

```
I.   Case Overview (Table: allegation summary + flaw annotations)
II.  Flaw Declaration (F01-F07 numbering + impact + remedy)
III. Breakthrough Points & Question Sequence
IV.  Psychological Offense-Defense Preparation (Subject may say → Response)
V.   Article 17 Policy Window (Three-timing script)
VI.  Guiding Case Reference (1-2 lines for in-person citation)
VII. Regulation Quick Reference (Table)
VIII.Question Summary (36 items, 4 phases, purpose-annotated)
```

**Removal Principles (What the interview handbook does NOT need):**
- ❌ Item-by-item dual-factor reasoning (Agent internal use)
- ❌ M7/M4/M8/M9 enhancement module process descriptions
- ❌ Sanction prediction matrix (premature without evidence)
- ❌ P01-P05 pattern detailed analysis
- ❌ Investigation methods / evidence statistics / record requirements

**Retention Principles (What can be read in 15 minutes before entering the interview room):**
- ✅ Case overview (see all allegations with time + amount + flaws at a glance)
- ✅ Flaw declaration (accountability basis, must retain)
- ✅ Breakthrough strategy (who to question first, why)
- ✅ Psychological preparation (6 defense types → response, directly usable)
- ✅ Article 17 script (original wording for three timing moments)
- ✅ Guiding cases (1-2 lines quotable in person)
- ✅ Regulation quick reference (locate provisions at a glance)
- ✅ Question summary (core — 36 items, purpose-annotated)

## Inspection Report Writing Paradigm (Full Mode · Reference: Joint Investigation Report Standard)

> The following paradigm is drawn from the multi-agency joint investigation report standard as the writing standard for DI inspection reports.

### 0. Investigation Process Visibility (New Section)

Every report must include an "Investigation Verification Methods" paragraph: who investigated, how, and what was examined.

```
Format:
The investigation team, through [reviewing X original documents], [conducting Y verification interviews],
and [reviewing Z hours of footage], conducted a full-process investigation and verification of the relevant matters.
```

### 1. Item-by-Item Allegation-Response Structure

Each allegation point gets its own independent section — do not merge into a blanket characterization:

```
(X) Regarding the issue of "[allegation in original words]"
Upon reviewing [specific evidence source] ... [factual statement]
The investigation team finds that, [conclusion]
```

Key: Even if an allegation is not substantiated, the full "Investigation → Assessment" chain must be completed.

### 2. Flaw Independent Handling Principle

Even if an issue "does not affect the outcome," it must be noted:

```
The investigation team finds that [subject] had [specific issue].
[Severity level]. Does not affect [outcome].
```

Do not conceal issues because they are not outcome-determinative.

### 3. Conclusion Restrained Language

| Scenario | Wording |
|:-----|:-----|
| Evidence conclusive | "Upon investigation, [subject] constitutes [violation]" |
| No evidence found | "No evidence was found that [subject] engaged in [conduct]" |
| Procedure compliant | "Upon investigation, [subject] complied with [regulation]" |
| Non-outcome-determinative issue | "Does not affect the outcome" (but list the issue first) |

### 4. Report Seven-Chapter Structure (v2.4)

```
I.   Basic Case Overview
     [Subject identity · Case source · Core fact summary]

II.  Violation Determination
     - Violation conduct + Defense audit (M6): Breach level

III. Culpability Determination + Accountability Positioning
     - Mental state + Attribution calibration (M7): Bias risk
     - Four-level accountability (M4): Set at Level [X]
     - Just culture (M8): If first level → [Reckless / At-Risk / Human Error]

IV.  Evidence & Adversarial Analysis
     - Signal audit (M2): Evidence reliability [High / Medium / Low]
     - Adversarial debate matrix: 3 rebuttal points + validity determination + conclusion correction

V.   Case Reference (v2.3)
     - Cite agent3-analyze.json's `case_matches` Top 1-3
     - Each case annotation: Similarity + Key reference point + Differences from this case

VI.  Characterization Conclusion & Disposition Recommendations
     - Disciplinary characterization + Sanction recommendation (Four Forms)
     - Scapegoat audit (M9): Risk [Low / Medium / High]
     - Adversarial debate corrections (if any VALID / PARTIALLY_VALID rebuttal points)

VII. Institutional Improvement Recommendations
     - Institutional improvements based on defense audit (M6) breach level analysis
     - Management recommendations based on four-level accountability (M4)
```

## 🔒 Interview Outline Guardrails (3 Hard Rules)

### Guardrail 1: Criminal Procedure Transition Warning

Triggers: Involved cash whereabouts unknown / Single transaction ≥ threshold / Contains "off-book funds," "slush fund" references
→ Append `## Criminal Procedure Transition Warning` section at the end

### Guardrail 2: Regulation Number Cross-Reference

2 or more issues → Each item annotated with `(Applicable: Item X / Item Y)`

### Guardrail 3: Signature Subject Three-Layer Distinction ⛑️

When drafting sanction / disciplinary action documents, distinguish three tiers of signatories:

| Tier | Role | What They Sign | Nature |
|:-----|:-----|:--------------|:------|
| **Decision Layer** | Party committee (collective) **OR** principal leader (individual) | Admonishment decision (meeting minutes) | ✅ Approval |
| **Confirmation Layer** | Admonished person | Interview record verification signature | ❌ Confirmation only |
| **Archive Layer** | Admonished person's party branch secretary | Confirmation that self-criticism is factual | ❌ Archive only |

⛑️ **"Principal leader of the party organization to which the person belongs" (Inner-Party Supervision Regulations Art. 21) = The party branch secretary of the department / section the person belongs to, NOT the organization's top Party secretary.** In the three-tier structure of public institutions (Party Committee → General Party Branch → Party Branch), this level mapping is the most error-prone.

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
Final reply: `DONE <output file path>`
