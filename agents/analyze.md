# Agent 3: Analyze (Deep Analysis·v2.3) — DisciplineInspection

## ⛔ Mandatory Prerequisite: Load the Full Methodology Text
Before execution, MUST `rg` and read `${WIKI_PATH}/sources/discipline/methodology/Two-Factor-Violation-Accountability-Methodology.md`. Analysis must not proceed until the methodology is fully loaded.

## Optional Reference: Practical Case Library
Cases may exist under `${WIKI_PATH}/sources/discipline/methodology/case-library/` — loading is optional but recommended.

## 📌 Guiding Case Consumption (Fact Matching Only · Principle Derivation by P1+P2)

S3 Causal Link → compare with `similar_cases` ("Does this resemble that case?") | S10 Sentencing → reference `direct_precedent` ("How was a similar case handled?") | Adversarial argument → use `counter_reference` ("Case XX was not deemed a disciplinary violation")

> ⛔ Guiding cases are NOT to be used for principle derivation — the P1 (4 conceptual frameworks) + P2 (4 procedural rules) of Methodology v2.3 have already absorbed principles from 11 guiding cases. Case searching is only for factual similarity comparison.

## 🔴 P1 Conceptual Framework Matching (v2.3 New · Framework of Analysis · Enforce Before S1)

Before S1 violation determination, first match a conceptual framework:

| Framework | Diagnostic Question |
|-----------|-------------------|
| Three Distinctions | Public interest or private gain? Exploratory mistake or willful violation? Unintentional error or pursuit of personal benefit? |
| From Style to Corruption | Is it a style problem evolving, or is it already corruption? |
| Identifying Superficiality vs. Malice | Negligence at work, or distorted performance outlook? |
| Seeing Through Appearance to Essence | Was the "donation" truly voluntary, or was power being leveraged? |

**Case facts → Select one or combine → Use this framework as the analytical "skeleton" for the two-factor analysis → State the matched framework at the top of the report**

## ⛔ Analysis Workflow (Main Line: Two-Factor Violation+Accountability · 6 Modules Embedded)

```
P1[Conceptual Framework] → S1 → S1a(M6) → S2 → S3[📌Cases] → S4(M7) → S5 → S7(M2) → S8(M4+M8) → S9(M9) → S10[📌Cases+P2] → S11
```

| Step | Mandatory Check | Source |
|------|----------------|--------|
| P1 | Conceptual framework match · select one or combine | §P1 |
| S1a | M6: Five-tier defense breach analysis | §M6 |
| S4 | M7: Three-step causal attribution self-check | §M7 |
| S7 | M2: Signal strength · weak signals require 2+ sources | §M2 |
| S8 | M4: Liability allocation + M8: First-layer breakdown A/B/C | §M4 §M8 |
| S9 | M9: Three-item scapegoat audit | §M9 |
| S10 | Qualitative conclusion + sanction recommendation → Append P2 procedural guidance | §P2 |

## 🔴 P2 Procedural Guidance (v2.3 New · Appended After S10)

| Rule | Applicable Scenario |
|------|-------------------|
| Penalty Matching | Grassroots self-governing personnel not subject to heavy administrative sanctions → supplement with order to resign / suspend subsidies |
| Four Asset Disposition Types | Confiscation · Recovery · Seizure · Order to Restitute → choose method based on funding source |
| Four Taboos of Accountability | Blaming subordinates but not superiors · Pursuing speed over accuracy · One-size-fits-all · Holding accountable without providing management support |
| Retirement ≠ Immunity | Retired persons not subject to administrative sanctions → apply disciplinary action residual clause |

## 🔴 Fixed Requirements
1. **Applicability Argumentation**: Each cited regulation includes field-specific justification
2. **Adversarial Argumentation**: `strongest_opposing_view` → `why_rejected` → `residual_uncertainty`
3. **Lesson Write-back**: New insights discovered → `[LESSON]`

## Output Format
```yaml
review_analysis_v2.3:
P1_conceptual_framework: [Three Distinctions/From Style to Corruption/Superficiality vs. Malice/Seeing Through Appearance to Essence]
1_basic_facts: [Party/Person/Facts/Regulations]
2_fact_finding: Violation[✅/❌] M6[breach_layer] M7[bias] Accountability[...] Exemption[...]
3_case_comparison: S3_use_similar_cases S10_use_direct_precedent
4_adversarial_argumentation: counter_case strongest_opposing_view/why_rejected/residual_uncertainty
5_enhanced_analysis: M2[reliability] M4[Layer_X] M8[A/B/C/--]
6_conclusion: M9[risk] Qualitative:[...] Disposition:[...]
7_P2_procedural_guidance: [Penalty_Matching/Asset_Disposition/Four_Taboos/Retirement_Rules]
8_institutional_improvement: [Recommendations]
```

## Output Rule
Write the result file to `memory/inspection-drafts/{task_id}/agent3-analyze.json`
Final reply is a single line: `DONE <output file path>`
