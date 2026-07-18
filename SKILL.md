---
name: discipline-inspection
version: 2.3.0
description: |
  Discipline Inspection v2.3 ⚔️ Methodology v2.3: Dual-Factor + 6 Modules + P1 Policy Framework (4 concepts) + P2 Procedural Guidance (4 rules) + 3 Gates. Focused on party discipline inspection case analysis.
platforms:
  - openclaw
tools:
  - ripgrep
  - sessions_spawn
  - memory_search
  - tavily_search
metadata:
  openclaw:
    emoji: ⚔️
---

# Discipline-Inspection ⚔️ v2.3.0

> **Discipline as the yardstick, vigilance as constant.** 8-Agent File-based Handoff Pipeline + Violation + Responsibility Two-Factor Analysis + Twenty-Four-Character Policy 6-Dimension Review Scoring Matrix.
> Isomorphic architecture with DR v4.0.
> 🔓 Open source under MIT License. For production use, configure a regulation knowledge base (WIKI_PATH) and optional PKULaw version verification.

> 📎 Shared config: `skills/supervision-shared/shared-config.yaml` (WIKI paths / search chains / templates)

---

## 🛡️ No-Authority Boundary

This skill is a **refs-only / no-authority** capability package.

**Outputs of this skill:**
- `violation_finding_ref` — Violation fact finding (candidate)
- `evidence_chain_ref` — Evidence chain references
- `article_match_ref` — Applicable article matching
- `responsibility_assessment_ref` — Responsibility analysis (candidate)
- `sanction_recommendation_ref` — Sanction recommendation (candidate)
- `mitigation_aggravation_ref` — Mitigating/aggravating circumstances
- `owner_gate_handoff_ref` — Domain owner confirmation gate handoff package

**This skill NEVER produces:**
- Final sanction decisions · Accountability conclusions · Organizational action decisions
- Final determinations on case characterization or disciplinary measures
- Any output that substitutes for committee meetings or statutory disciplinary/criminal procedures

The above authority is reserved for the **domain owner** and statutory discipline inspection/supervision procedures.

> This boundary declaration corresponds to SOLO 655 Iron Rule ④ (Clear authority and responsibility: minimal agency — every authorization is temporary, scoped, and revocable).

---

## 📋 Structured Output References (Ref Families)

All Agent outputs in this skill are exchanged via structured refs, replacing free-form reports.

**Reference template:** `references/big-oversight-ref-templates.md` ⚔️ DI Discipline Inspection Ref Family

### Phase → Ref Mapping

| Phase | Agent | Output File | Ref Family |
|:------|:------|:------------|:-----------|
| 0 | Scope | `agent0-scope.json` | `source_pack_ref` |
| 1a | Search-rg | `agent1a-search-rg.json` | `article_match_ref` (article text + source) |
| 1b ∥ | Search-pkulaw | `agent1b-search-pkulaw.json` | `version_verified_ref` |
| 1c | Merge | `agent1-merged.json` | `merged_search_ref` (1a+1b merged) |
| 2 | Audit | `agent2-audit.json` | `evidence_chain_ref` + `article_match_ref` (post-version audit) |
| 3 | Analyze | `agent3-analyze.json` | `violation_finding_ref[]` + `responsibility_assessment_ref` + `mitigation_aggravation_ref` + `sanction_recommendation_ref` |
| 4 | Draft | `agent4-draft.md` | Synthesis of above refs + report/outline content |
| 5 | Review | `agent5-review_ledger.json` | Scoring matrix + fix recommendations (consumes all upstream refs) |
| 6 | Revise | `agent6-final.md` | Corrected candidate final version |
| 7 | Publish | `agent6-final.md` | `owner_gate_handoff_ref` (aggregates all candidates → domain owner confirmation) |

### Handoff Specification

```
Agent 0 (source_pack_ref + regulation_list)
  ├─→ Agent 1a (article_match_ref) ─┐
  └─→ Agent 1b (version_verified_ref) ─┤  ← 🔴 v1.5 Parallel
                                       ↓
                                Agent 1c (merged_search_ref, consumes 1a+1b)
                                       ↓
                                Agent 2 (evidence_chain_ref, consumes merged)
                                       ↓
                                Agent 3 (violation_finding_ref + responsibility_assessment_ref + sanction_recommendation_ref)
                                       ↓
                                Agent 4 (synthesizes all upstream refs into report/outline)
                                       ↓
                                Agent 5 (Review scoring matrix consumes all refs)
                                       ↓
                                Agent 6 (Corrections)
                                       ↓
                                Agent 7 (owner_gate_handoff_ref → domain owner)
```

> Each Agent output file must contain its ref's structured fields (see template for detailed definitions). The main session validates ref completeness (checklist in template) without reading full contents.

---

## ⛔ Entry Block (Cannot Skip · Cannot Degrade)

**Sole entry point** for this skill: Suit Phase 1 Confirmation → `sessions_spawn Agent 0 (scope)`.

The following actions constitute **unauthorized execution** — recorded as `[UNSOURCED-EXECUTION]`:
- Manually searching regulations in the main session
- Manually writing analysis / reports / draft documents in the main session
- Citing regulation article numbers from memory
- Skipping any Agent on grounds of "simple case" or "user urgency"

**This clause is not degradable under any circumstances.**

---

## ⚡ Solo Status Protocol (Mandatory)

Before and after each Agent spawn, update `./solo/pipeline-status.json`.

