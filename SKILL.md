---
name: discipline-inspection
version: 2.8.1
description: "Discipline Inspection v2.8 - Three routing modes: quick (regulation consultation, search audit cannot be skipped), interview (talk outline, 8-segment standard), full (hearing recommendation, five-part V5 style). 9-Agent Full-Gate Pipeline + four guardrails (template injection, restatement comprehension, rewrite loop, main-session final review) + QJ circumstance determination framework + violation and accountability main line + case precedent matching + medical/dual-directory search + anonymized output."
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
# Discipline-Inspection ⚔️ v2.8

> **Discipline as the yardstick, vigilance as constant.** 9-Agent Full-Gate Pipeline + Schema Gates (100% coverage) + 🌟 Case Precedent Matching (v2.7·Agent3自动比对中纪委指导性案例) + Grounded Citations (v0.20.0原生·每条引用溯源到原文)。
> 🔓 Open source under MIT License.

> 📎 Shared config: `shared-config.yaml` · Agent files: `agents/*.md` (10 files, full Gate coverage) · Case index: `references/case-index.json` · Citation ledger: `scripts/sources.py` (Grounded Citations)

### 工具增强（2026-07-24）
- **execute_code**: 批量多文件比对·法规竞合分析·证据链完整性检查
- **vision_analyze**: 扫描件/截图OCR失败时的文档视觉分析（OCR管线降级后备）
- **todo**: 管线Agent阶段追踪·P0超时可视化
- **🌟 sources.py (v0.20.0)**: 引用溯源账本——每条法规引用逐一注册编号·逐字证据匹配·verify自动检查覆盖率

### 引用溯源工作流（v2.8加Gate）

**启动时（主会话·不可跳过）**: `sources.py --ledger <case>/citations.json reset`
**Agent 1a**: 每次rg搜索→ `sources.py add "file://..."` 注册· `quote --text` 附原文
**Agent 1b**: 每次pkulaw→ `sources.py add "https://pkulaw.com/..."` 注册
**Agent 4**: 用 `[1][2]` 编号引用→ `render --replace-in draft.md` 渲染Sources
**Agent 5**: `verify draft.md --evidence --min-coverage 0.6` 自动验证

**⛔ Gate 0 强制（v2.8）**：管线启动时主会话**必须**执行 `sources.py --ledger <case>/citations.json reset`——未初始化账本即开始搜索，Agent 1a/1b不得跳过注册（实战曾因未初始化跳过注册·教训固化）。Gate 0不通过→不启动管线。

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

### ⛔ Hard Pipeline Enforcement（v2.6·全模式硬控）

**三种路由模式全部硬控——必须逐Agent delegate调用，禁止单次delegate包全部。**

```
违规模板: delegate_task("DI full: 全部Agent") ← 🔴 禁止

full模式:
  deleg Ag0 → Ag1a∥Ag1b → Ag1c → Ag2 → Ag3 → Ag4 → Ag5(≥80) → Ag6 → Ag7

interview模式:
  deleg Ag0 → Ag1a∥Ag1b → Ag1c → Ag2 → Ag3+4 → Ag7

quick模式（v2.8.1 增加轻量Analyze+Review）:
  deleg Ag0 → Ag1a∥Ag1b → Ag1c → Ag2 → Ag3(轻量) → Ag5(轻量) → Ag7

🔴 quick≠直接回答·法规咨询也必须走搜索+审计+轻量分析+轻量审查
🔴 interview≠跳过Review·Ag2审计不可少
🔴 任何模式禁止主会话直接写结论
```

```
正确模式:
  deleg Ag0 → 等待返回·读 agent0-scope.json
  deleg Ag1a∥Ag1b 并行 → 等待返回·读两个json
  deleg Ag1c → 等待返回·读 agent1-merged.json
  deleg Ag2  → 等待返回·读 agent2-audit.json
  deleg Ag3  → 等待返回·读 agent3-analyze.json
  deleg Ag4  → 等待返回·读 agent4-draft.md
  deleg Ag5  → 等待返回·读 agent5-review_ledger.json
  deleg Ag6  → 等待返回·读 agent6-final.md
  deleg Ag7  → 等待返回·上传确认
```

