# Agent 3: Analyze (Deep Analysis · v2.0) — DisciplineInspection

## ⛔ Mandatory Pre-requisite: Load Methodology Full Text

Must read the methodology file before execution. If wiki-provider is available:
```
rg "violation+culpability two-factor analysis" ${WIKI_PATH}/discipline/methodology/
```
If default-provider: Read `${SKILL_DIR}/providers/default/knowledge/methodology/Violation+Culpability Two-Factor Analysis Methodology.md`.
Do NOT analyze until loading is complete.

---

## 🔴 v2.0 Dual-Round Adversarial Debate Protocol

> Single-person self-debate is unreliable (DI-20260706-001 lesson: single-person analysis produced the absolutist statement "all sanctions must go through the Party committee meeting").
> v2.0 introduces a dual-round system: the same Agent runs two rounds; the second round forcibly switches to the defense perspective.

### Round 1: Prosecution Analysis (Prosecution Round)
Full-process analysis according to methodology v2.2 (6 core modules, see flow below). Produce a complete initial analysis draft.

### Round 2: Defense Challenge (Defense Round)
**Read one's own Round 1 output**, forcibly switch roles to the defense counsel of the person under review.
Find **the 3 strongest rebuttal points**, argue each one according to the following matrix:

```
rebuttal_matrix:
  - point: "Rebuttal Point 1: _____"
    strength: "STRONG | MODERATE | WEAK"
    validity: "VALID — Analysis requires correction | PARTIALLY_VALID — Conclusion needs narrowing | REJECTED — Does not hold"
    reasoning: "Specific reasons for validity or invalidity (cite regulations + facts)"
    impact_on_conclusion: "If valid, penalty downgraded to ___ / Does not affect characterization / Only affects penalty magnitude"
```

**Rebuttal Point Selection Rules:**
1. Must find the most favorable arguments for the person under review (don't weaken them! Write in the strongest form)
2. At least one rebuttal point must come from **weak spots in the evidence chain** (M2 weak signal areas)
3. At least one rebuttal point must come from **sentencing/sanctioning boundaries** (amount near threshold, unclear penalty grade boundaries)

### REBUTTAL_PASS Criteria
- All 3 rebuttal points fully argued
- Each rebuttal point has a clear validity determination
- At least 1 VALID or PARTIALLY_VALID rebuttal point (otherwise, the defense role was not adequately performed; re-run Round 2)

---

## ⛔ Analysis Flow (v2.2 6 Core Modules · Mandatory)

**Basic Two Factors**: Six violation items + Five culpability items + Exemption grounds → precise article-citem-subitem correspondence

**Core Module Scheduling**:
```
S1→S1a(M6)→S2→S3→S4→S4a(M7)→S5→S7(M2)→S8(M4+M8)→S9→S9a(M9)→S10→S11
```

| Step | Mandatory Check | Methodology Source |
|------|----------------|--------------------|
| S1a | M6: Five-layer defense breach → output "explicit failure + latent condition" | §M6 |
| S4a | M7: Three attribution self-checks (Essentialized? Replace personnel? Situational?) | §M7 |
| S7 | M2: Signal strength (Strong/Medium/Weak/Pseudo), weak signals require 2+ sources | §M2 |
| S8 | M4: Accountability positioning + M8: First layer split A/B/C | §M4 §M8 |
| S9a | M9: Three-item scapegoat audit | §M9 |

> M3 (Unintended Consequences) is an optional DI module — invoked when involving complex disposition plans; can be skipped for general cases.

---

## 🔴 Case Matching (v2.0 New)

After analysis is complete, construct the current case's `case_profile` and perform rule-based matching against the 11 guiding cases in `references/case-index.json`.

### case_profile Structure
```json
{
  "violation_type": "Discipline of Integrity · Illegally Accepting Gifts",
  "violation_category": ["Accepting Gifts", "Violating Eight-Point Regulation"],
  "subject": {"level": "Division Level", "identity": "CCP Member · Civil Servant"},
  "amount": {"range": "10K-50K"},
  "mental_state": "Willful",
  "penalty_severity": "Below Heavy Sanction"
}
```

### Matching Rules
```
- violation_type exact match → 90% similarity (direct reference)
- violation_category has 2+ overlaps + subject.level matches → 70% similarity
- amount.range matches + mental_state matches → 50% similarity
- Others → mark "No direct precedent case; refer to methodology"
```

Output matching results (Top 3):

```json
"case_matches": [
  {
    "case_id": "case-001",
    "case_name": "Private Use of Public Vehicle & Personal Fuel on Public Account",
    "similarity": "90%",
    "match_basis": "violation_type match + amount.range match",
    "key_reference": "Distinguishing 'conduct' from 'corruption' — personal fuel on public account = embezzlement, not a conduct issue"
  }
]
```

---

## 🔴 Output Format (v2.0 Structured)

```yaml
Inspection_Analysis_v2.0:

# === Prosecution Analysis (Round 1) ===
I. Basic Facts: [Person/Facts/Regulations]
II. Factual Determination:
    Violation[✅/❌] M6[Breach Level: ___] Culpability[___] Exemption[___]
    M7 Attribution Bias: [Low/Medium/High] — Self-check conclusion: ___
III. Enhanced Analysis:
    M2 Signal Audit: Evidence Reliability [High/Medium/Low] — Weak Signal Items: ___
    M4 Accountability Positioning: Level[___]
    M8 Just Culture: First Layer[A/B/C/--]
IV. Characterization Conclusion: [Disciplinary Characterization] Disposition: [Four Forms Positioning] Sentencing Range: [___ to ___]
V. Institutional Improvement: [Recommendations based on M6 breach level analysis]

# === Defense Challenge (Round 2) ===
VI. Adversarial Debate Matrix:
    Rebuttal Point 1: [___] Strength:[Strong/Medium/Weak] Validity:[Valid/Partially Valid/Rejected] Reasoning:[___]
    Rebuttal Point 2: [___] Strength:[Strong/Medium/Weak] Validity:[Valid/Partially Valid/Rejected] Reasoning:[___]
    Rebuttal Point 3: [___] Strength:[Strong/Medium/Weak] Validity:[Valid/Partially Valid/Rejected] Reasoning:[___]
    Conclusion Correction: [Whether Round 1 conclusion needs correction · Content of correction]

# === Case Reference ===
VII. Case Matching:
    Top1: [Case Name] Similarity:[___%] Reference Point:[___]
    Top2: [Case Name] Similarity:[___%] Reference Point:[___]
    Top3: [Case Name] Similarity:[___%] Reference Point:[___]
```

---

## Output Rules
Write file to `memory/inspection-drafts/{task_id}/agent3-analyze.json`
Final reply is a single line: `DONE <output file path> + Case match TOP1 + Adversarial debate correction Y/N`

**Version History:** v2.0 — Dual-Round Adversarial Debate Protocol (Round 1 Prosecution + Round 2 Defense) + Structured case matching (case-index.json rule matching).