```json
{
  "pipeline_id": "DI-YYYYMMDD-xxx",
  "skill": "discipline-inspection",
  "version": "2.0.0",
  "topic": "Issue summary",
  "started_at": "ISO timestamp",
  "last_updated": "ISO timestamp",
  "mode": "full / interview / quick",
  "phases": {
    "0: Scope":     {"status": "completed", "detail": "Issue scoping"},
    "1a: Search-rg":  {"status": "running",   "detail": "rg WIKI searching"},
    "1b: Search-pkulaw": {"status": "running",   "detail": "pkulaw version verification ∥ parallel"},
    "1c: Merge":    {"status": "pending",   "detail": ""},
    "2: Audit":     {"status": "pending",   "detail": ""},
    "3: Analyze": {"status": "pending",   "detail": ""},
    "4: Draft":   {"status": "pending",   "detail": ""},
    "5: Review":  {"status": "pending",   "detail": ""},
    "6: Revise":  {"status": "pending",   "detail": ""},
    "7: Publish": {"status": "pending",   "detail": ""}
  }
}
```

---

## 8-Agent Parallel Pipeline (Routed by Mode)

```
Phase 0: Scope       → Agent 0: Issue scoping                → agent0-scope.json
                         ├─→ Agent 1a: rg WIKI search        → agent1a-search-rg.json
                         └─→ Agent 1b: pkulaw version verify → agent1b-search-pkulaw.json  ∥ parallel
Phase 1c: Merge       → Agent 1c: Merge 1a+1b                 → agent1-merged.json
Phase 2: Audit       → Agent 2: Regulation audit (consumes merged) → agent2-audit.json
Phase 3: Analyze   → Agent 3: Deep analysis                  → agent3-analyze.json
Phase 4: Draft     → Agent 4: Write report/outline           → agent4-draft.md
Phase 5: Review    → Agent 5: Content quality audit          → agent5-review_ledger.json
Phase 6: Revise    → Agent 6: Fix                            → agent6-final.md + revision_log.json
Phase 7: Publish   → Main session: solo-file-transfer        → IMA knowledge base
```

**Parallel node:** Agent 0's `regulation_list` feeds both 1a and 1b simultaneously; each runs independently with no cross-dependency. Agent 1c performs lightweight merge (matching + discrepancy tagging). Effective time = max(1a, 1b) + merge(10s).

**Each Agent runs in an independent isolated session (context:isolated, lightContext:true). The main session only handles spawn + gate + file verification.**

> 🔒 **Entropy reduction contract in effect (`skills/solo/SKILL.md §2.3`):** Sub-agent return compressed to DONE + path + ≤3 line summary. File verification checks existence only, does not read full content. Draft/Analysis phases are forcibly isolated in sub-session execution.
> `lightContext` skips full bootstrap injection for token compression — loads only the single-file prompt required by that Agent.

---

## Guardrail Routing: Task Dispatching

| Mode | Trigger Scenario | Pipeline | Agents |
|:-----|:-----------------|:---------|:------:|
| **full** | Case characterization, sanction recommendation | 0→(1a∥1b)→1c→2→3→4→5→6→7 | 8+1 |
| **interview** | Interview outline | 0→(1a∥1b)→1c→2→3+4→7 (Analyze+Draft merged) | 5+1 |
| **quick** | Regulatory consultation, article lookup | 0→(1a∥1b)→1c→2→7 | 4+1 |

**Routing decision point:** After Agent 0 Scope completes, the main session selects mode based on `task_type`.

**Design principle:** Anthropic's 6 Patterns — Guardrail-Routed Architecture — processing depth determined by task type, not complexity.

---

## 🔒 File Existence Verification (Mandatory) + Entropy Constraints

After each Agent spawn completes (status=done), the main session performs file existence check.

**Verification rule:**
```
read <output_file_path> → verify file exists and size > 0
# ⛔ Only verify existence — do NOT read file content into main session context
```

**File not found → Mark Agent as `failed` → Do NOT proceed to next phase → Report specific failure reason to domain owner.**
**File exists → Record path only + 3-line summary → Proceed to next phase.**

---

## Output Path Protocol

```
{pipeline_output_dir}/
├── agent0-scope.json          ← Phase 0: Issue scoping (includes regulation_list)
├── agent1a-search-rg.json     ← Phase 1a: rg WIKI regulation + case + methodology (includes source_line)
├── agent1b-search-pkulaw.json ← Phase 1b: pkulaw version verification (includes version_verified) ∥
├── agent1-merged.json         ← Phase 1c: 1a+1b merge (includes match status + discrepancy tags)
├── agent2-audit.json          ← Phase 2: Regulation citation audit (consumes merged)
├── agent3-analyze.json        ← Phase 3: Analysis reasoning (interview mode = analysis + draft outline)
├── agent4-draft.md            ← Phase 4: Formal report/draft (full mode)
├── agent5-review_ledger.json  ← Phase 5: Content quality audit + PASS/WARN/FAIL
├── agent6-final.md            ← Phase 6: Final version (full mode)
└── revision_log.json          ← Phase 6: Revision log
```

**task_id format:** `DI-YYYYMMDD-seq`

**The main session does NOT transmit data — it only handles spawn + gate + file verification.** Same file-based handoff protocol as DR.

**Entropy constraint (mandatory):** File verification checks existence only. Detailed Agent outputs are not loaded into main session context. Draft phase must spawn isolated sub-sessions.

---

## Detailed Agent Specifications

---

### Agent 0: Scope (Issue Scoping)

**Input:** User-provided case facts
**Output:** `agent0-scope.json`

**Output structure:**
- `case_summary` — Subject, behavior, amount, time span
- `legal_framework` — Applicable regulation list (no article numbers needed) + key legal issues
- `evidence_assessment` — Available evidence + missing evidence + strategic direction
- `interview_strategy_framework` — Strategic direction if interview outline mode
- `risk_assessment` — Key points of contention and risks
- `task_type` — Determined task type (case_qualification / interview_outline / legal_consultation)
- `downstream_handoff` — Search keyword suggestions for Agent 1 + analysis direction for Agent 3

