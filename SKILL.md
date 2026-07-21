---
name: discipline-inspection
version: 2.5.1
description: |
  Discipline Inspection v2.5.1 ⚔️ Methodology v2.3: Dual-Factor + 6 Modules + P1/P2 Framework + 10-Agent Full-Gate Pipeline + Resilience + LESSON(urgency routing) + Quality Dashboard + KG Activation + Agent Tuning + KG Writeback. Focused on party discipline inspection case analysis.
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

# Discipline-Inspection ⚔️ v2.5.1

> **Discipline as the yardstick, vigilance as constant.** 10-Agent Full-Gate Pipeline + Schema Gates (100% coverage) + Pipeline Resilience + LESSON Collection + Quality Dashboard + Knowledge Graph Enrichment + Agent Tuning + Case Ruling Logic (L1/L2/L3).
> 🔓 Open source under MIT License.

> 📎 Shared config: `skills/supervision-shared/shared-config.yaml` · Agent files: `agents/*.md` (10 files, full Gate coverage) · Case index: `references/case-index.json`

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
| 7 | Publish | `agent7-publish-report.json` | Lesson collection + Quality dashboard + IMA upload |

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
                          Agent 7 (publish: LESSON + quality + IMA)
```

**Each Agent runs in isolated session (context:isolated, lightContext:true). Main session only handles spawn + gate + file existence verification + Agent 7 IMA upload call.**

### Guardrail Routing

| Mode | Trigger | Pipeline | Agents |
|:-----|:--------|:---------|:------:|
| **full** | Case characterization, sanction recommendation | 0→(1a∥1b)→1c→2→3→4→5→6→7 | 9+1 |
| **interview** | 谈话手册 | 0→(1a∥1b)→1c→2→3+4→7 | 6+1 |
| **quick** | Regulation consultation / article lookup | 0→(1a∥1b)→1c→2→7 | 5 |

**Routing decision:** After Agent 0 completes, select mode based on `task_type`.

---

## 🔒 Protocol

### Agent Gate Protocol (v2.4 — Schema Validation)

After each Agent completes, execute gate in order:

**Gate A — File Existence (v2.3):** `read <output> → exists + size > 0`. File not found → mark `failed` → write `pipeline_failure_log.json` → do NOT proceed.

**Gate B — Schema Validation (v2.4 NEW):** Parse JSON output, validate against Agent's `## Output Schema` section in its agent file.
- Required fields present → PASS → proceed to next Agent
- Required fields missing → mark Agent `SCHEMA_FAIL` → write `pipeline_failure_log.json` → **return to that Agent for re-run (max 1 retry)**
- Markdown output (Agent 4/6): `rg` search for required heading markers

**Gate C — Summary Record (v2.4 NEW):** Gate passed → record `<output_path> + <agent_name> + <status> + <key_metrics>` to quality context for downstream agents.

```
Gate flow: A(exists?) → B(schema valid?) → C(record summary) → next Agent
                        ↓ FAIL
                   pipeline_failure_log.json → re-run Agent (1 retry) → still FAIL → halt
```

**⛔ Gates A+B only verify structure — do NOT read full content into main session context.**

### 进度可见性（v2.6 · 对标 OPL progress visibility）

> 每个 Phase 完成后，主会话输出一行人类可读的进度摘要。不再盲猜管线走到哪。

**进度输出格式：**

```
🔵 0/9 Scope      ⏳ 运行中（第一步）
🟢 0/9 Scope      ✅ 公职人员身份确认 → regulation_list: 5部法规
🟢 1/9 Search∥     ✅ 1a: 8条款原文 | 1b: 5法规版本确认
🟢 2/9 Merge       ✅ 5法规 matched + 2条额外发现(第98/111条)
🟡 3/9 Audit       ⚠️ PASS_WITH_WARNINGS (5项WARNING)
🟢 4/9 Analyze     ✅ 双轮辩论完成 → 111条优先认定
🟢 5/9 Draft       ✅ 685行 v2.4报告
🟢 6/9 Review      ✅ 82/100 PASS
🟢 7/9 Revise      ✅ 33处[未溯源]标注 + 59处P0-P2
🟢 8/9 Publish     ✅ IMA已上传
⬜ 9/9 Self-Repair  ⏳ 扫描中…
✅ 9/9 Done         0条P0教训 / 48分钟
```

