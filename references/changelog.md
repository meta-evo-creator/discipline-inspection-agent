# DI SKILL.md Changelog

> Historical version changes. Active architectural patterns → SKILL.md §LEARNED PATTERNS.
> This file preserves the full historical record removed during the 2026-07-18 SKILL.md slimming (848→215 lines).

---

## v2.5.1 — Urgency Routing + KG Writeback + LESSON Agent File + Publish Fix (2026-07-18)

**Key additions over v2.5.0:**
- `urgency` field in LESSON collection — P0 triggers immediate wecom notification (<1 min vs 30-day cron cycle)
- `kg_writeback` field in Agent 3 output — proposals flow via LESSON to `_lessons.json` with `category: "kg"`
- **New file:** `agents/publish.md` — Agent 7 now has its own agent file with Output Schema (was previously main-session steps only)
- Fixed ima upload script path: `ima-upload.cjs` → `ima_upload.cjs` (underscore spelling)
- Pipeline now 10 agents (0→1a∥1b→1c→2→3→4→5→6→7) with all Schema Gates covered

**Files changed:**
- New: `agents/publish.md`
- Modified: `SKILL.md` (agent count update, ima script path fix)
- Modified: `references/changelog.md` (this entry)

**Ecosystem coordination:** Monthly cron Part A now coordinates with weekly cron (`weekly regulation check`). solo-audit v5.6 deepened DI quality dashboard consumption (trend deviation detection).

**Principle:** An evolution ecosystem is not defined by its components — it is defined by the feedback loops between them. v2.5.1 shortens the DI→Cron→DI loop from 30 days to <1 minute for critical lessons, and makes the KG a living graph instead of a static snapshot.

---

## v2.5.0 — Full-Gate Pipeline + Case Ruling Logic + KG + Tuning + WIKI_PATH Guard (2026-07-18)

**Three-case CCDI live-fire validation.** All mechanisms triggered and verified.

**New agent:** `agents/merge.md` — Agent 1c is no longer inline; pipeline now 9/9 agents with Schema Gate.

**All 9 agent files:** Output Schema + Execution Tuning sections.

**SKILL.md:** 8-Agent → 9-Agent pipeline. Gate B schema validation. Pipeline resilience + failure log + resume protocol. Agent 7 expanded: LESSON collection + Quality Dashboard. P1/P2/KG entries consolidated.

**references/case-index.json:** v2.4 with ruling_logic (L1/L2/L3 matching) for all 11 cases.

**agents/scope.md:** Step -1 WIKI_PATH check. Step 4 output template aligned with Schema (REQUIRED/OPTIONAL).

**agents/analyze.md:** KG activation with 1-hop enrichment. `kg_enrichment` required in Schema.

**New files:** `_lessons.json`, `_pipeline_quality_log.json`, `merge.md`.

**Cron updates:** Monthly regulation inspection cron Part C3 semi-automated extraction + C6 health report + Part D _lessons.json sync. SOLO daily audit expanded to 19 checks.

**Live test results:** 3 cases (Case A / Case B / Case C), avg score 88.37, 2 Schema Gate intercepts, 2 pipeline recoveries, 0 uncorrected failures.

---

## v2.4.0 — (merged into v2.5.0; see above)

---

## v1.0.1 — Independent Separation from DI v3.0.2 (2026-06-08)

**Source:** Split from original discipline-inspect v3.0.2. Discipline inspection and inspection tour supervision methodologies were incompatible (violation+responsibility vs political examination); wiki data layers already independent.

**Core inheritance:** 8-stage pipeline + Guardrail Routing + Two-factor analysis + 24-Character Policy scoring matrix + File verification protocol + Anonymization protocol.

**Removed items:** Inspection Work Regulation (→ supervision-inspection), inspection tour wiki paths, inspect-tour mode from Guardrail routing.

---

## v1.0.1 — Quick Mode Must Include Audit (2026-07-06)

Quick mode pipeline corrected from `0→1→7` to `0→1→2→7`. All cited regulation articles must undergo ripgrep original text comparison before Publish.

---

## v1.0.2 — Sanction Approval Classification Analysis Principle (2026-07-06)

**Source:** DI-20260706-001 stated "all party disciplinary sanctions must go through party committee" — imprecise. Warning/severe warning can be approved by the discipline inspection commission at the same level (Article 6 of Approval Authority and Procedures Regulations).