**为什么**: 单次delegate跳过搜索审计→法规从记忆引用→来源不可追溯。独立会话执行已验证——不可跳过。

### Guardrail Routing

| Mode | Trigger | Pipeline | Agents |
|:-----|:--------|:---------|:------:|
| **full** | 处理建议（审理建议·经审理查明→认为→处理建议） | 0→(1a∥1b)→1c→2→3→4→5→6→7 | 9+1 |
| **interview** | 谈话手册 | 0→(1a∥1b)→1c→2→3+4→7 | 6+1 |
| **quick** | 法规咨询/条款查询 | 0→(1a∥1b)→1c→2→**3(轻量)**→**5(轻量)**→7 | 🔴搜索和审计不可跳过 |

> **quick 模式 v2.8.1 优化（实战复盘）**：原 quick=0→1a∥1b→1c→2→7 缺 Analyze/Review——一次 quick 实战暴露：Agent 7 直接写报告出现"目的解释涵盖宴请"类错误论证（法理深度不足）·未被管线发现（靠用户追问才暴露）。
> **轻量 Agent 3**：只做法理要点分析（行为定性·版本演进·案例参照·对抗要点）·不做完整双轮辩论/QJ 全维度——但**必须输出违规定性+案例对照**（v2.8.1 四步法）。
> **轻量 Agent 5**：只查关键错误（条款号错误·文义跳跃·来源缺失·结论与依据矛盾）·不全维度评分——但**必须输出 PASS/REJECT**。
> 目的：法规咨询也保证法理深度 + 质量把关·复用现有 Agent 3/5（非新增）。

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
🔴 5/9 Review      🔴 HUMAN_ESCALATION: 56/100 < 65 → 暂停，等用户决策
```

### Solo Status Protocol（机器可读·保留兼容）
Before/after each Agent spawn, update `./solo/pipeline-status.json` with pipeline_id + phase status (structure defined in `skills/solo/SKILL.md`).

### Output Path Protocol（v2.8统一）
> ⚠️ v2.8修正：所有Agent输出统一到 `tmp/{task_id}/`（主会话创建）——不再使用旧路径。
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

### 案件节点 Checkpoint 打点（Harness 借鉴 · P1-2）
> 办案会话在三个关键节点执行一次 Hermes checkpoint（`hermes checkpoint` 内建·git-like 快照），并把节点名写进产物头部——复盘/改版从最近节点恢复，防「子代理写冲突」类事故（实战曾发生后续运行覆盖前期版本的教训）。
```
🔴 三节点打点（纪委"三定一析"文书节奏对齐）:
① 初核启动（事实范围确定后）
② 谈话提纲定稿（DI interview 模式 agent6-final 前）
③ 审理报告定稿（DI report-writing 上传 IMA 前）
```
**产物头标注**：`> 节点: 初核启动/提纲定稿/报告定稿 · checkpoint: <id>`（可追溯·可恢复）。

### 过程卷宗（Harness 借鉴 · P1-1）
> 办案产物（谈话手册/审理报告/量纪建议/合规意见）**尾部固定一段「过程卷宗」**——AI 参与办案的留痕规范（纪律刚需·对齐「凡进结论的依据必须可查」）。
```
## 过程卷宗
- 模型层级：哪几步 Pro / 哪几步轻量
- 检索依据：命中法规文件名 + 文号清单（WIKI库/知网/指导性案例来源）
- 子代理链：deleg_id + 输入摘要（一句话）+ 产出文件名
- 事实修正轮次：v1→vN 每轮改了什么事实（只记变化·不记案情细节）
```
**🔴 只记依据·不记案情**：不写谈话内容原文/个人信息细目（脱敏天然成立·护栏）。
**适用**：纪律审查类管线最终产物（agent6-final.md 上传 IMA 前必须含此段）。

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

### Agent 3: Analyze（核心·重中之重·v2.8）
**Input:** agent0-scope.json + agent1-merged.json + agent2-audit.json
**Output:** `agent3-analyze.json` — 违规+有责两因素主线（违规性六要素+有责性五要素）→ QJ情节认定框架（方向判定·八维度·加重减轻·由风变腐·反面翻盘）→ 案例匹配 → 双轮对抗辩论 → P2程序指引
**Agent file:** `agents/analyze.md`（含核心定位三层结构·QJ Framework·违规+有责方法论）
**Model:** ⚠️ **必须使用 Pro 模型**——深度法律论证（对抗辩论·竞合分析·案例匹配·情节认定）需要最强推理。轻量模型只用于搜索采集类Agent（1a/1b）。主会话 delegate 时指定 Pro 模型。

### Agent 4: Draft（谈话手册 / 案件报告）

**Output:** `agent4-draft.md`

- **interview模式→谈话手册**：速览+瑕疵+策略+法规卡+问话表。150行以内。删减：逐条论证/M7-M9过程/量纪矩阵/调查方法清单。保留：案件速览、瑕疵声明、突破口策略、心理攻防、第十七条话术、指导性案例参照、法规速查、**36条问话汇总（分四阶段）**。
  - 📎 interview 模式参考：8段模板 `references/interview-handbook-8segment-template.md` · 零证据策略 `references/zero-evidence-interview-strategies.md` · 提问4要素/分线/pitfalls `references/di-interview-pitfalls.md` · 质量验证 `scripts/verify-interview-handbook.py` · 境外持股案型 `references/overseas-shareholding-case-20260826.md`
- **full模式→审理建议**：五部分结构——①被核查人基本情况 ②核查结果(具体日期精确到日·业务往来背景·定性条款嵌入) ③处理建议(结论先行·"鉴于…综合认定情节轻微"一句话·办公会·拟批评教育·责令退缴) ④情节认定分析(按本案实际情节命名·轻微/较重/严重·案情简单可简写) ⑤结束语 + 依据附注(每条完整条款原文+版本年份+适用分析)
**Agent file:** `agents/draft.md`（含四护栏·范文注入V5·复述理解·回炉机制）

### Agent 5: Review (Quality Audit)
**Input:** agent4-draft.md + agent1a + agent1b + agent3-analyze
**Output:** `agent5-review_ledger.json` — 六维评分(0-80) + R1-R4可读性(0-20) + R5案例匹配质量(0-10) = 0-110总分. ≥88 PASS · 70-87 REVISE · <70 REJECT
**Agent file:** `agents/review.md`（含R1读者视角/R2说服力/R3条款完整性/R4全局一致性/R5案例匹配质量）

### Agent 6: Revise (Fix)
**Input:** agent4-draft.md + agent5-review_ledger.json
**Output:** `agent6-final.md` + `revision_log.json`
**Agent file:** `agents/revise.md`

### Agent 7: Publish (v2.6 — IMA Upload + LESSON Collection + Quality Dashboard)

**Agent file:** `agents/publish.md` (includes Output Schema for Gate B validation)

**Step 7a — IMA Upload:** Called from main session: `node skills/solo-file-transfer/scripts/ima_upload.cjs <agent6-final.md> <KB_ID>`

**Step 7b — LESSON Collection (v2.4 → v2.6):** After upload, scan all agent output files for `[LESSON]` markers:
- `rg "\[LESSON\]" tmp/{task_id}/` across all json/md files
- Collect structured lessons → append to `tmp/_lessons.json`:
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
**Urgency routing (v2.6 NEW):**
- `urgency: P0` (critical methodology bug / systematic error pattern) → **IMMEDIATE notification** to domain owner. Compose: `"⚡ DI URGENT LESSON | {task_id} | {source_agent} | {lesson_summary_first_80_chars}"` → send via messaging tool. Duration from finding to notification: <1 minute (vs 30-day monthly cron cycle).
- `urgency: P1` (important pattern / recurring gap) → flagged for next regulation-manager monthly cron review.
- `urgency: P2` (minor improvement) → recorded only, no active push.
- Default (no urgency field): treated as P1.

Lessons with `action: UPDATE_AGENT` → flagged for next regulation-manager monthly cron review (P1/P2) or immediate push (P0).

**Step 7c — Quality Dashboard (v2.4 NEW):** Aggregate pipeline quality metrics → write `tmp/_pipeline_quality_log.json`:
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

⛔ **Report purity:** IMA upload = pure analysis content only. No pipeline IDs / Agent identifiers / audit metadata. Metadata → `tmp/<case>/`.

---

### Phase 8 — 主会话终审门禁（v2.8·结构性防"不合格交付"）

Agent 6产出 agent6-final.md 后，**主会话必须终审**才能上传IMA：

1. 读 agent6-final.md 全文
2. 对照 writing-convention v5.1 逐条检查：
   - ✅ 五部分：基本情况→核查结果→处理建议→情节认定分析→结束语
   - ✅ 处理建议：结论先行·依据嵌入·办公会要素
   - ✅ 依据附注每条含**完整条款原文**+版本年份+适用分析
   - ✅ 金额/人名/时间等事实要素与案件已知事实一致（不虚构）
   - ✅ 无附录/审计链/Agent标注/pipeline ID/矩阵/要件表
   - ✅ 语言像正式文书（非JSON拼接）
3. 任一不通过 → 退回Agent 4重写（走护栏三）
4. 全部通过 → 才执行 IMA 上传

**终审是主会话职责——不可跳过·不可委托Agent。**

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

> 📌 **Agent 定义加载**：各 Agent 规范=主技能 `agents/<name>.md`（子代理在 delegate prompt 中注明读取对应文件路径，不再依赖独立技能）。Agent 增量参考/验证脚本在 `agents/<name>/references/` 与 `agents/<name>/scripts/`。
> 📌 **模式组件索引**：interview 手册→`references/di-interview-pitfalls.md`+`interview-handbook-8segment-template.md` · 审理报告→`references/di-report-writing.md` · 量纪论证→`references/discipline-sentencing-argumentation.md` · 境外持股案型→`references/overseas-shareholding-case-20260826.md`

### 关键差异

| 项目 | OpenClaw | Hermes |
|:-----|:---------|:-------|
| Agent 1a∥1b | sessions_spawn ×2 | delegate_task tasks[] 批量并行 |
| Gate 验证 | read 文件 | read_file 文件 |
| IMA上传 | 消息平台通知 | 聊天平台原生交付 |
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

> 📚 Full regulation inventory maintained in wiki: `${WIKI_PATH}/discipline/regulations/` (45+ regulations), `${WIKI_PATH}/medical/` (行业规范·九不准/九项准则/行动计划), `${WIKI_PATH}/discipline/guiding-cases/` (11 CCDI guiding cases). Auto-updated monthly by regulation-manager cron.

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

### v2.5.2 — Urgency Routing + KG Writeback + Ecosystem Tightening (2026-07-18)

**Feedback loop acceleration (SP-ECO-001):** LESSON collection upgraded with `urgency` field. P0 lessons trigger immediate notification (<1 minute vs 30-day monthly cron cycle). P1/P2 follow normal monthly review path.

**Bidirectional KG activation (SP-ECO-004):** Agent 3 `kg_enrichment` was read-only. Added `kg_writeback` field to propose new edges/nodes/updates discovered during analysis. Monthly cron Part D5 consumes `category:"kg"` lessons → high-confidence proposals auto-applied, medium/low flagged for review.

**Ecosystem coordination:** Monthly cron Part A now coordinates with weekly cron (new: `weekly regulation check` every Monday). solo-audit v5.6 deepened DI quality dashboard consumption (trend deviation detection).

**Principle:** An evolution ecosystem is not defined by its components — it is defined by the feedback loops between them. v2.5.2 shortens the DI→Cron→DI loop from 30 days to <1 minute for critical lessons, and makes the KG a living graph instead of a static snapshot.

### v2.5.0 — Full-Gate Pipeline (9/9) + Resilience + LESSON + Quality Dashboard + KG + Ruling Logic + Tuning (2026-07-18)

**The v2.5 milestone: 9-agent pipeline with 100% Schema Gate coverage.** Three-case CCDI live-fire validation confirmed all mechanisms.

**Structural hardening (P0):** Every agent file has `## Output Schema` → Gate B validates structure at every handoff. `merge.md` closes the last unprotected step (formerly inline, now a full agent). Schema rigidity fix: agent output templates aligned with Schema declarations, eliminating the most common failure mode (2 SCHEMA_FAILs in live test). Pipeline resilience: `pipeline_failure_log.json` + resume-from-checkpoint → 2 recoveries in live test without re-running completed agents.

