# DI Discipline Inspection Agent ⚔️ v3.0

> **AI-powered discipline inspection pipeline — four specialist agents covering the full case lifecycle.**
> 4 Specialist Agents · Phase-Relay Pipeline · Dual-Factor Analysis · 80-Point Quality Gate · L2 Data Never Leaves the Machine

---

## What's New in v3.0: From a 10-Agent Pipeline to Four Specialist Agents

Previous versions ran a monolithic 10-agent pipeline inside a single assistant. v3.0 splits the discipline-inspection capability into **four dedicated, always-on specialist agents** — each with its own model, context, skill set, and security boundary. Think of it as moving from "one general practitioner who does everything" to "four specialized departments on the same case pathway."

| Why | Benefit |
|:----|:--------|
| **Failure isolation** | One agent stuck/down only affects its own stage — the rest keep working |
| **Focused context** | Each agent only sees its stage's material — no cross-case pollution, lower token cost |
| **Clear accountability** | Which stage has a problem? Ask the corresponding specialist; independent audit per agent |
| **Structural security** | Every agent fails closed (no external fallback) — L2 case data has no egress path by construction |

## Four Specialist Agents

| Stage | Agent | Skill | Function |
|:-----:|:------|:-----:|:---------|
| ① | **CT — Clue Triage Specialist** | clue-triage | Lead intake & triage: multi-source verification, checkability analysis, four disposition types (close / shelve / consult-verify / interview & inquiry) |
| ② | **IO — Interview Outline Specialist** | interview-outline | Pre-interview preparation: four-stage question handbook built on four elements per question (what / why / follow-up / expected answer) with breakthrough design |
| ③ | **CD — Case Determination Specialist** | case-determination + case-evidence-argumentation | Determination & sentencing: violation+culpability dual-factor analysis, sentencing three questions, adversarial debate, eight-dimension review |
| ④ | **PD — Proposal Drafting Specialist** | proposal-drafting | Final recommendation document: five-part structure (facts / verification / determination / recommendation / clauses), gated by an 80-point quality score |

**Relay model**: CT → IO → CD → PD, phase by phase. Each stage's output is handed directly to the next; the next stage starts only after the previous one passes its acceptance check. This is a queue-style handover — not simultaneous deliberation.

## 30-Second Install

```bash
# 1. Ensure Hermes Agent is installed
hermes --version

# 2. Clone the DI skill
cd ~/AppData/Local/hermes/skills/
git clone https://github.com/meta-evo-creator/discipline-inspection-agent.git

# 3. Run verification
python skills/discipline-inspection-agent/scripts/di_check.py
```

See `✅ All checks passed` and you're ready. **Zero config — 3 core regulations built in.**

## Usage Modes (v3.0)

### Quick Consultation (joint foundation)

Ask the DI Agent directly:

> "A department director who is a Party member received a gift worth 800 USD from a vendor during a procurement process. Analyze the case."

### Phase Relay (full case)

Dispatch the case sequentially to the four specialists — each phase consumes the previous phase's product:

```
Lead → [CT] triage & disposition → [IO] interview handbook → [CD] determination & sentencing → [PD] recommendation document
```

### Safety by Construction

- All four agents run on the primary model tier (deep-analysis) with **empty fallback providers** — if the primary fails, the agent refuses rather than silently switching to a third-party model (fail-closed).
- **L2 case data stays on the local machine.** Only public-source collection is allowed to leave via designated, audited channels.
- Each agent holds only its own skills plus the shared regulation bases (local law library + citation verification) — no skill drift between specialists.

## Configuration (Optional)

```yaml
regulation_source: builtin  # builtin | wiki | web
wiki_path: ""               # WIKI regulation DB path (wiki mode)
pkulaw: disabled            # PKULaw version verification
ima:
  enabled: false            # IMA knowledge-base upload (local deployment)
```

## References

- `four-agent-fleet.md` — full v3.0 technical description: each specialist's structure, workflow, and sample artifacts (desensitized).