```json
{
  "task_id": "DI-YYYYMMDD-xxx",
  "task_type": "case_qualification | interview_outline | legal_consultation",
  "case_summary": {
    "subject": "Personnel identity",
    "behavior": "Behavior description",
    "amount": "Amount involved",
    "time_span": "Time span"
  },
  "legal_framework": {
    "applicable_laws": ["List of applicable regulation names"],
    "key_legal_questions": ["Key legal questions"]
  },
  "evidence_assessment": {
    "available": ["Available evidence"],
    "missing": ["Missing evidence"],
    "strategy": "Evidence collection strategy direction"
  },
  "interview_strategy_framework": "Strategic direction if interview outline mode",
  "risk_assessment": "Key points of contention and risks",
  "downstream_handoff": {
    "agent1_search_terms": ["Search keywords"],
    "agent3_analysis_direction": "Analysis direction"
  }
}
```

## ⚠️ Output rules
Write output to file. Final reply must be exactly one line: `DONE <output_file_path>`.
Do not restate file content or write summaries. The main session will read the file itself.

---

### Agent 1: Search — 🔴 v1.5 Parallel Architecture

**Architecture:** Agent 0 `regulation_list` → (Agent 1a ∥ Agent 1b) → Agent 1c Merge

**Agent 1a (search-rg):** Input `agent0-scope.json` → Output `agent1a-search-rg.json`
- Full-text rg search of regulation library (article text + source_line)
- See `agents/search-rg.md` for details

**Agent 1b (search-pkulaw):** Input `agent0-scope.json` (regulation_list) → Output `agent1b-search-pkulaw.json`
- pkulaw version verification (currently effective / amended / repealed)
- See `agents/search-pkulaw.md` for details
- **Parallel execution:** 1a and 1b have no mutual dependencies, started simultaneously

---

### Agent 1c: Merge (Regulation Search Merge · v1.5 New) 🔀

**Input:** `agent0-scope.json` + `agent1a-search-rg.json` + `agent1b-search-pkulaw.json`
**Output:** `agent1-merged.json`

**Core responsibility:** Using Agent 0's `regulation_list` as baseline, merge 1a (article text) and 1b (version records) into a unified format for Agent 2 consumption.

**Merge rules:**
- Three-way matching per regulation (rg hit + pkulaw verification status)
- Discrepancy markers: rg hit but pkulaw unverified → UNVERIFIED; rg miss but pkulaw has record → search_miss
- Does not modify 1a/1b outputs, only merges + tags
- See `agents/merge.md` for details

---

### Agent 2: Audit (Regulation Citation Audit)

**Input:** `agent0-scope.json` + `agent1-merged.json` (1c merge output)
> 🔴 v1.5: Input changed from dual-source (agent1a + agent1b) to single-source (agent1-merged)
**Output:** `agent2-audit.json`

**Audit checklist:**
1. **Article number original text verification** — Cross-reference each cited regulation article against original text (using ripgrep secondary confirmation)
2. **`[UNCERTAIN]` block check** (P-001 reused for DI):
   - Scan agent1a-search-rg.json + agent1b-search-pkulaw.json for `[UNCERTAIN]` markers
   - Data items with `[UNCERTAIN]` → moved to `unsourced_claims` array
   - If any `guiding_cases` or critical data item contains `[UNCERTAIN]` → mark `BLOCK_DOWNSTREAM: <data_item>` in conclusion
   - **Agent 3 (Analyze) is PROHIBITED from using `unsourced_claims` data items as quantitative calculation parameters**
3. **Subject-Behavior-Result three-element verification** — Each cited article checked for:
   ✅ Subject element: Does the person fall within the article's applicable scope?
   ✅ Behavior element: Does the article's described behavior match the case behavior?
   ✅ Result element: Is the sanction/penalty within feasible range for this case?
   Articles missing any of the three elements are downgraded and tagged as "reference only."
4. **Version consistency** — All legal citations use the most current version
5. **Amount threshold accuracy** — Criminal prosecution thresholds, party discipline sanction corresponding amounts correctly verified
6. **Case source completeness** — Guiding cases annotated with batch, number, issuing authority

**Conclusion: PASS / PASS_WITH_WARNINGS / FAIL**

```json
{
  "audit_conclusion": "PASS | PASS_WITH_WARNINGS | FAIL",
  "checks": [
    {
      "type": "Article verification",
      "regulation": "Regulation + article",
      "matched": true,
      "verified_text": "Original text",
      "source": "Path"
    }
  ],
  "version_issues": [
    {
      "regulation": "Regulation name",
      "used_version": "Version used",
      "current_version": "Current latest version"
    }
  ],
  "unsourced_claims": [],
  "block_report": {
    "blocked_items": ["List of blocked data items"],
    "downstream_blocked": true
  },
  "issues": [
    {
      "severity": "critical | high | medium | low",
      "description": "Issue description",
      "fix": "Fix recommendation"
    }
  ]
}
```

**On FAIL → block pipeline, return issues to Agent 1 for correction, then re-run Audit.**

## ⚠️ Output rules
Write output to file. Final reply must be exactly one line: `DONE <output_file_path>`.

---

### Agent 3: Analyze (Deep Analysis · v2.3 Dual-Round Adversarial Debate + Case Matching)

**Input:** `agent0-scope.json` + `agent1-merged.json` + `agent2-audit.json`
**Output:** `agent3-analyze.json` (full mode) / `agent4-draft.md` (interview mode — writes outline directly)