**Knowledge refinement (P1):** Case-index.json upgraded to L1(tag)/L2(ruling_logic)/L3(difference) matching with `ruling_logic` (core_principle + distinction_criteria + applicable_when + not_applicable_when) for all 11 cases. Structured LESSON collection pipeline: `[LESSON]` → `_lessons.json` → monthly cron → Agent Tuning fields. Quality dashboard aggregates per-run metrics with trend detection.

**Ecosystem integration (P2):** Knowledge graph activation (55 nodes, 58 edges) → Agent 3 1-hop enrichment with `kg_enrichment` observability. Monthly cron Part C3: semi-automated case labeling + similarity matching + ruling_logic draft generation. All 9 agent files have `Execution Tuning` sections ready for lesson injection.

**Guard improvements (P3):** `scope.md` Step -1 WIKI_PATH check prevents silent degradation. Case ruling logic L2 matching enables logic-level (not just tag-level) case comparison.

**Principle:** A precision factory needs every handoff guarded, every signal collected, every lesson fed back. Quality is not a checkpoint — it is a continuous loop that starts at the first gate and never stops.

### v2.6 — Analyze Agent方法论重构 (2026-07-21)
来源：实战复盘 + 方法论文档吸收
核心改动（Agent 3 analyze.md）：
- **基座不变**：违规+有责双因素仍是基础
- **增强模块嵌入**：M7/M4/M8/M9四个高频模块内嵌到Agent prompt
- **条件触发**：M2（证据存疑时）/ M6（系统性案件时）
- **案例模式匹配**：新增P01-P05通用案例模式
- **经查→认为**：强制作为结论输出格式
- **interview精简路径**：跳过M2/M6，仍必做M7/M4/M8/M9
- **瑕疵不遗漏**：每项未确认事实标注F01-F06类编号

