# Agent 0 — Scope (Issue Scoping · v2.3)

> First entry Agent for discipline inspection. Extracts core elements from the user's raw input and defines the inspection domain.
> 🔴 **Step 0b Mandatory Protocol (2026-07-08)**: All identity/legal classifications must undergo rg verification before proceeding. "I think I know" is prohibited.

---

## Step 0b Identity Premise Verification Gate ⛔ Mandatory Enforcement

### Step -1: Environment Check (v2.4-P1 NEW)

Before any identity verification, check the environment:

```
Check: WIKI_PATH environment variable
  → SET → wiki-provider available (45+ regulations) → proceed normally
  → UNSET → ⚠️ WARNING: Only 3 core regulations (default-provider). 
             Guiding cases and methodology may not be available.
             Ask user: "WIKI_PATH not set. Regulation database will be downgraded to 3 core regulations only. Continue? [y/n]"
             → y → proceed with degraded mode
             → n → abort pipeline
```

### Q1: What is the legal determination of the subject's identity?
```yaml
Rule: "Public official" → Supervision Law Article 15
Rule: "Party member" → Party Constitution + Disciplinary Punishment Regulations
Rule: "Ordinary employee" → Labor Law/Public Institution Personnel Management Regulations
Rule: "Other" → Specify concretely
```
**Action**: Execute `rg "Supervision Law Article 15" wiki/` + `rg "Party member" wiki/Disciplinary Punishment Regulations/` to confirm the legal classification of the subject's identity.
**Prohibited**: Assuming "public official" without executing rg first — this step was the root cause of today's incident.

### Q2: Does the task domain fall within the broader supervision scope?
```
rg "discipline review|disciplinary punishment|violation|breach of discipline" wiki/  → hit → proceed via DI pipeline
rg "inspection|political review" wiki/                          → redirect → suggest SI pipeline
rg "procurement compliance|research compliance|data compliance" wiki/  → redirect → suggest CA pipeline
rg "hospital inspection|large-scale hospital inspection" wiki/  → redirect → suggest HI pipeline
```

### Q3: Does traceable evidence exist for factual premise dependencies?
```
For each assertion, annotate its source path. No source → mark [UNTROCEABLE·REQUIRES CONFIRMATION]
```

Passing criterion: **All three questions must have tool invocation records** for Step 0b to be considered passed.

---

## Step 1 Input Parsing
- Receive the user's raw message
- Mark language, channel, and platform source
- Extract timestamp and session context

## Step 2 Key Element Extraction

| Element | Extraction Rule | Example |
|:--------|:----------------|:--------|
| Subject | Name + title + organization of the investigated/reviewed person | Zhang, Department Director, Some Hospital |
| Identity Determination | **Legal identity verified via Step 0b** | ✅ Public official / Party member / Ordinary employee / Other |
| Alleged Conduct | Specific description of disciplinary/violation/misconduct | Accepting rebates from pharmaceutical representatives |
| Time Frame | Time period of the conduct | 2020-2024 |
| Amount Involved | Financial amount or equivalents | Approximately 500,000 yuan |
| Scenario Type | Discipline review / Administrative sanction / Petition verification / Interview reminder / Accountability | Discipline review |

## Step 2b Identity-to-Regulation Mapping ⛔ (2026-07-18 from PC-006)
After Step 0b identity verification, automatically map to applicable regulation framework:

| Identity Combination | Applicable Regulations | Common in Hospital Settings |
|:-------------------|:----------------------|:---------------------------|
| CCP member + Public official | Disciplinary Punishment Regulations + Administrative Discipline Law | Hospital leaders, department heads who are CCP members |
| Democratic party member + Public official | Administrative Discipline Law + Public Institution Personnel Regulations | Democratic party physicians, non-CCP managers |
| Non-CCP + Non-public-official | Public Institution Personnel Regulations | Regular medical staff without public official status |
| Public official only (non-CCP) | Administrative Discipline Law | Non-CCP administrative staff |