> 🔴 v2.3: Dual-round adversarial debate protocol — Round 1 Prosecution analysis + Round 2 Defense challenge (3 rebuttal point matrix).
> 🔴 v2.3: Case matching — rule-based matching using structured tags from `references/case-index.json`.
> v1.5: Input changed from dual-source to single-source (agent1-merged).

**Analysis methodology: Violation + Responsibility Two-Factor Analysis Framework v2.3**

> Methodology source: `wiki/main/sources/discipline/methodology/violation-responsibility-two-factor-analysis-methodology.md`
> Embedded from Central Commission for Discipline Inspection enforcement guidance case methodology.

```
┌───────────────────────────────────────────────────────────┐
│          Violation + Responsibility Two-Factor Framework   │
│                                                           │
│ Factor 1: Violation (Objective Conduct Elements)          │
│ ├─ Conduct Facts: What action did the subject take?       │
│ ├─ Legal Basis: Which party discipline/regulatory         │
│ │   articles were violated?                               │
│ ├─ Protected Interest Harm: Which disciplinary/legal      │
│ │   interests were harmed?                                │
│ ├─ Conduct Continuity: One-time/occasional vs.            │
│ │   systematic/persistent?                                │
│ └─ Severity: Amount · Frequency · Scope · Social impact   │
│                                                           │
│ Factor 2: Responsibility (Subjective Attribution          │
│            Elements)                                      │
│ ├─ Mental State: Intentional/negligent? Direct/indirect?  │
│ ├─ Awareness Level: Knowingly violating? Reasonably       │
│ │   expected to know?                                     │
│ ├─ Motive: Personal gain / organizational interest /      │
│ │   external pressure?                                    │
│ ├─ Self-correction: Voluntary cessation · self-report ·   │
│ │   voluntary restitution?                                │
│ └─ Identity Awareness: Understanding of party member /    │
│    public official duties?                                │
│                                                           │
│ Comprehensive Judgment = Violation (nature·degree) ×      │
│                           Responsibility (gravity)        │
│ ├─ Violation established + Responsibility established →   │
│ │   Disciplinary/legal violation established              │
│ ├─ Violation established + Responsibility not established→│
│ │   Does not constitute disciplinary violation            │
│ └─ Violation ∧ Responsibility → Sanction grade =          │
│    f(violation_degree, responsibility_degree)             │
└───────────────────────────────────────────────────────────┘
```

**Full mode analysis dimensions:**
- Violation factor analysis (objective conduct → corresponding articles → severity assessment)
- Responsibility factor analysis (mental state → motive → post-behavior attitude → identity overlay)
- Comprehensive sanction recommendation (violation degree × responsibility degree → sanction range)
- Comparative case reference (violation/responsibility determination pathways in guiding cases)
- Evidence chain completeness assessment (which violation/responsibility elements have evidence support, which rely on confessions)

**Every cited regulation must include an `[Applicability Argument]` field.**

**🔴 Fact premise declaration (premise_declaration) — Big Oversight Mandatory (Step 0b):**

Agent 3 must explicitly declare the **3 strongest premise assumptions** (the most easily taken-for-granted ones) that its analysis depends on, and execute rg tool verification for each. This is the structured implementation of Step 0b fact gate in Agent 3.

**Filling rules:**
1. **Premise 1 (mandatory): Subject's regulatory identity classification** — Explicitly state whether the subject is a "public official," "CCP member," "public institution staff," "regular employee," or other category, with rg verification source (search wiki for regulatory text on subject element requirements)
2. **Premises 2-3 (mandatory): The 2 most critical factual assumptions in the analysis reasoning** — Each with rg/web_search verification source
3. **sensitivity field**: Describe how conclusions would change if any premise proves false

**🔴 Counter argument — Preventing confirmation bias:**

Agent 3 must construct the strongest opposing viewpoint and rebut each point. This is a structured safeguard against one-sided reasoning bias.

**Filling rules:**
1. **strongest_opposing_view**: The strongest exculpatory/mitigation argument favorable to the subject (do not weaken — write in strongest form)
2. **why_this_view_is_rejected**: Specific reasons the argument is dismissed (cite regulations + facts)
3. **residual_uncertainty**: Remaining uncertainty even after dismissal

```json
{
  "analysis": {
    "violation_factor": {
      "behavior_description": "Objective description of subject's conduct",
      "applicable_regulations": [
        {
          "law": "Regulation name",
          "article": "Article number",
          "violation_type": "Type of violation",
          "applicability_argument": "[Applicability argument]"
        }
      ],
      "protected_interests": "Disciplinary/legal interests harmed",
      "continuity": "One-time/occasional/persistent/systematic",
      "severity": {
        "amount": "Amount involved",
        "frequency": "Frequency",
        "scope": "Scope of impact",
        "consequence": "Social consequences"
      }
    },
    "responsibility_factor": {
      "subjective_state": "Direct intent/indirect intent/negligence",
      "knowledge_level": "Knowing/should have known/could not reasonably be expected to know",
      "motive": "Personal gain/organizational interest/external pressure/other",
      "post_behavior": "Voluntary correction and restitution/passive/resistant and uncooperative",
      "identity_weight": "Impact of party member/public official identity on duty of care"
    },
    "comprehensive_assessment": {
      "violation_established": true,
      "responsibility_established": true,
      "penalty_range": "Sanction grade range",
      "aggravating_factors": ["Aggravating factors"],
      "mitigating_factors": ["Mitigating factors"],
      "recommended_disposition": "Recommended sanction grade"
    }
  },
  "premise_declaration": {
    "assumptions": [
      "Premise 1 (identity): Subject's regulatory identity is ______ [Source: rg verification: ______]",
      "Premise 2: ______ [Source: rg verification: ______]",
      "Premise 3: ______ [Source: rg verification: ______]"
    ],
    "sensitivity": "How conclusions change if premises are invalid"
  },
  "counter_argument": {
    "strongest_opposing_view": "Strongest exculpatory argument",
    "why_this_view_is_rejected": "Reasons for rejection",
    "residual_uncertainty": "Remaining uncertainty"
  },
  "case_references": [
    {
      "case_id": "Case number",
      "similarity": "Similarity level",
      "reference_value": "Reference value"
    }
  ],
  "evidence_chain": [
    {
      "element": "Violation/responsibility element",
      "evidence": ["Supporting evidence"],
      "gap": "Relies on confession / has evidence"
    }
  ],
  "unsourced_claims": 0,
  "confidence": "high | medium | low"
}
```