### v2.8.0 — Agent 3核心重构 + 四护栏 + V5报告样式 (2026-08-07)
来源：全流程实战复盘 + 用户反馈（"报告不好读"·"情节轻微论证不充分"·"九项准则漏引"·"情节考量不能机械"）
核心改动：
- **Agent 3三层结构**：主线(违规+有责两因素·违规性六要素+有责性五要素·必读方法论文件) + 关键支撑(QJ情节认定框架·方向判定→八维度→加重减轻→由风变腐→反面翻盘) + 辅助(案例匹配/P1/对抗辩论/M模块)
- **QJ Framework**：从11指导性案例+5模式(31案统计)凝练——量纪分水岭(P04·谋利=断崖)·八维度QJ-8D·加重减轻清单·由风变腐Stage1阻断窗口·反面翻盘点"高置信·条件性"·禁引5000元
- **四护栏**：范文注入(V5首选)·复述理解·回炉重写·主会话终审
- **V5报告样式**：五部分(基本情况→核查结果→处理建议→情节认定分析(灵活命名)→结束语)+依据附注
- **教训**：①版本号/检查项/Agent定义三处同步 ②Agent 3必须Pro模型 ③金额人名等事实以用户确认为准 ④行业规范版本链条（九不准2013行为时→九项准则2021替代参照）

