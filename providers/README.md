# Providers — Pluggable Knowledge Sources

The DI pipeline is decoupled from the regulation data layer via a Provider interface. Different users can drive the analysis pipeline with different knowledge sources.

## Quick Selection

| I want to... | Use This Provider | Requirements |
|:-------------|:-----------------|:-------------|
| Quick demo / trial | `default-provider` | None — works out of the box |
| Production use at an institution | `wiki-provider` | Local WIKI regulation database |
| Regulation version verification | `pkulaw-provider` | PKULaw subscription |

## Stacking Providers

Providers can be combined:
```
wiki-provider (regulation search) + pkulaw-provider (version verification)
```

Or used standalone:
```
wiki-provider alone → regulation search works; versions marked VERSION_UNVERIFIED
default-provider alone → 3 core regulations only; versions marked VERSION_UNVERIFIED
```

## Detection Priority

The pipeline auto-detects at startup — no manual configuration required:
1. Check `DI_REGULATION_PROVIDER` env var → use specified provider
2. Check `WIKI_PATH` → if set, enable wiki-provider
3. Check pkulaw-mcp → if available, stack pkulaw-provider
4. None of the above → use default-provider

## Custom Providers

Create your own knowledge source adapter:
1. Create a new directory under `providers/`
2. Write a `provider.yaml` following the interface in `regulation-source.interface.md`
3. Set `DI_REGULATION_PROVIDER=your-provider-name`

See: `regulation-source.interface.md`
