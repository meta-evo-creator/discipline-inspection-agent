# DI Discipline Inspection Agent ⚔️ v2.5.2

> **AI-powered discipline inspection pipeline — from case facts to interview outline, fully automated.**
> 10 Agents · Dual-Factor Analysis · 6-Dimension Scoring · Works Out of the Box

---

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

---

## Three Usage Modes

### Quick Consultation

Ask the DI Agent directly:

> "A department director who is a Party member received a gift worth 800 USD from a vendor during a procurement process. Analyze the case."

### Interview Outline

Provide case details, and the Agent auto-generates an interview handbook:

> "We received the following leads: 1. ... 2. ... 3. ... Draft an interview outline."

### Full Case Analysis

Standard 10-Agent full pipeline — regulation search → version verification → dual-factor analysis → adversarial debate → quality scoring → report generation.

---

## Configuration (Optional)

Edit `di-config.yaml`:

```yaml
regulation_source: builtin  # builtin | wiki | web
wiki_path: ""               # WIKI regulation DB path (wiki mode)
pkulaw: disabled            # PKULaw version verification
ima:
  enabled: false            # IMA knowledge base upload
  kb_id: ""
```

Default `builtin` mode requires zero configuration.

---

## Capabilities

| | builtin (free) | wiki + pkulaw (full) |
|:-----|:--:|:--:|
| Regulations | 3 core regulations | 45+ full texts |
| Version verification | ❌ | ✅ PKULaw authoritative |
| Guiding cases | ❌ | ✅ 11 CCDI cases |
| Common case patterns | ❌ | ✅ P01-P05 violation patterns |
| Knowledge graph | ❌ | ✅ 131 nodes / 136 edges |
| IMA upload | ❌ | ✅ |
| Analysis methodology | ✅ Dual-factor + 6-dimension scoring | ✅ Full suite |

---

## Documentation

- [Dual-Factor Analysis Methodology](METHODOLOGY.md) — Violation + culpability analysis framework
- [Configuration Reference](di-config.yaml) — All configurable options
- [Agent Pipeline Architecture](SKILL.md) — Complete 10-Agent specification

---

## License

MIT License
