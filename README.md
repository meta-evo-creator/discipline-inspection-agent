# Discipline-Inspection ⚔️ v2.0

> **Discipline as the yardstick. Constant vigilance.** 9-Agent parallel pipeline (1a∥1b) × Dual-Round Adversarial Debate × Case Structured Index (11 cases) × 6 Enhancement Modules × 24-Character Guideline scoring.

An AI-powered case analysis engine for party discipline inspection: feed in case facts → parallel regulation search + version verification → merge → audit → dual-round adversarial analysis with case matching → draft → review → finalized output.

---

## 🚀 Quick Start

### Out-of-the-box (demo mode)

```bash
git clone https://github.com/meta-evo-creator/discipline-inspection-agent.git
cd discipline-inspection-agent
# No configuration needed — default knowledge pack includes 3 core regulations
```

Feed case facts into Agent 0 (Scope). The pipeline runs automatically. Output includes ⚠️ version-unverified markers.

### Production use

```bash
# 1. Configure regulation database
export WIKI_PATH=/path/to/wiki/main/sources

# 2. (Optional) Configure version verification
# Install pkulaw-search skill + pkulaw-mcp service
```

With configuration, the pipeline unlocks 45+ regulations + PKULaw version verification.

---

## Three-Tier Value

| Tier | No Knowledge Source | Default Pack | Full WIKI + PKULaw |
|:--:|:--------------------|:-------------|:-------------------|
| 🥇 **Methodology** | ✅ Dual-factor / 24-char scoring | — | — |
| 🥈 **Pipeline Architecture** | ✅ 8-Agent Handoff / Guardrail Routing | — | — |
| 🥉 **Runnable Instance** | — | ✅ 3 regulation demo | ✅ 45+ regs + cases + version verify |

---

## Pipeline Architecture (v2.0)

```
Phase 0: Scope           → Problem framing (outputs regulation_list)
Phase 1a ∥ 1b:           → Reg search + Version verification (PARALLEL)
Phase 1c: Merge          → 3-way merge of 1a + 1b
Phase 2: Audit           → Citation audit & cross-verification
Phase 3: Analyze         → ⭐ Dual-Round Adversarial Debate
                           Round 1: Prosecution analysis
                           Round 2: Defense challenge (3-point rebuttal matrix)
                           + ⭐ Case matching (11-case structured index)
Phase 4: Draft           → Report / interview outline (7 chapters incl. case refs)
Phase 5: Review          → 6-D scoring + debate completeness audit
Phase 6: Revise          → Fixes based on review
Phase 7: Publish         → Finalized output
```

**Guardrail-routed modes:**
- `full`: Case qualification / sanction recommendation (9 Agents)
- `interview`: Interview outline (6 Agents)
- `quick`: Regulation consultation / article lookup (5 Agents)

---

## Knowledge Source Architecture

The pipeline is decoupled from the regulation data layer via a **Provider interface**:

```
┌─────────────────────────────────────────┐
│         DI 8-Agent Pipeline             │
│  (methodology + analysis + scoring)     │
└──────────┬─────────────┬────────────────┘
           │             │
    ┌──────▼──────┐ ┌───▼──────────┐
    │ Regulation  │ │ Version      │
    │ Search      │ │ Verification │
    │ Provider    │ │ Provider     │
    └──────┬──────┘ └───┬──────────┘
           │             │
    ┌──────▼──────┐ ┌───▼──────────┐
    │ default     │ │ pkulaw       │
    │ wiki        │ │ (PKULaw)     │
    │ custom...   │ │              │
    └─────────────┘ └──────────────┘
```

See: [`providers/regulation-source.interface.md`](providers/regulation-source.interface.md)

---

## Dependencies

### Runtime
- **OpenClaw** — Agent pipeline runtime
- **ripgrep** (`rg`) — Full-text regulation search
- **Python 3** — pkulaw-search script (optional)

### Optional
| Dependency | Capability | Behavior When Missing |
|:-----------|:-----------|:----------------------|
| WIKI regulation DB (45+) | Full-text search, guiding cases | Degrades to 3 core regulations (demo) |
| pkulaw-mcp | Version/timeliness verification | All regulations marked VERSION_UNVERIFIED; pipeline not blocked |
| PKULaw subscription | Data source for pkulaw-mcp | Same as above |

---

## Directory Structure

```
discipline-inspection-agent/
├── SKILL.md                    # Full skill specification
├── README.md                   # This file
├── agents/                     # 9 Agent prompts
│   ├── scope.md
│   ├── search-rg.md
│   ├── search-pkulaw.md
│   ├── merge.md                # v1.5: parallel merge
│   ├── audit.md
│   ├── analyze.md              # v2.0: dual-round debate + case matching
│   ├── draft.md
│   ├── review.md
│   └── revise.md
├── providers/                  # Pluggable knowledge layer 🔌
│   ├── regulation-source.interface.md
│   ├── default/                # Bundled demo regulation pack
│   │   ├── provider.yaml
│   │   └── knowledge/
│   ├── wiki/                   # Local WIKI regulation DB adapter
│   │   └── provider.yaml
│   └── pkulaw/                 # PKULaw version verification adapter
│       └── provider.yaml
└── references/                 # Reference documents
    ├── scoring-matrix.md
    └── case-index.json         # v2.0: 11-case structured feature index
```

