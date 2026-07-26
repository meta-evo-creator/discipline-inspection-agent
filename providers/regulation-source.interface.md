# Regulation Source Interface v1.0

> **Pluggable Knowledge Source Interface Specification** — The DI skill pipeline decouples from the regulation data layer through this interface.
> Any Provider implementing this interface can drive the DI pipeline.

---

## Interface Definition

Each Provider declares its capabilities and configuration via `provider.yaml`:

```yaml
name: "provider-name"
version: "1.0"
description: "Brief description"

capabilities:
  regulation_search: true|false           # Supports full-text regulation search
  version_verification: true|false        # Supports regulation version/timeliness verification
  case_search: true|false                 # Supports guiding case retrieval
  methodology_access: true|false          # Supports methodology document access

degradation:
  missing_version_verification: "VERSION_UNVERIFIED | BLOCK | SKIP"
  missing_regulation_search: "BLOCK | USE_DEFAULT"
  note: "Describes degradation behavior when a capability is missing"

search:
  engine: "ripgrep | pkulaw-mcp | custom"
  base_path: "${VARIABLE}"               # Environment variable, resolved by the agent at parse time
  script: "path/to/script.py"            # (Optional) CLI script path
  scopes:                                # Search scope mapping
    discipline_laws: "${BASE}/discipline-laws"
    medical_laws: "${BASE}/medical"
    cases: "${BASE}/guiding-cases"
    methodology: "${BASE}/methodology"
```

---

## Capability Matrix

| Capability | Agent Consumer | Pipeline Behavior When Missing |
|:-----------|:---------------|:-------------------------------|
| `regulation_search` | Agent 1a (search-rg) | If `USE_DEFAULT` → falls back to default-provider; if `BLOCK` → pipeline refuses to start |
| `version_verification` | Agent 1b (search-pkulaw) | All regulations marked `VERSION_UNVERIFIED`, Agents 2/3 attach ⚠️ warnings |
| `case_search` | Agent 1a | Skipped, pipeline not blocked |
| `methodology_access` | Agent 1a / Agent 3 | Degraded: uses methodology references embedded in SKILL.md |

---

## Provider Selection Logic

At pipeline startup, the main session (or Agent 0) selects a Provider using the following priority:

```
1. Environment variable DI_REGULATION_PROVIDER specified → use designated provider
2. WIKI_PATH env var exists + wiki directory readable → use wiki-provider
3. pkulaw-mcp detected as available → layer on pkulaw-provider (version verification enhancement)
4. None of the above → use default-provider (built-in sample regulation pack)
```

Providers can be **stacked**:
- `wiki-provider` provides regulation search (Agent 1a)
- `pkulaw-provider` provides version verification (Agent 1b)
- Both are configured independently, with no mutual dependency

---

## Built-in Provider List

| Provider | Capability | Use Case |
|:---------|:-----------|:---------|
| **default-provider** | Regulation search (3 core regulations) + methodology | Out-of-the-box for open-source users / demo |
| **wiki-provider** | Full-text regulation search + case search (45+ regulations) | Institutions with a local WIKI regulation database |
| **pkulaw-provider** | Regulation version verification (currently effective/amended/abolished) | Institutions with a PKULaw subscription |

---

## Custom Providers

Users can create their own Provider:
1. Create a new directory under `providers/`
2. Write a `provider.yaml` (following the interface above)
3. Set the environment variable `DI_REGULATION_PROVIDER=your-provider-name`
4. The pipeline loads it automatically at startup

---

## Environment Variables

| Variable | Description | Default |
|:---------|:------------|:--------|
| `DI_REGULATION_PROVIDER` | Specifies the provider name | auto-detect |
| `WIKI_PATH` | Root path of the WIKI regulation database | (none) |
| `SKILL_DIR` | DI skill directory | auto-detected |