### v2.8.1 — 定性路径选择方法论（多路径对比+边界设定）

**来源**：某案定责·用户质疑定性路径选择（"依据A还是B处理比较？"）→ 路径裁决后固化方法论。

**核心方法**：
1. **列路径**：行为可能涉及的所有定性路径
2. **逐路径要件检视**：每条路径列构成要件·逐项对照事实——不满足即排除（不因"行为可谴责"硬套）
3. **选主线**：最能反映**行为本质**的路径为定性主线
4. **边界设定**：明确"什么情况才转另一路径"——供实务对照·防误判

**泄露隐私三要件**（判"泄露"是否成立·民法典1032/1226条文义参照）：
- 对象：是否扩散（单点/特定 vs 多人/公开）
- 动机：主观故意是否指向"泄露隐私"（非"证明某事"）
- 内容：是否患者重大敏感隐私（涉性病/HIV/精神疾病等·单点披露即侵权·不要求扩散）

**自查**：写定性前先问——"这个行为最像哪条路径？其他路径为什么不成立？什么情况会转路径？"——三问过一遍再落笔。

**案件事实链护栏**：新事实→全量重写（事实每轮变化都驱动定性/处分修正·最终版才准确）。写定责文书时先确认"事实是否已全部锁定"·未锁定项标注[待核实]不预判。