**Lesson:** For approval procedure questions, analyze by light sanctions (warning/severe warning) vs heavy sanctions (removal from party post and above). Cross-verify: Regulations on Approval Authority and Procedures + Supervision and Enforcement Work Rules.

**Absolute statement check:** Any use of absolute terms ("must/should/all/always") requires self-check for exceptions.

---

## v1.0.3 — Agent 0 Step 0b Fact Prerequisite Verification Enforcement (2026-07-08)

**Source:** DI-20260708-001 — Agent 0 did not execute rg verification, incorrectly classified a medical professional as "public official." Step 0b in AGENTS.md was only a "one-time stated rule" — now structurally built into agents/scope.md.

---

## v1.0.4 — Agent 1/2 Agent File vs SKILL.md Content Gap Fix (2026-07-16)

**Source:** DI-20260716-001 — Agent 1 skipped Step 1B (pkulaw version verification) and fabricated non-existent Articles 36-37. Root cause: agents/search.md and agents/audit.md were slimmed-down versions of SKILL.md, missing key enforcement constraints.

**Fix:** agents/search.md: Added Step 1B mandatory execution + article number anti-hallucination rules (source_line required) + [UNCERTAIN] tagging. agents/audit.md: Added pre-gates (Gate 1: Step 1B existence → FAIL / Gate 2: source_line completeness → threshold FAIL) + HALLUCINATION detection.

**Principle:** Agent files must NOT be "slimmed-down" versions of SKILL.md. Slimming = removing guardrails.

---

## Inherited Lessons

### Subject-Behavior-Result three-element verification (2026-05-28)
Each cited article checked for subject element, behavior element, result element. Articles missing any element → downgraded, tagged "reference only."

### File existence verification (2026-05-27)
After each Agent completes, main session verifies file existence. Not found → mark failed.

### Suit hard enforcement
Keywords: discipline inspection / case characterization / interview outline → Step 1: confirmation prompt → domain owner confirms → sessions_spawn Agent 0.

---

## v1.4.0 — Quick Mode Three Gates (2026-07-17)

Even when not running full pipeline, three checks mandatory before any qualitative conclusion:
- **G-VERSION:** pkulaw verification required before citing articles
- **G-COUNTER:** Must write `strongest_opposing_view` + `why_rejected`
- **G-IDENTITY:** Verify: subject identity → applicable regulation → sanction path

---

## v2.3.0 Full Entry — P1+P2 Framework + Inline Merge (2026-07-17)

**Files changed:**
- Modified: `agents/analyze.md` (P1+P2 framework + 11-step workflow + YAML output)
- Deleted: `agents/merge.md` (merge logic inline)
- Modified: `SKILL.md` (v2.3 version number · Agent 3 specification · Agent counts)
- Modified: `README.md` (agent count · directory structure)

## v2.0.0 — Dual-Round Adversarial Debate + Case Indexing

**Files changed:**
- New: `references/case-index.json` (11-case structured labels)
- Modified: `agents/analyze.md` (dual-round debate + case matching), `agents/draft.md`, `agents/review.md`, `agents/search-rg.md`
- Modified: `SKILL.md` (v2.0 version number · Agent 3 specification)

## v1.5.0 — Pipeline Parallelization: 0→(1a∥1b)→1c→2

**Files changed:**
- New: `agents/merge.md` (Agent 1c — later inlined in v2.3.0)
- Modified: `agents/scope.md`, `agents/search-pkulaw.md`, `agents/search-rg.md`, `agents/audit.md`
- Modified: `SKILL.md` (pipeline diagram · Phase descriptions · Solo Status · output paths · Agent specifications)

## v1.4.0 — Provider Architecture

**Files changed:**
- New: `providers/` (interface + 3 provider configs + default knowledge package)
- New: `README.md` (open-source project homepage)
- Modified: `agents/search-rg.md`, `agents/search-pkulaw.md`, `agents/audit.md`
- Modified: `SKILL.md`, `supervision-shared/shared-config.yaml`

## v1.1.0 — 1a/1b Split

**Files changed:**
- New: `agents/search-rg.md` (Agent 1a)
- Restructured: `agents/search.md` → Agent 1b
- Modified: `agents/audit.md`
- Modified: `SKILL.md` (pipeline 0→1→2→... → 0→1a→1b→2→...)
