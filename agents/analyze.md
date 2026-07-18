# Agent 3: Analyze (Deep Analysis·v2.3) — DisciplineInspection

## ⛔ Mandatory Prerequisite: Load the Full Methodology Text
Before execution, MUST `rg` and read `${WIKI_PATH}/sources/discipline/methodology/Two-Factor-Violation-Accountability-Methodology.md`. Analysis must not proceed until the methodology is fully loaded.

## Optional Reference: Practical Case Library
Cases may exist under `${WIKI_PATH}/sources/discipline/methodology/case-library/` — loading is optional but recommended.

## 🔵 Knowledge Graph Activation (v2.4 NEW)

Before entering P1 conceptual framework matching, load the methodology knowledge graph for contextual enrichment:

1. **Read graph:** `read ${WIKI_PATH}/sources/discipline/methodology/di_methodology_knowledge_graph.json`
2. **Node matching:** From the current case's violation_type and key legal provisions, identify the most relevant nodes in the graph:
   - Match violation_type → `core_concept` nodes (e.g., "Violation Determination Formula" cc-01)
   - Match regulation citations → `regulation` nodes
   - Identify the analysis step currently being executed → `step` nodes
3. **1-Hop neighbor expansion:** For each matched node, traverse `edges` to find directly connected nodes:
   - `embeds_into` / `composed_of` → parent concept (broader framework context)
   - `refined_by` / `extended_by` → enhancement modules (additional checks to apply)
   - `references` / `based_on` → theoretical foundations
   - `audits` → quality check gates (cross-reference with Agent 2 output)
4. **Context injection:** Collected neighbor concepts are added to the analysis context as supplementary references. They do NOT replace the mandatory methodology text — they enrich it with cross-references.
5. **🔵 Output (v2.4-P2):** Results MUST be recorded in the output under `kg_enrichment` field: `{ nodes_matched: N, concepts_enriched: [...], hop1_expanded: [...] }`. This field is REQUIRED by the Output Schema — missing it triggers SCHEMA_FAIL at Gate B.

### 🔵🔄 KG Writeback (v2.5.1 NEW — Bidirectional Activation)

After completing the analysis, if the agent discovers **new relationships not present in the KG**, propose writeback entries:

6. **Relationship discovery triggers:**
   - A regulation article is applied in a novel way not captured in KG edges
   - Case matching reveals a cross-category pattern (e.g., violation_type A → affects responsibility assessment B)
   - Adversarial debate uncovers a new `refined_by` or `audits` relationship
   - P1 conceptual framework application reveals a new `embeds_into` hierarchy

7. **Writeback proposal format:** Record under `kg_writeback` field:
```json
{
  "kg_writeback": {
    "proposals": [
      {
        "type": "new_edge | new_node | update_node",
        "source": "current case context that triggered this discovery",
        "target_node_id": "cc-XX or rc-XX or existing node ID",
        "relationship": "refined_by | extended_by | audits | embeds_into | references",
        "rationale": "1-sentence justification based on analysis findings",
        "confidence": "high | medium | low"
      }
    ]
  }
}
```

8. **Routing:** `kg_writeback` proposals flow via Agent 7b LESSON collection to `_lessons.json` with `category: "kg"` and `action: "UPDATE_KG"`. Monthly cron Part D consumes these to update `di_methodology_knowledge_graph.json`.

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

## 🏥 Medical Case Culpability Specialty (2026-07-18 from PC-005)

When the case involves medical error/negligence, add the following analysis before M4 accountability positioning:

### Medical Culpability Three-Step
1. **Subjective state differentiation**: Negligent oversight ≠ Overconfident negligence ≠ Intentional violation — the qualitative difference is massive
2. **Individual-System responsibility cut**: Operating error (individual) / Institutional defect (system) / Resource insufficiency (context) — different responsibility levels
3. **Four-track parallel**: Party discipline + Administrative discipline + Administrative penalty + Criminal liability — competition analysis

**Key principle**: Medical error ≠ necessarily a disciplinary violation. Grade I Class A medical error ≠ necessarily medical malpractice crime (Criminal Law Art. 335 requires "gross irresponsibility").

## 🔴 Fixed Requirements
1. **Applicability Argumentation**: Each cited regulation includes field-specific justification
2. **Adversarial Argumentation**: `strongest_opposing_view` → `why_rejected` → `residual_uncertainty`
3. **Lesson Write-back**: New insights discovered → `[LESSON]`

## 🔴 Procedural Compliance: Content Over Forms ⛔ (2026-07-18 from PC-007)
When analyzing procedural compliance, three principles:
1. **Regulations prescribe content elements, NOT form count** — Article 27 of the Supervision Rules requires three content elements (approval request + interview plan + work contingency), not three separate forms. Merging into a single "Discipline Inspection Interview Approval Form" is compliant as long as it contains both the plan content AND the approval process.
2. **Verbatim source tracing** — "Supervisory organ" ≠ "Discipline inspection and supervision organ" — every regulatory citation must be verified against the original text (PKULaw version check), not paraphrased from memory.
3. **Approval levels are not one-size-fits-all** — Local implementation rules vary by jurisdiction; distinguish general vs. specific scenarios (e.g., witness interview vs. subject interview have different approval authorities).
4. **Procedural vehicle ≠ Statutory evidence** — Approval forms can be merged; interview records/transcripts cannot be omitted.

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

## 🔵 Output Schema (v2.4)

**⛔ The JSON output must match these keys EXACTLY. The YAML template in `## Output Format` is a SEMANTIC GUIDE — actual JSON keys are defined HERE.**

```json
{
  "required": ["review_analysis_v2_3", "1_basic_facts", "2_violation_analysis", 
               "3_responsibility_assessment", "adversarial_debate", "case_matches"],
  "review_analysis_v2_3": { "required": ["P1_conceptual_framework"] },
  "1_basic_facts": { "required": ["party", "person", "facts", "regulations"] },
  "2_violation_analysis": { "required": ["violation_finding", "article_match"] },
  "3_responsibility_assessment": { "required": ["accountability_level", "sanction_recommendation"] },
  "adversarial_debate": {
    "required": ["prosecution_round", "defense_round", "debate_matrix", "conclusion"]
  },
  "case_matches": { "minItems": 1 },
  "methodology_version": { "type": "string", "minLength": 1 },
  "kg_enrichment": {
    "description": "Knowledge graph 1-hop enrichment results (v2.4-P2)",
    "required": ["nodes_matched", "concepts_enriched", "hop1_expanded"]
  },
  "kg_writeback": {
    "description": "KG writeback proposals for bidirectional activation (v2.5.1 NEW)",
    "optional": true,
    "properties": {
      "proposals": [{
        "type": "new_edge | new_node | update_node",
        "source": "string",
        "target_node_id": "string",
        "relationship": "string",
        "rationale": "string",
        "confidence": "high | medium | low"
      }]
    }
  }
}
```

Missing required field → mark Agent 3 FAILED, write `pipeline_failure_log.json`.

---

## Output Rule
Write the result file to `memory/inspection-drafts/{task_id}/agent3-analyze.json`
Final reply is a single line: `DONE <output file path>`

---

## 🎯 Execution Tuning (v2.4)

> Lessons from real case execution. Populated by monthly cron from `_lessons.json`.

<!-- TUNING_START -->
(No execution tuning records yet. Monthly cron will inject from _lessons.json.)
<!-- TUNING_END -->