### v2.8.1 — 篡改病历构成要件（文义优先·结果性动词）

**核心方法论**：**"篡改"是结果性动词**——评价"病历是否被篡改"（最终记载是否失真）·非"是否曾有一次改动动作"。操作日志证明"有改动"≠"构成篡改"。禁止因"行为可谴责"而扩大解释（文义优先：如2021九项准则专门增补"宴请"即说明旧文义不含）。

**篡改病历四要件**（全部满足才构成）：
1. 对象要件：针对**既成文书**（已签名/已打印/已归档·非初稿书写过程）
2. 行为要件：以作伪手段改动记载内容
3. 结果要件：使记载与客观事实不符（失真）
4. 持续性要件：失真状态存在未被纠正

**初稿（草稿）≠ 既成病历**：《病历书写基本规范》(卫医政发〔2010〕11号)第7条"书写过程中修改"属正常环节·由"修改规范"调整·非"篡改"评价。《电子病历应用管理规范》(国卫办医发〔2017〕8号)第17条"归档后原则上不得修改"——归档=既成文书分界点。

**边界（构成篡改的情形）**：①既成文书（已签名/打印）②失真持续未改回③归档后擅自修改④目的是使虚假记载长期存在（掩盖医疗过错/骗保/规避责任）。

**自查**：写病历篡改定性前，先查四要件——"改过"≠"篡改"；初稿修改≠篡改；改回恢复≠篡改。

### v2.8.1 — 科技成果转化持股合规论证链

**来源**：某科研人员持股案（中共党员·临床医生·拟提拔·持股基于自身科技成果转化·单位现金奖励→现金购股）·合规+纪律双管线·版本A/B裁决。