**阻塞输出格式：**

```
🔴 3/9 Audit       ❌ REJECT: Agent 2 条款核查失败 → 退回 Agent 1c 重查
🔴 5/9 Review      🔴 HUMAN_ESCALATION: 56/100 < 65 → 暂停，等石冰决策
```

### Solo Status Protocol（机器可读·保留兼容）
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
├── agent6-final.md              ← Phase 6: final version
├── revision_log.json            ← Phase 6: revision log
├── agent7-publish-report.json   ← Phase 7: lesson scan + quality dashboard report
├── pipeline_failure_log.json    ← v2.4: failure tracking + resume checkpoint
├── _quality.json                ← v2.4: pipeline quality metrics aggregation
└── _lessons.json                ← v2.4: structured lesson collection
```
**task_id format:** `DI-YYYYMMDD-seq`

### Pipeline Resilience (v2.4 NEW)

**Failure Log:** Any Agent gate failure → write `pipeline_failure_log.json`:
```json
{
  "pipeline_id": "DI-YYYYMMDD-seq",
  "failed_agent": "agentN",
  "failure_type": "FILE_MISSING | SCHEMA_FAIL | GATE_FAIL",
  "failure_detail": "...",
  "completed_outputs": ["agent0-scope.json", "agent1a-search-rg.json", ...],
  "retry_count": 0,
  "timestamp": "ISO-8601"
}
```

**Resume Protocol:** Before spawning any Agent, check if its output file already exists in `pipeline_output_dir/`:
- Output exists + not marked FAILED in `pipeline_failure_log.json` → **skip** (already completed)
- Output exists + marked FAILED → **re-run** (retry)
- Output missing → **spawn** (normal execution)

**Max retries:** 1 per Agent. After 2nd FAIL → pipeline halts, report to domain owner with `pipeline_failure_log.json`.

**Cross-session resume:** Pipeline can be resumed from a different session if `pipeline_failure_log.json` + completed outputs exist. Main session reads failure log → spawns next pending Agent.

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

### Agent 1c: Merge (Three-Way Regulation Merge)
**Input:** agent0-scope.json + agent1a + agent1b
**Output:** `agent1-merged.json` — three-way match per regulation (rg hit + pkulaw status) with discrepancy markers (UNVERIFIED / search_miss). Five-status classification per regulation: matched / text_only / version_only / missing.
**Agent file:** `agents/merge.md` (v2.4-P3: formerly inline, now with dedicated agent file + Output Schema + Gate B coverage)

### Agent 2: Audit (Regulation Citation Audit)
**Input:** agent0-scope.json + agent1-merged.json
**Output:** `agent2-audit.json` — article number verification · [UNCERTAIN] block check · Subject-Behavior-Result three-element verification · version consistency · conclusion: PASS / PASS_WITH_WARNINGS / FAIL
**Agent file:** `agents/audit.md`

### Agent 3: Analyze (Deep Analysis · v2.3)
**Input:** agent0-scope.json + agent1-merged.json + agent2-audit.json
**Output:** `agent3-analyze.json` — P1 conceptual framework → violation+responsibility two-factor analysis (11-step workflow with embedded M2-M9 modules) → dual-round adversarial debate → case matching → P2 procedural guidance
**Agent file:** `agents/analyze.md` (includes full P1+P2 framework, 11-step workflow, YAML output template, medical case specialty)

### Agent 4: Draft（谈话手册 / 案件报告）

**Output:** `agent4-draft.md`

- **interview模式→谈话手册**：速览+瑕疵+策略+法规卡+问话表。150行以内。删减：逐条论证/M7-M9过程/量纪矩阵/调查方法清单。保留：案件速览、瑕疵声明、突破口策略、心理攻防、第十七条话术、指导性案例参照、法规速查、**36条问话汇总（分四阶段）**。
- **full模式→核查报告**：七章标准报告 + 谈话提纲护栏（涉刑转段警告+法规交叉引用+谈话对象三层区分）
**Agent file:** `agents/draft.md`

### Agent 5: Review (Quality Audit)
**Input:** agent4-draft.md + agent1a + agent1b
**Output:** `agent5-review_ledger.json` — Twenty-Four-Character Policy 6-dimension scoring matrix (25/20/20/15/10/10 weights). ≥80 PASS · 60-79 REVISE · <60 REJECT
**Agent file:** `agents/review.md`

### Agent 6: Revise (Fix)
**Input:** agent4-draft.md + agent5-review_ledger.json
**Output:** `agent6-final.md` + `revision_log.json`
**Agent file:** `agents/revise.md`

### Agent 7: Publish (v2.5.1 — IMA Upload + LESSON Collection + Quality Dashboard)

**Agent file:** `agents/publish.md` (includes Output Schema for Gate B validation)

**Step 7a — IMA Upload:** Called from main session: `node skills/solo-file-transfer/scripts/ima_upload.cjs <agent6-final.md> <KB_ID>`

**Step 7b — LESSON Collection (v2.4 → v2.5.1):** After upload, scan all agent output files for `[LESSON]` markers:
- `rg "\[LESSON\]" memory/inspection-drafts/{task_id}/` across all json/md files
- Collect structured lessons → append to `memory/inspection-drafts/_lessons.json`:
```json
{
  "pipeline_id": "DI-YYYYMMDD-seq",
  "date": "ISO-8601",
  "lessons": [
    {
      "source_agent": "agent3",
      "category": "methodology | regulation | case | procedure",
      "urgency": "P0 | P1 | P2",
      "lesson": "...",
      "action": "UPDATE_AGENT | ADD_CASE_TAG | UPDATE_REGULATION | NOTE_ONLY"
    }
  ]
}
```
**Urgency routing (v2.5.1 NEW):**
- `urgency: P0` (critical methodology bug / systematic error pattern) → **IMMEDIATE notification** to domain owner. Compose: `"⚡ DI URGENT LESSON | {task_id} | {source_agent} | {lesson_summary_first_80_chars}"` → send via messaging tool. Duration from finding to notification: <1 minute (vs 30-day monthly cron cycle).
- `urgency: P1` (important pattern / recurring gap) → flagged for next regulation-manager monthly cron review.
- `urgency: P2` (minor improvement) → recorded only, no active push.
- Default (no urgency field): treated as P1.

Lessons with `action: UPDATE_AGENT` → flagged for next regulation-manager monthly cron review (P1/P2) or immediate push (P0).

**Step 7c — Quality Dashboard (v2.4 NEW):** Aggregate pipeline quality metrics → write `memory/inspection-drafts/_pipeline_quality_log.json`:
```json
{
  "pipeline_id": "DI-YYYYMMDD-seq",
  "timestamp": "ISO-8601",
  "quality": {
    "agent2_audit": "PASS | PASS_WITH_WARNINGS | FAIL",
    "agent5_score": 0-100,
    "agent5_dimensions": {
      "accurate_characterization": 0-100,
      "clear_facts": 0-100,
      "conclusive_evidence": 0-100,
      "appropriate_disposition": 0-100,
      "complete_procedures": 0-100,
      "procedural_compliance": 0-100
    },
    "upstream_feedback": [{"agent": "agentN", "issue": "...", "severity": "critical|high|medium|low"}],
    "lessons_generated": 0,
    "retries": 0
  }
}
```
**Quality trend check:** After append, compare current score with last 3 runs' average → deviation >15 points → flag for review.

⛔ **Report purity:** IMA upload = pure analysis content only. No pipeline IDs / Agent identifiers / audit metadata. Metadata → `memory/inspection-drafts/<case>/`.

---


## 🔧 Hermes 执行指南（v2.6.0）

> 本技能在 Hermes 上使用 `delegate_task` 替代 `sessions_spawn`。管线逻辑不变。

### 主会话执行流程

```
1. delegate_task Agent 0 (scope) → 读回 agent0-scope.json
2. delegate_task Agent 1a + 1b (并行) → 读回两个json
3. delegate_task Agent 1c (merge) → 读回 agent1-merged.json
4-9. agent 2→6 顺序 delegate
10. Agent 7 (publish) + Phase 8 (main session skill_manage)
```

### 关键差异

| 项目 | OpenClaw | Hermes |
|:-----|:---------|:-------|
| Agent 1a∥1b | sessions_spawn ×2 | delegate_task tasks[] 批量并行 |
| Gate 验证 | read 文件 | read_file 文件 |
| IMA上传 | wecom通知 | QQ Bot 原生交付 |
| 自修复 | ❌ | ✅ skill_manage 即时patch |

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
P1: 4 conceptual frameworks (Three Distinctions · Style-to-Corruption Gradient · Superficiality Identification · Seeing Through Appearance to Essence) as analysis backbone before violation determination. P2: 4 procedural rules (Sanction Matching · Asset Disposal · Accountability Pitfalls · Retirement≠Immunity) appended after conclusion. Agent 1c merge logic inlined (no standalone file). **Principle:** Higher-level conceptual framework reduces two-factor analysis blind spots.

### v2.5.2: Analyze Agent方法论重构 (2026-07-21)
来源：王某案实战 + OpenClaw 597行方法论文档吸收
核心改动（Agent 3 analyze.md）：
- **基座不变**：违规+有责双因素仍是基础
- **增强模块嵌入**：M7/M4/M8/M9四个高频模块内嵌到Agent prompt
- **条件触发**：M2（证据存疑时）/ M6（系统性案件时）
- **案例模式匹配**：新增P01-P05通用案例模式
- **经查→认为**：强制作为结论输出格式
- **interview精简路径**：跳过M2/M6，仍必做M7/M4/M8/M9
- **瑕疵不遗漏**：每项未确认事实标注F01-F06类编号

### v2.5.1 — Urgency Routing + KG Writeback (2026-07-18)

**Feedback loop acceleration (SP-ECO-001):** LESSON collection upgraded with `urgency` field. P0 lessons trigger immediate wecom notification (<1 minute vs 30-day monthly cron cycle). P1/P2 follow normal monthly review path.

**Bidirectional KG activation (SP-ECO-004):** Agent 3 `kg_enrichment` was read-only. Added `kg_writeback` field to propose new edges/nodes/updates discovered during analysis. Monthly cron Part D5 consumes `category:"kg"` lessons → high-confidence proposals auto-applied, medium/low flagged for review.

**Ecosystem coordination:** Monthly cron Part A now coordinates with weekly cron (new: `weekly regulation check` every Monday). solo-audit v5.6 deepened DI quality dashboard consumption (trend deviation detection).

**Principle:** An evolution ecosystem is not defined by its components — it is defined by the feedback loops between them. v2.5.1 shortens the DI→Cron→DI loop from 30 days to <1 minute for critical lessons, and makes the KG a living graph instead of a static snapshot.

### v2.5.0 — Full-Gate Pipeline (9/9) + Resilience + LESSON + Quality Dashboard + KG + Ruling Logic + Tuning (2026-07-18)

**The v2.5 milestone: 9-agent pipeline with 100% Schema Gate coverage.** Three-case CCDI live-fire validation confirmed all mechanisms.

**Structural hardening (P0):** Every agent file has `## Output Schema` → Gate B validates structure at every handoff. `merge.md` closes the last unprotected step (formerly inline, now a full agent). Schema rigidity fix: agent output templates aligned with Schema declarations, eliminating the most common failure mode (2 SCHEMA_FAILs in live test). Pipeline resilience: `pipeline_failure_log.json` + resume-from-checkpoint → 2 recoveries in live test without re-running completed agents.

**Knowledge refinement (P1):** Case-index.json upgraded to L1(tag)/L2(ruling_logic)/L3(difference) matching with `ruling_logic` (core_principle + distinction_criteria + applicable_when + not_applicable_when) for all 11 cases. Structured LESSON collection pipeline: `[LESSON]` → `_lessons.json` → monthly cron → Agent Tuning fields. Quality dashboard aggregates per-run metrics with trend detection.

**Ecosystem integration (P2):** Knowledge graph activation (55 nodes, 58 edges) → Agent 3 1-hop enrichment with `kg_enrichment` observability. Monthly cron Part C3: semi-automated case labeling + similarity matching + ruling_logic draft generation. All 9 agent files have `Execution Tuning` sections ready for lesson injection.

**Guard improvements (P3):** `scope.md` Step -1 WIKI_PATH check prevents silent degradation. Case ruling logic L2 matching enables logic-level (not just tag-level) case comparison.

**Principle:** A precision factory needs every handoff guarded, every signal collected, every lesson fed back. Quality is not a checkpoint — it is a continuous loop that starts at the first gate and never stops.

> Full changelog with file-level changes → `references/changelog.md`
