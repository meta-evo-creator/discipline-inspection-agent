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
> 🔓 Open source under MIT License.

> 📎 Shared config: `skills/supervision-shared/shared-config.yaml` · Agent files: `agents/*.md` · Case index: `references/case-index.json`

---

## 🛡️ No-Authority Boundary

This skill is a **refs-only / no-authority** capability package.

**Outputs:** violation_finding_ref · evidence_chain_ref · article_match_ref · responsibility_assessment_ref · sanction_recommendation_ref · mitigating_aggravation_ref · owner_gate_handoff_ref

**This skill NEVER produces:** Final sanction decisions · Accountability conclusions · Organizational action decisions · Final case characterization · Any output substituting for committee meetings or statutory procedures.

> Boundary corresponds to SOLO 655 Iron Rule ④ (minimal agency — every authorization is temporary, scoped, and revocable).

---

## ⛔ Entry Block (Cannot Skip · Cannot Degrade)

**Sole entry point:** Suit Phase 1 Confirmation → `sessions_spawn Agent 0 (scope)`.

The following are recorded as `[UNSOURCED-EXECUTION]`:
- Searching regulations / writing analysis / drafting reports in the main session
- Citing regulation article numbers from memory
- Skipping any Agent on grounds of "simple case"

**This clause is not degradable under any circumstances.**

---

## 📋 Pipeline

### Phase → Ref Mapping

| Phase | Agent | Output | Ref Family |
|:------|:------|:-------|:-----------|
| 0 | Scope | `agent0-scope.json` | `source_pack_ref` |
| 1a ∥ 1b | Search-rg ∥ Search-pkulaw | json | `article_match_ref` ∥ `version_verified_ref` |
| 1c | Merge | `agent1-merged.json` | `merged_search_ref` |
| 2 | Audit | `agent2-audit.json` | `evidence_chain_ref` |
| 3 | Analyze | `agent3-analyze.json` | violation + responsibility + sanction refs |
| 4 | Draft | `agent4-draft.md` | Synthesis of upstream refs |
| 5 | Review | `agent5-review_ledger.json` | Scoring matrix + fixes |
| 6 | Revise | `agent6-final.md` | Corrected final |
| 7 | Publish | → IMA upload | `owner_gate_handoff_ref` |

### Pipeline Diagram

```
Agent 0 ─┬─→ Agent 1a (rg WIKI) ─┐
         └─→ Agent 1b (pkulaw)  ─┤ ∥ parallel
                                 ↓
                          Agent 1c (merge)
                                 ↓
                          Agent 2 (audit)
                                 ↓
                          Agent 3 (analyze)
                                 ↓
                          Agent 4 (draft)
                                 ↓
                          Agent 5 (review)
                                 ↓
                          Agent 6 (revise)
                                 ↓
                          Agent 7 (publish → IMA)
```

**Each Agent runs in isolated session (context:isolated, lightContext:true). Main session only handles spawn + gate + file existence verification.**

### Guardrail Routing

| Mode | Trigger | Pipeline | Agents |
|:-----|:--------|:---------|:------:|
| **full** | Case characterization, sanction recommendation | 0→(1a∥1b)→1c→2→3→4→5→6→7 | 8+1 |
| **interview** | Interview outline | 0→(1a∥1b)→1c→2→3+4→7 | 5+1 |
| **quick** | Regulatory consultation, article lookup | 0→(1a∥1b)→1c→2→7 | 4+1 |

**Routing decision:** After Agent 0 completes, select mode based on `task_type`.

---

## 🔒 Protocol

### File Verification (Mandatory)
After each Agent completes: `read <output> → exists + size > 0`. File not found → mark `failed` → do NOT proceed → report to domain owner. File exists → record path only + ≤3 line summary → proceed.

**⛔ Only verify existence — do NOT read content into main session context.**

### Solo Status Protocol
Before/after each Agent spawn, update `./solo/pipeline-status.json` with pipeline_id + phase status (structure defined in `skills/solo/SKILL.md`).

### Output Path Protocol
```
{pipeline_output_dir}/
├── agent0-scope.json          ← Phase 0: scoping + regulation_list
├── agent1a-search-rg.json     ← Phase 1a: rg WIKI (includes source_line)
├── agent1b-search-pkulaw.json ← Phase 1b: pkulaw version verify ∥
├── agent1-merged.json         ← Phase 1c: merge (match + discrepancy tags)
├── agent2-audit.json          ← Phase 2: citation audit
├── agent3-analyze.json        ← Phase 3: deep analysis
├── agent4-draft.md            ← Phase 4: report/outline
├── agent5-review_ledger.json  ← Phase 5: quality audit
├── agent6-final.md            ← Phase 6: final version
└── revision_log.json          ← Phase 6: revision log
```
**task_id format:** `DI-YYYYMMDD-seq`

---

## Agent Specifications

### Agent 0: Scope (Issue Scoping)
**Input:** User-provided case facts
**Output:** `agent0-scope.json` — case_summary · legal_framework · evidence_assessment · task_type · downstream_handoff · regulation_list (parallel pipeline key field)
**Agent file:** `agents/scope.md` (includes Step 0b identity verification + identity→regulation mapping)

### Agent 1: Search (Parallel Architecture)
**Architecture:** Agent 0 `regulation_list` → (1a ∥ 1b) simultaneously
- **1a (search-rg):** Full-text rg search of regulation library → `agent1a-search-rg.json`. See `agents/search-rg.md`.
- **1b (search-pkulaw):** pkulaw version verification → `agent1b-search-pkulaw.json`. See `agents/search-pkulaw.md`.