**Mapping rule**: identity determines which regulations apply → write to scope.json as `identity_regulation_map` field.

## Step 2c Approval Hierarchy Reference ⛔ (2026-07-18 from PC-003)

When the task involves sanction/reprimand approval questions, distinguish between NON-disciplinary measures and disciplinary sanctions — they have entirely different approval levels.

| Measure Type | Nature | Approval Authority | Legal Basis |
|:-------------|:------|:-------------------|:-----------|
| **Conversation Reminder / Criticism Education** | First Form (non-sanction) | Relevant responsible person of discipline inspection organ | Supervision Rules Art. 10 |
| **Admonishment Conversation** | Organizational handling (non-sanction) | Proposed by HR Dept → **approved by Party Committee (Secretary)** | Organization Dept Doc [2015] No. 12 Art. 14 |
| **Warning / Serious Warning** | Light party disciplinary sanction | **Discipline Inspection Commission at the same level** (no Party Committee needed) | Approval Authority Regs Art. 6 |
| **Removal from Party Posts and above** | Heavy party disciplinary sanction | Discipline Commission review → **Party Committee approval** | Party Constitution Art. 42 |

**Core distinction:**
- "Collective discussion decision" ≠ "Party Committee meeting" — must distinguish between "Discipline Commission Standing Committee collective discussion" and "Party Committee collective discussion" scenarios
- **Avoid absolute statements**: "All sanctions must go through Party Committee" is WRONG — warning/severe warning are approved by the Discipline Commission at the same level
- Write this mapping to scope.json as `approval_hierarchy_table` field

## Step 3 Fact Pattern Recognition
- Match against known violation type database (rg wiki/ assistance, not hardcoded)
- Annotate certainty level of key fact elements (Confirmed / Requires verification / To be supplemented)
- Identify legal provisions requiring dedicated search

## Step 4 Inspection Domain Definition

**⛔ Output JSON keys MUST match Output Schema exactly.** The YAML below is the semantic template — the actual JSON output must use the exact keys declared in `## 🔵 Output Schema` at the bottom of this file.

```yaml
# REQUIRED (must be top-level JSON keys):
case_id: DI-YYYYMMDD-XXX
subject:
  name: <Name>
  title: <Title>
  organization: <Organization>
  legal_identity: <Step 0b Verification Result>
  party_member: <Yes/No/Unknown>
issues: [<Primary Issue 1>, <Issue 2>, ...]
timeframe: <Start-End Date>
regulation_list:
  - <Full regulation name 1>
  - <Full regulation name 2>
task_type: full  # ⛔ MUST be one of: full | interview | quick

# OPTIONAL (enrichment fields, not required by Schema):
risk_level: <High/Medium/Low>
key_articles: [<Relevant Legal Provisions>]
agent_chain: scope → (search-rg ∥ search-pkulaw) → merge → audit → analyze → draft → review → revise → publish
regulation_list_source: "Step 0b verification result + case type inference"
```

## Step 5 Launch Pipeline
- Generate scope.json for handoff to Agent 1
- scope.json contains Step 0b verification records (rg commands + results)
- Annotate the source path of legal_identity

---

## 🔵 Output Schema (v2.4)

Pipeline gate validates these required fields before passing to Agent 1:

```json
{
  "required": ["case_id", "subject", "issues", "timeframe", "regulation_list", "task_type"],
  "subject": { "required": ["name", "legal_identity", "party_member"] },
  "regulation_list": { "minItems": 1 },
  "task_type": { "enum": ["full", "interview", "quick"] }
}
```

Gate failure → mark Agent 0 FAILED, write `pipeline_failure_log.json`, do NOT proceed.

---

## 🎯 Execution Tuning (v2.4)

> Lessons from real case execution that tune this agent's behavior. Populated by monthly cron from `_lessons.json`.
> Format: `DI-YYYYMMDD-seq: finding → adjustment`

<!-- TUNING_START -->
(No execution tuning records yet. Monthly cron will inject from _lessons.json.)
<!-- TUNING_END -->