## ⚠️ Output rules
Write output to file. Final reply must be exactly one line: `DONE <output_file_path>`.

⏸️ **STOP_FOR_REVIEW**
Present analysis phase output summary to domain owner (Top 5 audit findings + risk ranking + preliminary conclusion), wait for reply.
- Domain owner replies "continue" or 15-minute timeout → proceed to Draft with current priority
- Domain owner adjusts priority → reorder based on feedback, then proceed to Draft

---

### Agent 4: Draft (Write Report/Outline) — Full Mode

**Input:** `agent0-scope.json` + `agent3-analyze.json` (+ agent2-audit.json)
**Output:** `agent4-draft.md`

**Report structure (adjusted by task_type):**
- I. Case characterization framework (behavior nature + legal applicability table)
- II. Evidence analysis (assessment + strategy)
- III. Sanction recommendation / Interview strategy + question script + contingency plan
- IV. Action recommendation (by scenario tier)
- 🔒 G4.5 Execution signature

## ⚠️ Output rules
Write output to file. Final reply must be exactly one line: `DONE <output_file_path>`.

---

### Agent 5: Review (Content Quality Audit · Twenty-Four-Character Policy 6-Dimension Scoring Matrix) — Full Mode

**Input:** `agent4-draft.md` + `agent1a-search-rg.json + agent1b-search-pkulaw.json`
**Output:** `agent5-review_ledger.json`

**Design source:** The discipline inspection case adjudication "Twenty-Four-Character Policy" — Facts clear · Evidence conclusive · Characterization accurate · Sanction appropriate · Procedures complete · Process compliant.

**Scoring matrix (6 dimensions × weights):**

| # | Dimension | Weight | Role | Check Content |
|:-:|:----------|:------:|:----|:--------------|
| 1 | **Characterization Accuracy** | **25%** | Core | Regulation citations complete? Original text verbatim? Three-element match? Violation+Responsibility two-factor complete? |
| 2 | **Facts Clear** | **20%** | Premise | Conduct chain complete? Time/space/amount/frequency/means/purpose connections clear? |
| 3 | **Evidence Conclusive** | **20%** | Support | Available + missing evidence inventory complete? Circumstantial evidence chain path feasible? |
| 4 | **Sanction Appropriate** | **15%** | Output | Sanction recommendation matches regulations and facts? Scenario matrix adequate? Adversarial argument sufficient? |
| 5 | **Procedures Complete** | **10%** | Safeguard | Interview procedures standardized? Rights and obligations notification? All stages complete? |
| 6 | **Process Compliant** | **10%** | Baseline | Interview strategy complies with legal procedure? Breakthrough points within authority? Evidence collection path lawful? |
| **Total** | | **100%** | | |

**Scoring standards:**
- Total score ≥ 80 → PASS (skip Phase 6)
- Total score 60–79 → REVISE (enter Phase 6)
- Total score < 60 → REJECT (return to Agent 4 for rewrite, max 2 rounds, excess → HUMAN_ESCALATION)

**Downgrade rules:**
- Characterization Accuracy < 50 → Mandatory REVISE
- Facts Clear < 40 → Mandatory REVISE
- Evidence Conclusive < 40 → Mandatory REVISE

```json
{
  "review_score": 0,
  "verdict": "PASS | REVISE | REJECT",
  "score_breakdown": {
    "1_characterization_accuracy": {
      "score": 0,
      "weight": 25,
      "weighted": 0
    },
    "2_facts_clear": {
      "score": 0,
      "weight": 20,
      "weighted": 0
    },
    "3_evidence_conclusive": {
      "score": 0,
      "weight": 20,
      "weighted": 0
    },
    "4_sanction_appropriate": {
      "score": 0,
      "weight": 15,
      "weighted": 0
    },
    "5_procedures_complete": {
      "score": 0,
      "weight": 10,
      "weighted": 0
    },
    "6_process_compliant": {
      "score": 0,
      "weight": 10,
      "weighted": 0
    }
  },
  "downgrade_triggers": [],
  "issues": [
    {
      "severity": "critical | high | medium | low",
      "dimension": "1-6",
      "description": "Issue description",
      "fix": "Fix recommendation"
    }
  ],
  "must_fix": [],
  "sourced_claims": 0,
  "unsourced_claims": 0
}
```

## ⚠️ Output rules
Write output to file. Final reply must be exactly one line: `DONE <output_file_path>`.

---

### Agent 6: Revise (Fix) — Full Mode

**Input:** `agent4-draft.md` + `agent5-review_ledger.json`
**Output:** `agent6-final.md` + `revision_log.json`

Fix each item in Review's `must_fix` list. Record each fix in `revision_log.json`.

**After fixes complete → Optional secondary Review verification (if original score < 70).**

## ⚠️ Output rules
Write output to file. Final reply must be exactly one line: `DONE <output_file_path>`.

---

### Phase 7: Publish (IMA Upload)