**核心规则**：
1. **身份分水岭**（第一母变量）：管理岗（监察对象·从严）vs 技术岗职称（创新创业空间）·"双肩挑"任管理岗即监察对象
2. **持股定性**：党纪103条(二)"违反有关规定"拥有非上市公司股份——**前置要件**是"违反有关规定"·合规科技成果转化激励不在射程
3. **分类管理**（国发〔2016〕16号(八)）：正职领导（不含内设机构）原则上不得获股权激励·**其他担任领导职务的科技人员**（副职/中层）可获现金、股份或出资比例奖励
4. **奖励路径**：现金奖励（转化法44+45条(一)）→ 以奖励资金购股 = "奖励转化形态"（非自有资金投资·不视同经商办企业·百问百答37）
5. **版本A/B分水岭**：购股公司=成果转化形成的公司（A·合规）vs 无关公司（B·103条(二)风险上升）——**事实决定论证路径**·未确认前不预设结论
6. **程序补强**：单位审批/公示/奖励文件三要件（人社部规〔2017〕4号）·缺程序=最大翻车点
7. **对抗要点**：现金到账后再购股=投资？奖励资金购股=变相投资？领导干部一律不得持股？公立医院不适用16号(八)？涉医院业务=利益冲突？（5条预案见 references/keji-chengguo-zhuanhua-chigu-hegui.md）

**自查**：写党员领导干部持股定性前，先问——持股来源是什么？（科技成果转化 vs 自行投资）·购股公司是否与成果相关？·拟任/现任岗位是正职还是其他领导？

### v2.8.1 — 医院纪委办案核心制度依据（重要）

**来源**：医院纪委办案场景提醒——"我们是医院纪委办案·九项准则+行为规范是很重要的制度依据·要重点用"

**教训**：DI 管线默认把《医疗机构工作人员廉洁从业九项准则》（国卫医发〔2021〕37号）当"行业规范参照"·《医疗机构从业人员行为规范》（2012·**卫办发〔2012〕45号**）完全没提——**医院纪委办案时这两部是直接定性依据·不是参照**！

**核心规则**：
1. **医院纪委办案·定性三件套**（配套使用·全部要引）：
   - 《医疗机构从业人员行为规范》= 基础行为准则·**第八条"廉洁自律恪守医德"**·第五十五条（考核/医德考评/职称晋升挂钩）·**第五十六条（院内处理出口：批评教育→通报→低聘→解聘·需纪检的移交纪检）**
   - 《医疗机构工作人员廉洁从业九项准则》= 廉洁从业专项依据·违反→"视情节依法依规处理·违反党纪政纪移交纪检监察"
   - 《事业单位工作人员处分规定》= 纪律责任（身份适用·事业编）
2. **谈话手册必须贯穿**：案件速览定性 + 适用框架 + 辩解预案（身份锚定"职业操守问题非私德"）+ 政策窗口（第五十六条=院内处理出口）+ 法规卡
3. **行为时版本链**：2021-11-12 前行为→九不准（2013·国卫办发〔2013〕49号）·之后→九项准则（37号）
4. **场景判断**：医院纪委办案 → 三件套必引；非医院场景 → 按身份适用

**自查**：写医院系统人员纪律分析时，grep 手册是否含"九项准则+行为规范"——缺失=依据不全。

### v2.8.1 — 多案综合复盘：DI技能优化 (2026-08-12)
来源：full/interview/quick 多案跨案例归纳
**本版改动**：
- **quick模式增加轻量Analyze+Review**：0→1a∥1b→1c→2→3(轻量)→5(轻量)→7——法规咨询也保证法理深度+质量把关（某次quick实战"目的解释涵盖宴请"错误未被管线发现·靠用户追问才暴露）
- **指导性案例深入结合四步法**：案例贯穿违规性/有责性/QJ/处理四步·非Step 0一次性
- **版本演进核查子步骤(4.1)**：定性前必查行业规范版本链（九不准→九项准则→医药代表管理办法）·条款变化证明文义边界·防错误扩大解释
**跨案例共性**：
- 身份→法规体系映射是第一步（群众/非党员/普通职工·三层折叠）
- 事实锁定在分析前·新事实→全链重写——事实确认护栏
- 行业规范版本链是定性关键（九项准则增补宴请）——非个案·已固化为标准维度
- 指导性案例是"对照基准"非"参考材料"（如违规吃喝指导性案例5名干部批评教育——轻处理可对标）

> Full changelog with file-level changes → `references/changelog.md`