### Agent 1c: Merge (Inline)
**Input:** agent0-scope.json + agent1a + agent1b
**Output:** `agent1-merged.json` — three-way match per regulation (rg hit + pkulaw status) with discrepancy markers (UNVERIFIED / search_miss). No standalone agent file; merge logic is embedded in pipeline flow.

### Agent 2: Audit (Regulation Citation Audit)
**Input:** agent0-scope.json + agent1-merged.json
**Output:** `agent2-audit.json` — article number verification · [UNCERTAIN] block check · Subject-Behavior-Result three-element verification · version consistency · conclusion: PASS / PASS_WITH_WARNINGS / FAIL
**Agent file:** `agents/audit.md`

### Agent 3: Analyze (Deep Analysis · v2.3)
**Input:** agent0-scope.json + agent1-merged.json + agent2-audit.json
**Output:** `agent3-analyze.json` — P1 conceptual framework → violation+responsibility two-factor analysis (11-step workflow with embedded M2-M9 modules) → dual-round adversarial debate → case matching → P2 procedural guidance
**Agent file:** `agents/analyze.md` (includes full P1+P2 framework, 11-step workflow, YAML output template, medical case specialty)

### Agent 4: Draft (Report Writing)
**Input:** agent0-scope.json + agent3-analyze.json
**Output:** `agent4-draft.md` — seven-chapter report with interview outline guardrails (criminal transition warning + regulation cross-reference + signature subject three-layer distinction)
**Agent file:** `agents/draft.md`

### Agent 5: Review (Quality Audit)
**Input:** agent4-draft.md + agent1a + agent1b
**Output:** `agent5-review_ledger.json` — Twenty-Four-Character Policy 6-dimension scoring matrix (25/20/20/15/10/10 weights). ≥80 PASS · 60-79 REVISE · <60 REJECT
**Agent file:** `agents/review.md`

### Agent 6: Revise (Fix)
**Input:** agent4-draft.md + agent5-review_ledger.json
**Output:** `agent6-final.md` + `revision_log.json`
**Agent file:** `agents/revise.md`

### Agent 7: Publish (IMA Upload)
Called directly from main session: `node skills/solo-file-transfer/scripts/ima-upload.cjs <final_file> <KB_ID>`

⛔ **Report purity:** IMA upload = pure analysis content only. No pipeline IDs / Agent identifiers / audit metadata. Metadata → `memory/inspection-drafts/<case>/`.

---

## Anonymization Protocol
Organization names use anonymized placeholders ("A tertiary hospital" / "A provincial hospital"). Sensitive data → reference Agent 0 scope file path, not written directly into prompts.

---

## Regulation Knowledge Base (Pluggable Provider Architecture)

Pipeline startup selects knowledge source by priority:
1. `WIKI_PATH` env → wiki-provider (full regulations)
2. `pkulaw-mcp` available → overlays pkulaw-provider (version verification)
3. Neither → default-provider (3 core regulation demo)

| Provider | Search | Version | Cases | Use Case |
|:---------|:------:|:-------:|:-----:|:---------|
| wiki-provider | 45+ full text | ❌ | 11 cases | Organizations with WIKI |
| pkulaw-provider | ✅ | ✅ | ❌ | pkulaw subscribers |
| default-provider | 3 core | ❌ | ❌ | Open-source users |

**Degradation:** No wiki → fallback default (`⚠️ Only 3 core regulations`). No pkulaw → Agent 1b outputs `VERSION_UNVERIFIED` (pipeline not blocked).

> 📚 Full regulation inventory maintained in wiki: `${WIKI_PATH}/discipline/regulations/` (45+ regulations), `${WIKI_PATH}/medical/` (8 healthcare standards), `${WIKI_PATH}/discipline/guiding-cases/` (11 CCDI guiding cases). Auto-updated monthly by regulation-manager cron.

---

## LEARNED PATTERNS

> Architectural methodology changes that shaped the current pipeline structure.
> Historical bug fixes (v1.0.x) are encoded in agent files — see `agents/*.md`.
> Execution-level patterns absorbed from practical cases → injected directly into agent files.

### v1.1.0 — Agent 1a/1b Split: pkulaw Structurally Unskippable
Splitting rg search + pkulaw verification into independent sub-sessions makes version verification structurally unskippable. **Principle:** High-risk substeps as independent sessions = impossible to bypass.

### v1.4.0 — Provider Architecture: Three-Layer Decoupling
Regulation data layer decoupled from pipeline via pluggable Provider interface (default/wiki/pkulaw). **Principle:** Pipeline methodology is the product, regulation data is the fuel — deliver separately, configure independently.

### v1.5.0 — Pipeline Parallelization: 0→(1a∥1b)→1c→2
Agent 0 feeds 1a and 1b simultaneously (no mutual dependency). 1b input changed from agent1a to agent0 — eliminates implicit coupling where "1a miss = 1b blind spot." **Principle:** Eliminating implicit coupling > increasing parallelism.

### v2.0.0 — Dual-Round Adversarial Debate + Structured Case Indexing
Agent 3 runs prosecution round + defense round (3 rebuttal points). Structured case indexing (11 guiding cases × 7 dimensional tags) for rule-based matching. **Principle:** Structured perspective-shifting combats cognitive blind spots; same agent runs two rounds — no new agent overhead.

### v2.3.0 — P1 Policy Framework + P2 Procedural Guidance
P1: 4 conceptual frameworks (三个区分开来 · 由风变腐 · 虚浮辨识 · 透过现象看本质) as analysis backbone before violation determination. P2: 4 procedural rules (Sanction Matching · Asset Disposal · Accountability Pitfalls · Retirement≠Immunity) appended after conclusion. Agent 1c merge logic inlined (no standalone file). **Principle:** Higher-level conceptual framework reduces two-factor analysis blind spots.

> Full changelog with file-level changes → `references/changelog.md`
