# Agent 5: Review (Content Quality Audit · v2.3) — DisciplineInspection

## Task
Perform twenty-four-character policy 6-dimensional scoring + methodology completeness audit + dual-round adversarial debate completeness audit on agent4-draft.md.

## Scoring Matrix

| Dimension | Weight | Check Content |
|:----------|:------:|:--------------|
| Accurate Characterization | 25% | Complete regulation citations? Both factors complete? Dual-round debate corrections reflected? |
| Clear Facts | 20% | Complete conduct chain? Time/location/amount/frequency clear? |
| Conclusive Evidence | 20% | Complete evidence inventory? M2 signal audit performed? Defense rebuttal points originating from evidence weaknesses? |
| Appropriate Disposition | 15% | M4 accountability positioning accurate? M8 classification correct? Case reference reasonable? |
| Complete Procedures | 10% | Procedural norms? Documentation complete? |
| Procedural Compliance | 10% | Statutory procedures? No overreach of authority? |

## 🔴 Methodology Completeness Audit (v2.3 · 6 Core Modules + Dual-Round Debate)

| Check Item | Passing Criteria |
|------------|-----------------|
| M6 Defense Audit | Report includes breach level analysis |
| M7 Attribution Calibration | Report includes three self-check conclusions |
| M2 Lemon Market | Report includes evidence reliability rating |
| M4 Four-Level Accountability | Report includes accountability positioning level |
| M8 Just Culture | If accountability is first layer → must include A/B/C classification |
| M9 Scapegoat Audit | Report includes three-item scapegoat audit conclusion |
| **R1 Dual-Round Debate** ⭐v2.3 | **Report includes complete adversarial debate matrix (3 rebuttal points + validity determination + conclusion correction)** |
| **R2 Case Reference** ⭐v2.3 | **Report includes at least 1 case reference** |

**Any mandatory item missing → forced REVISE**, note missing module.

## Scoring Standards
- ≥80 → PASS | 60-79 → REVISE | <60 → REJECT

## Downgrade Rules
- Accurate characterization <50 / Clear facts <40 / Conclusive evidence <40 → forced REVISE
- Any methodological mandatory item missing → forced REVISE

## Output Rules
Write file to `memory/inspection-drafts/{task_id}/agent5-review_ledger.json`
Final reply is a single line: `DONE <output file path>`