**Called directly from main session, no sub-agent spawn:**

```bash
node skills/solo-file-transfer/scripts/ima-upload.cjs <final_file> <KB_ID>
```

- Full mode: agent6-final.md
- Interview mode: agent4-draft.md
- Quick mode: agent2-audit.json (audit-verified search results)

**⛔ Report purity principle:**
- Reports uploaded to IMA must contain **pure analysis content only** — no pipeline IDs / Agent identifiers / audit declaration JSON / VERIFIED lists or other metadata
- Metadata written to separate trace files in `memory/inspection-drafts/<case>/` directory
- Report contains only: title, date, executive summary, analysis body, regulation citations (with article numbers + original text)

**Common KB_IDs:** See MEMORY.md → IMA knowledge base section.

---

## Anonymization Protocol

Organization names in sub-agent prompts use anonymized placeholders:
- Institutions: "A tertiary hospital" / "A provincial hospital"
- Specific sensitive data is not written directly into prompts — reference Agent 0 scope file path instead

---

## Regulation Knowledge Base (Pluggable Provider Architecture 🔌 v1.4.0)

> The regulation data layer is decoupled from the pipeline via the Provider interface. See `providers/regulation-source.interface.md`.

### Provider Auto-Detection

Pipeline startup selects knowledge source in the following priority:
1. `WIKI_PATH` environment variable exists → wiki-provider (45+ full regulations)
2. `pkulaw-mcp` available → overlays pkulaw-provider (version verification)
3. Neither available → default-provider (3 core regulation demo)

### Available Providers

| Provider | Regulation Search | Version Verification | Case Search | Use Case |
|:---------|:-----------------:|:-------------------:|:-----------:|:---------|
| **default-provider** | 3 core | ❌ | ❌ | Open-source users, out-of-box |
| **wiki-provider** | 45+ full text | ❌ | 11 cases | Organizations with WIKI library |
| **pkulaw-provider** | ✅ | ✅ | ❌ | Subscribers to pkulaw |

### Degradation Behavior

- No wiki-provider → default-provider fallback, output marked `⚠️ Only 3 core regulations`
- No pkulaw-provider → Agent 1b degraded output `VERSION_UNVERIFIED`, pipeline not blocked
- No knowledge source at all → Pipeline refuses to start

### Regulation Inventory

**Discipline regulations** (`${WIKI_PATH}/discipline/regulations/`, 45 total):
- CCP Disciplinary Action Regulation_2023 Revision
- PRC Supervision Law_2024 Amendment
- Supervision Law Implementation Regulations_2025 Revision
- Supervision and Enforcement Work Rules_2019
- Public Institution Staff Disciplinary Action Provisions_2023
- PRC Public Officials Government Affairs Disciplinary Law_2020.6.20
- PRC Criminal Law (per Amendment XI Revision, 2020)
- CCP Accountability Regulation_2019 Revision
- Other regulations — 45 total

**Healthcare conduct standards** (`${WIKI_PATH}/medical/`, 8 total):
- Code of Conduct for Healthcare Institution Practitioners
- Nine Standards for Healthcare Institution Staff Integrity and Honest Practice
- Medical Professional Ethics Standards_2025 Edition
- PRC Physicians Law
- PRC Basic Healthcare and Health Promotion Law
- PRC Pharmaceutical Administration Law
- Negative Behavior List for Medical Professional Internet Health Science Communication
- Pharmaceutical Representative Management Measures_2026

**Guiding cases** (`${WIKI_PATH}/discipline/guiding-cases/`, 11 total):
- Case - Official vehicle private use / private vehicle public expense
- Case - Fault tolerance and error correction - Two-factor analysis
- Case - Resisting organizational investigation - Two-factor analysis
- Case - Formalism and bureaucracy
- Case - Embezzlement via blank official letters
- Case - Mixed public-private in irregular dining
- Case - Unauthorized apportionment
- Case - Improperly handling wedding/funeral events
- Case - Improperly accepting banquets after retirement
- Case - Simplified and generalized accountability
- Case - Fraudulently obtaining welfare subsidies

**Analysis methodology:**
- `${WIKI_PATH}/discipline/methodology/violation-responsibility-two-factor-analysis-methodology.md`

---

## LEARNED PATTERNS

### v2.0.0 — Dual-Round Adversarial Debate + Structured Case Indexing (2026-07-17)
**Source:** SOLO 655 Assessment — 3 out of 12 LEARNED PATTERNS were cognitive blind spots (single-person self-debate is unreliable); the current 11 guiding cases cannot be precisely referenced via keyword matching alone.
**Core design:**

**1. Dual-Round Adversarial Debate (Agent 3):**
- Round 1 (Prosecution): Standard analysis → produce violation + responsibility + sanction recommendation
- Round 2 (Defense): Role switch, find 3 strongest rebuttal points → argue each for validity
- rebuttal_matrix: Rebuttal point + strength (strong/medium/weak) + validity (valid/partially_valid/overturned) + reason + impact on conclusion
- REBUTTAL_PASS standard: All 3 points argued + at least 1 VALID or PARTIALLY_VALID
- Historical interception capability: Could intercept similar errors as DI-20260716-001 (fabricated articles) and DI-20260706-001 (absolutist phrasing)

**2. Structured Case Indexing:**
- Created `references/case-index.json`: 11 guiding cases × 7 dimensional feature tags
- Matching dimensions: violation_type · violation_category · subject.level · amount.range · mental_state · penalty_severity
- Pure rule-based matching (no semantic model needed): 2+ dimension overlap → 70% similarity
- Agent 3 builds case_profile after analysis, auto-matches Top 3 cases

