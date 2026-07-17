# Default Knowledge Pack

> ⚠️ This directory contains **sample regulations only**, for demo/testing the DI pipeline.
> **Do not use for real case analysis.** A full regulation database must be configured separately.

## Contents

| Content | Description |
|:--------|:------------|
| CPC Disciplinary Punishment Regulations (2023 revision) | Full text, 69KB |
| PRC Supervision Law (2024 amendment) | Full text, 36KB |
| PRC Law on Administrative Punishment for Public Officials (2020) | Full text, 28KB |
| Dual-Factor Analysis Framework (violation + culpability methodology) | Full text, 27KB |

Files are organized in `laws/` and `methodology/` subdirectories.

## How to Get the Full Regulation Database

### Option 1: Configure a WIKI Regulation Database (recommended)

If you have access to a compiled WIKI regulation database:
```bash
export WIKI_PATH=/path/to/wiki/main/sources
```
The pipeline automatically switches to wiki-provider (45+ regulations + 11 guiding cases).

### Option 2: Build Your Own Regulation Database

1. Download full regulation texts from official sources:
   - [National Database of Laws and Regulations](https://flk.npc.gov.cn/)
   - [CCDI Official Website](https://www.ccdi.gov.cn/fgk/)
   - [PRC Government Portal](https://www.gov.cn/)
2. Save regulations as Markdown files in the `laws/` directory
3. The pipeline searches them automatically via ripgrep

### Option 3: Configure PKULaw

If you have a PKULaw subscription:
1. Configure the `pkulaw-mcp` service
2. Install the `pkulaw-search` skill
3. The pipeline automatically layers on version verification capability

## Source Attribution

Regulation texts in this directory are sourced from publicly available Chinese government legal documents (public domain). For authoritative legal texts, always refer to official NPC/State Council publications.
