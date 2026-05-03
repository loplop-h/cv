<div align="center">

# Max Ernst Huisman Gutiérrez · CV

**Software engineer building production AI systems — from agent tooling to full-stack platforms.**

![role](https://img.shields.io/badge/role-AI%2FML_engineer-1F4E79?style=flat-square)
![location](https://img.shields.io/badge/location-Barcelona-1F4E79?style=flat-square)
![available](https://img.shields.io/badge/available-now-1A7F37?style=flat-square)
![python](https://img.shields.io/badge/python-3.11_%7C_3.12_%7C_3.13-3776AB?style=flat-square)
![mypy](https://img.shields.io/badge/mypy-strict-1F4E79?style=flat-square)
![license](https://img.shields.io/badge/license-MIT-007EC6?style=flat-square)

📄 [**Download CV (PDF)**](./cv-max-huisman.pdf)

</div>

---

```bash
$ whoami   → ai/ml engineer
$ location → ~/barcelona
$ status   → available now
```

|       |       |       |       |
|:------|:------|:------|:------|
| **4** | **350+** | **88%** | **25K+** |
| PyPI packages | Tests shipped | Branch coverage | Launch impressions |

---

## About

Shipped **four hot-fix releases in 48h** after rewind's launch — third-year engineering student at **La Salle Barcelona** maintaining four Python packages on PyPI for agentic AI workflows. Together they form a coherent toolkit: **observe** (rewind), **measure** (spent), **secure** (mcpguard), **audit** (debtx). Hot-fixes were triggered by a real-session smoke test that caught two Windows-only bugs CI had missed. mypy strict, multi-OS CI green, release notes treated like product changelogs.

**Open to AI/ML engineering roles in Barcelona — available now.**

---

## Contact

| | |
|--|--|
| **email** | [maxernstprojects@gmail.com](mailto:maxernstprojects@gmail.com) |
| **phone** | +34 666 459 920 |
| **github** | [github.com/loplop-h](https://github.com/loplop-h) |
| **linkedin** | [linkedin.com/in/maxernst-huisman](https://linkedin.com/in/maxernst-huisman) |
| **site** | [maxhuisman.space](https://maxhuisman.space) |

---

## Selected projects

### [`rewind`](https://github.com/loplop-h/rewind) — time-travel debugger for AI agent sessions

[![PyPI](https://img.shields.io/badge/PyPI-rewindx-1F4E79?style=flat-square)](https://pypi.org/project/rewindx/) ![version](https://img.shields.io/badge/version-v0.1.4-grey?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-007EC6?style=flat-square)

```bash
$ pip install rewindx
$ rewind cc setup
✓ Hooks installed in ~/.claude/settings.json
# Time-travel debugging is now active.
```

- ✓ Captures every prompt, tool call, file edit and cost into a per-session SQLite (WAL) + content-addressed blob store; enables timeline scrub, rollback, undo, privacy-masked Markdown export
- ✓ **141 tests · 88% branch coverage** · CI green on Python 3.11/3.12/3.13 across **Linux · macOS · Windows**
- ✓ Two production bugs caught only by a real-session smoke test — Windows cp1252 stdout crash and bash-on-Windows backslash escape — both shipped within 24h

`Python` `anyio` `Click` `Rich` `SQLite (WAL)` `content-addressed storage` `pytest` `ruff` `mypy strict`

---

### `STRATUM` — regulatory intelligence platform for pharma

[![site](https://img.shields.io/badge/site-maxhuisman.space-1F4E79?style=flat-square)](https://maxhuisman.space) ![status](https://img.shields.io/badge/status-live-1A7F37?style=flat-square)

- ✓ Full-stack AI platform extracting FDA Complete Response Letters & EMA objections for compliance teams — processed **28,961 FDA · 418 CRLs · 3,307 objections · 2,296 EMA** through NLP + graph knowledge representation
- ✓ Multi-store data model: **PostgreSQL** (relational), **Neo4j** (graph), **Weaviate** (vector) — multi-dimensional regulatory search across structured, semantic and relational dimensions

`Python` `FastAPI` `Next.js` `PostgreSQL` `Neo4j` `Weaviate`

---

### [`spent`](https://github.com/loplop-h/spent) — cost tracker for AI agent sessions

[![PyPI](https://img.shields.io/badge/PyPI-spent-1F4E79?style=flat-square)](https://pypi.org/project/spent/) ![version](https://img.shields.io/badge/version-v0.5.1-grey?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-007EC6?style=flat-square)

- ✓ Real-time terminal dashboard tracking AI session costs with model detection, per-model breakdown and token-level analysis
- ✓ **220+ tests** · launch post reached **25K+ impressions, 100+ engagements** on LinkedIn

`Python` `Rich` `SQLite` `JSONL` `agent hooks`

---

### [`mcpguard`](https://github.com/loplop-h/mcpguard) · [`debtx`](https://github.com/loplop-h/debtx)

| Project | What it does | PyPI |
|---------|--------------|------|
| [**mcpguard**](https://github.com/loplop-h/mcpguard) | OWASP MCP Top 10 security scanner via AST analysis | [`guardmcp`](https://pypi.org/project/guardmcp/) |
| [**debtx**](https://github.com/loplop-h/debtx) | A–F static-analysis grader for AI-generated code | [`debtx`](https://pypi.org/project/debtx/) |

---

## Stack

| | |
|---|---|
| **code** | `Python (4 yrs primary)`, `TypeScript`, `SQL` |
| **ai / ml** | LLM APIs, agent frameworks, `MCP`, RAG, NLP, prompt engineering |
| **backend** | `FastAPI`, `Next.js`, `anyio`, `Click`, `Rich` |
| **data** | `PostgreSQL`, `SQLite (WAL)`, `Neo4j`, `Weaviate` |
| **tooling** | `pytest`, `ruff`, `mypy strict`, multi-OS CI |

---

## Recent ships

| When | What |
|-----|------|
| **May 2026** | 🟠 First PR to [Anthropic's MCP SDK](https://github.com/modelcontextprotocol/python-sdk/issues/1933) — stdio fix · in review |
| **Apr 2026** | Launched **rewind v0.1.4** on PyPI — 4 hot-fix releases in 48h, all triggered by real-session smoke testing |
| **Mar 2026** | Shipped **spent v0.5.1** — launch post reached 25K+ impressions, 100+ engagements on LinkedIn |
| **Jan 2026** | Built **STRATUM** — regulatory-AI platform processing 28K+ FDA + 2.2K EMA documents |

---

## Currently

> **BUILDING** — `rewind v0.2`: making AI-agent sessions inspectable like git history
>
> **LEARNING** — [Designing Data-Intensive Applications](https://dataintensive.net/) · [use-the-index-luke.com](https://use-the-index-luke.com/) · [DeepLearning.AI ML Specialization](https://www.coursera.org/specializations/machine-learning-introduction)

## Process

> *Building the AI tooling I wish existed when I started.*

- ✓ **mypy strict** — types non-negotiable
- ✓ **Real-session smoke tests** — CI misses the bugs that bite users
- ✓ **Release notes as product changelogs** — every patch tells a story

---

## Education & Distinctions

**La Salle Barcelona — Universitat Ramon Llull** · 2023 — Present
Bachelor of Engineering in OTIC (ICT & Telecommunications) — *Year 3 of 4*

🏆 [**1st place — RSME National Mathematics Competition**](https://rsme.es/ganadores-de-los-concursos-del-dia-internacional-de-las-matematicas/), video category · *Día Internacional de las Matemáticas, 2020*

## Languages

| | | | |
|---|---|---|---|
| **Spanish** | `NATIVE` | **Catalan** | `NATIVE` |
| **English** | `C1` | **Dutch** | `B1` |

## Certifications

| | |
|---|---|
| **Machine Learning Specialization** | Stanford / DeepLearning.AI · 2026 |
| **Generative AI Engineering Professional** | IBM · 2026 |
| **Claude Code in Action** | Anthropic · 2026 |
| **Claude Certified Architect Foundations** | Anthropic · *In Progress* |

---

<sub><em>"Loplop" — Max Ernst's bird-form alter ego. The surrealist painter who is the namesake's namesake.</em></sub>