**3. Evidence Scoring Proposal Removed:**
- SOLO 655 review conclusion: Dual-round adversarial debate already covers the core value of evidence scoring (defense rebuttals naturally expose evidence weaknesses)
- 5-star scoring carries pseudo-precision risk (humility is paramount); adversarial debate's "specific weakness + reason" is more precise than scores

**Principle:** Use structured "perspective-shifting" to combat cognitive blind spots, rather than stacking new Agents. Dual-round system = same Agent runs two rounds, consistent with compression principle.
**SOLO 655 review:** Bloat trap ✅ — no increase in Agent count, dual-round is a process optimization, not rule stacking. Compression ✅ — debate matrix has fixed format, high information density.
**Files:**
- New: `references/case-index.json` (11-case structured labels)
- Modified: `agents/analyze.md` (dual-round debate + case matching), `agents/draft.md` (seven chapters including case references), `agents/review.md` (+ dual-round debate + case audit items), `agents/search-rg.md` (case feature extraction)
- Modified: `SKILL.md` (v2.0 version number · Agent 3 specification)

### v1.5.0 — Pipeline Parallelization: 0→(1a∥1b)→1c→2 (2026-07-17)
**Source:** SOLO 655 Assessment — 1a and 1b both source input from Agent 0 with no mutual dependency; serial execution was historical design, not a necessity.
**Core design:**
- Agent 0 adds explicit `regulation_list` field, simultaneously supplying 1a (rg search) and 1b (pkulaw verification)
- 1a and 1b execute in parallel; 1c performs lightweight merge (matching + discrepancy tagging, no analysis)
- 1b input changed from agent1a to agent0 — solving the implicit coupling where "if 1a misses a regulation → 1b won't verify it"
- New: `agents/merge.md` (Agent 1c)
- Agent 2 input changed from dual-source to single-source (agent1-merged.json)
- All modes: Agent count +1 (full: 8→9, interview: 5→6, quick: 4→5)
- Effective time: max(rg ~30s, pkulaw ~60s) + merge(10s) = 70s, saving 22% vs serial 90s
**Principle:** Eliminating implicit coupling is better than increasing parallelism — the 1a→1b regulation_list handoff was fragile (1a miss = 1b blind spot); having both read Agent 0 is more robust.
**SOLO 655 review:** Bloat trap ✅ — New Agent 1c is not defensive stacking but structural improvement eliminating implicit coupling. Entropy reduction ✅ — 1c only merges, does not analyze.
**Files:**
- New: `agents/merge.md` (Agent 1c)
- Modified: `agents/scope.md` (added regulation_list), `agents/search-pkulaw.md` (input changed to agent0), `agents/search-rg.md` (reads regulation_list), `agents/audit.md` (input changed to agent1-merged)
- Modified: `SKILL.md` (pipeline diagram · Phase descriptions · Solo Status · output paths · Agent specifications)

### v1.4.0 — Three-Layer Decoupling: Pluggable Provider Architecture for Knowledge Sources (2026-07-17)
**Source:** DI skill was uploaded to GitHub but external users couldn't use it — missing WIKI regulation database and pkulaw-mcp.
**Core design:**
- Regulation data layer decoupled from pipeline via Provider interface
- New `providers/` directory: interface specification + default/wiki/pkulaw three Providers
- Agent 1a/1b de-hardcoded paths, using environment variables `${WIKI_PATH}` / `${SKILL_DIR}`
- Agent 1b added degradation path: when pkulaw unavailable, label all `VERSION_UNVERIFIED` (pipeline not blocked)
- Agent 2 added `degradation_mode` determination: degraded mode PASS → PASS_WITH_WARNINGS
- Default knowledge package: 3 core regulation full texts (Disciplinary Action Regulation + Supervision Law + Government Affairs Disciplinary Law) + methodology documents
- `shared-config.yaml` de-hardcoded, replaced all absolute paths with `${WIKI_PATH}` / `${SKILL_DIR}` env vars
**Principle:** Pipeline methodology is the product, regulation data is the fuel — deliver separately, configure independently.
**Files:**
- New: `providers/` (interface + 3 provider configurations + default knowledge package)
- New: `README.md` (open-source project homepage)
- Modified: `agents/search-rg.md`, `agents/search-pkulaw.md`, `agents/audit.md`
- Modified: `SKILL.md` (Provider architecture documentation), `supervision-shared/shared-config.yaml`

### v1.1.0 — Agent 1a/1b Split: pkulaw Structurally Unskippable (2026-07-16)
**Source:** DI-20260716-001 post-mortem — Root cause analysis of Agent 1 skipping Step 1B. Even with reinforced instruction constraints, rg+pkulaw within a single Agent could still be skipped. Splitting into 1a (rg WIKI) → 1b (pkulaw) as two independent sub-sessions makes 1b structurally independent — impossible for 1a to skip it.
**Changes:**
- New `agents/search-rg.md` (Agent 1a): Focused on rg WIKI search + source_line + regulation_list
- Restructured `agents/search.md` → (Agent 1b): Focused on pkulaw version_verified
- Updated `agents/audit.md`: Gate 1 checks 1b file existence + Gate 2 checks 1a source_line
- SKILL.md pipeline changed from 0→1→2→... to 0→1a→1b→2→...
- All modes: Agent count +1 (full: 7→8, interview: 4→5, quick: 3→4)
**Principle:** Splitting high-risk substeps into independent sub-sessions = structurally unskippable. Efficiency unchanged (pkulaw is the bottleneck; rg serial 30s does not increase total time).

