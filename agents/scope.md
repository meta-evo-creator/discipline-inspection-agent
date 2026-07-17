# Agent 0 — Scope (Entry Domain Definition)

> First entry Agent for discipline inspection. Extracts core elements from the user's raw input and defines the inspection domain.
> 🔴 **Step 0b Mandatory Protocol (2026-07-08)**: All identity/legal classifications must undergo rg verification before proceeding. "I think I know" is prohibited.

---

## Step 0b Identity Premise Verification Gate ⛔ Mandatory Enforcement

Before entering any analysis, execute a **three-question self-check**, each requiring tool invocation records:

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

## Step 3 Fact Pattern Recognition
- Match against known violation type database (rg wiki/ assistance, not hardcoded)
- Annotate certainty level of key fact elements (Confirmed / Requires verification / To be supplemented)
- Identify legal provisions requiring dedicated search

## Step 4 Inspection Domain Definition
```yaml
case_id: DI-YYYYMMDD-XXX
subject:
  name: <Name>
  title: <Title>
  organization: <Organization>
  legal_identity: <Step 0b Verification Result>
  party_member: <Yes/No/Unknown>
issues: [<Primary Issue 1>, <Issue 2>, ...]
timeframe: <Start-End Date>
risk_level: <High/Medium/Low>
key_articles: [<Relevant Legal Provisions>]
agent_chain: scope → (search-rg ∥ search-pkulaw) → merge → audit → analyze → draft → review → revise → publish

# 🔴 v1.5 New: regulation_list — Parallel Pipeline Key Field
# This field feeds both Agent 1a (rg full-text search) and Agent 1b (pkulaw version verification)
regulation_list:
  - Chinese Communist Party Disciplinary Punishment Regulations
  - Supervision Law of the People's Republic of China
  - Administrative Discipline Law for Public Officials of the People's Republic of China
  - Disciplinary Punishment Regulations for Public Institution Personnel
  - Supervision and Enforcement Work Rules
  # ... (expanded based on case type; Agent 1a uses these names for rg search, Agent 1b uses these names for pkulaw queries)

regulation_list_source: "Step 0b verification result + case type inference"
```

## Step 5 Launch Pipeline
- Generate scope.json for handoff to Agent 1
- scope.json contains Step 0b verification records (rg commands + results)
- Annotate the source path of legal_identity