---

## Methodology (v2.2)

### Core Framework: Dual-Factor Analysis (violation + culpability)

> Source: CCDI Case Review Office — *Introduction and Connotation of "Disciplinary Reasoning"*

```
Violation (objective elements)  ×  Culpability (subjective elements)  =  Disciplinary Violation
├─ Conduct facts                   ├─ Mental state (intent / negligence)
├─ Legal basis                     ├─ Degree of knowledge
├─ Harm to protected interests     ├─ Motive / purpose
├─ Continuity (one-off vs. systemic) ├─ Post-conduct behavior
└─ Severity (amount, frequency,     └─ Identity overlay (party member /
   scope, consequences)                public official obligations)

Violation = Violation Elements Satisfied + Culpability Elements Satisfied + No Exculpatory Circumstances
```

### Enhancement Modules (6 core modules for DI)

Five system-thinking tools augment the base dual-factor analysis:

| Module | Tool | Question It Answers | Phase |
|:-------|:-----|:--------------------|:------|
| **M2: Market for Lemons** | Akerlof signaling theory | Can we distinguish compliance from violation signals? | Evidence verification |
| **M4: Four-Tier Accountability** | Layered culpability model | Which tier does the culpability belong to? | Deepened culpability judgment |
| **M6: Swiss Cheese Audit** ⭐ | Reason's accident causation | What latent conditions enabled the active failure? | Violation identification |
| **M7: Attribution Calibration** ⭐ | Fundamental attribution error | Is the reviewer exhibiting attribution bias? | Culpability judgment |
| **M8: Just Culture Refinement** ⭐ | Dekker's just culture algorithm | Human error, at-risk behavior, or reckless conduct? | Sanction calibration |
| **M9: Scapegoat Risk Audit** ⭐ | Organizational scapegoating | Is someone being unfairly singled out? | Pre-conclusion safeguard |

> ⭐ = Added in v2.0. M1 (Incentive Compatibility), M3 (Unintended Consequences), and Triple-Mirror Analysis moved to Compliance Analysis (CA) skill per v2.2 specialization.

### Operational Flow: 3 Stages × 11 Steps + Enhancement Nodes

```
Stage 1: Fact Finding
  S1 Violation ID → S1a Swiss Cheese Audit 🔍 → S2 Legal basis → S3 Validation

Stage 2: Enhanced Analysis
  S4 Culpability → S4a Attribution Calibration 🧠 → S5 Evidence chain
  S6 Lemons Signal Audit 📡 → S7 Four-Tier Accountability Mapping
  S8 Sanction range → S8a Just Culture Refinement ⚖️

Stage 3: Conclusion
  S9 Counter-argument → S9a Scapegoat Audit 🛡️ → S10 Scoring → S11 Output
```

### Key Features (v2.0)

**Dual-Round Adversarial Debate** — Agent 3 runs two rounds: Round 1 as prosecution (standard analysis), Round 2 as defense (role-switch, 3 strongest counterpoints). Each counterpoint assessed for validity and impact on conclusion. Prevents cognitive blind spots that single-pass analysis misses.

**Case Structured Index** — 11 CCDI guiding cases indexed by 7 feature dimensions (violation type, subject level, amount range, mental state, penalty severity). Agent 3 builds a case profile and matches against the index using rule-based similarity scoring — no ML required.

### 24-Character Guideline 6-Dimension Scoring

| # | Dimension | Weight | Description |
|:-:|:----------|:------:|:------------|
| 1 | Accurate characterization | 25% | Complete regulation citation? Exact text match? Three-element verification? |
| 2 | Clear facts | 20% | Complete behavioral chain? Temporal/spatial/financial linkage clear? |
| 3 | Solid evidence | 20% | Evidence inventory complete? Indirect evidence chain viable? |
| 4 | Appropriate disposition | 15% | Sanction range matches regulation and facts? Scenario matrix adequate? |
| 5 | Complete procedures | 10% | Interview procedures compliant? Rights/obligations disclosed? |
| 6 | Compliant process | 10% | Investigation strategy lawful? Evidence collection path legal? |

---

## License

This repository contains:
- Pipeline code / methodology / scoring framework: MIT License
- Regulation texts (`providers/default/knowledge/`): Sourced from publicly available Chinese government legal documents (public domain)
- Authoritative legal texts should be verified against official NPC/State Council publications

---

## Disclaimer

This tool produces **candidate references only**. It does not replace:
- Formal decisions of disciplinary committee meetings or approval procedures
- Professional judgment of discipline inspection officials
- Advice from qualified legal professionals

Users are responsible for independently verifying regulation version validity and factual accuracy.