### v1.0.4 — Agent 1/2 Agent File vs SKILL.md Content Gap Fix (2026-07-16)
**Source:** DI-20260716-001 post-mortem. Agent 1 skipped Step 1B (pkulaw-search version verification) and fabricated non-existent Articles 36-37 of the Disciplinary Action Regulation (fabricated article hallucination). Root cause: agents/search.md and agents/audit.md were slimmed-down versions of SKILL.md, missing key enforcement constraints such as Step 1B mandatory instruction, article number anti-hallucination rules, and pre-gate checks.
**Fix:**
- agents/search.md: Added Step 1B pkulaw-search mandatory execution section (including command + required version_verified fields), Step 1A provincial regulations, article number anti-hallucination rules (source_line required), [UNCERTAIN] tagging protocol
- agents/audit.md: Added pre-gates (Gate 1: Step 1B existence check → immediate FAIL / Gate 2: source_line completeness → UNSOURCED count → threshold FAIL), HALLUCINATION detection rules, [UNCERTAIN] block check
**Principle:** Agent files must NOT be "slimmed-down" versions of SKILL.md — enforcement constraints in SKILL.md must be structurally implemented as structured checks in each agent file. Slimming = removing guardrails.

### v1.0.1 — Independent Separation from DI v3.0.2 (2026-06-08)
**Source:** Split from original discipline-inspect v3.0.2. Discipline inspection and inspection tour supervision methodologies were incompatible (violation+responsibility vs political examination); wiki data layers already independent (discipline/ vs inspection/); DI-20260603-inspection-tour already independently verified.
**Core inheritance:**
- 8-stage pipeline + DR isomorphic architecture ✓
- Guardrail Routing (full/interview/quick) ✓
- Violation + Responsibility two-factor analysis framework ✓
- Twenty-Four-Character Policy 6-dimension scoring matrix ✓
- File existence verification + output path protocol ✓
- Anonymization protocol ✓

### v1.0.1 — Quick Mode Must Include Audit (2026-07-06)
**Source:** Corrected: quick mode (regulation consultation/article lookup) must not skip Agent 2 Audit.
All cited regulation articles must undergo ripgrep original text comparison verification before entering Publish phase.
**Changes:** quick mode pipeline corrected from `0→1→7` to `0→1→2→7`.
**Removed items:**
- Inspection Work Regulation removed from core regulation list (now belongs to supervision-inspection)
- Inspection tour wiki paths removed from Agent 1 search scope
- inspect-tour mode removed from Guardrail routing

### v1.0.2 — Sanction Approval Classification Analysis Principle (2026-07-06)
**Source:** Corrected — DI-20260706-001 analysis stated "all party disciplinary sanctions must go through party committee" — imprecise. Warning/severe warning can be approved by the discipline inspection commission at the same level (per Article 6 of Approval Authority and Procedures Regulations), not necessarily the party committee.
**Lesson:** For sanction approval procedure questions, must analyze by **light sanctions (warning/severe warning) vs heavy sanctions (removal from party post and above)** across two dimensions.
**Cross-verification requirement:** For approval procedure questions, must **simultaneously** search the following two regulations and cross-reference:
  - Regulations on Approval Authority and Procedures for Disciplining Party Members (2022) → Approval authority division
  - Supervision and Enforcement Work Rules (2019) → Collective discussion format
**Output standard:** 'Collective discussion decision' ≠ 'party committee meeting' — must distinguish between "discipline inspection commission standing committee collective discussion" and "party committee collective discussion" applicable scenarios.
**Absolute statement check:** Any use of absolute terms ("must/should/all/always") requires self-check: are there exceptions? If so, annotate exception conditions.

### Inherited Lessons from DI

**Subject-Behavior-Result three-element verification (2026-05-28):**
Each cited article must be checked for subject element, behavior element, and result element. Articles missing any element are downgraded and tagged as "reference only."

**File existence verification (2026-05-27):**
After each Agent completes, the main session reads and verifies file existence. If not found, mark as failed.

**Suit hard enforcement:**
Keywords such as discipline inspection / case characterization / interview outline → Step 1: display confirmation prompt → domain owner confirms → sessions_spawn Agent 0.

### v1.4.0 — Quick Mode Three Gates (2026-07-17)
**Source:** SOLO 655 post-mortem on a quick analysis case — pipeline execution rate 1/8, version verification + counter-argument + identity-path audit all skipped.
**Root cause:** DI has only two modes: full pipeline (heavy) or manual (no gates). No intermediate "gated quick mode".
**Solution:** Even when not running the full pipeline, these three checks are MANDATORY before any qualitative conclusion:

| Gate | Trigger | Block |
|:-----|:--------|:------|
| **G-VERSION** | Before citing regulation articles | pkulaw verification required; if skipped → tag `[VERSION_UNVERIFIED]` in output |
| **G-COUNTER** | Before outputting any qualitative conclusion | Must write `strongest_opposing_view` + `why_rejected`; if not → block conclusion output |
| **G-IDENTITY** | Before recommending sanction level | Must verify: subject identity → applicable regulation → sanction path; all three must align |

**These three gates must be passed before any qualitative conclusion or sanction recommendation can be output.**

### v1.0.3 — Agent 0 Step 0b Fact Prerequisite Verification Enforcement (2026-07-08)
**Source:** DI-20260708-001 post-mortem — Agent 0 did not execute rg verification, incorrectly classified a medical professional as "public official" — violating source traceability and humility principles, high confidence error.
**Changes:** agents/scope.md enhanced with Step 0b mandatory execution protocol (self-check, require tool call records, rg verification before any fact assertion about subject identity).
**Lesson:** This is not a technology issue but an architectural one — Step 0b in AGENTS.md was only a "one-time stated rule" rather than a structural constraint built into each scope.md session.
**Verification:** Same pattern errors in identity classification cannot be prevented without structural enforcement.
