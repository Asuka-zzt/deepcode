# AGENTS.md

Entry-point instructions for all coding agents (Claude Code / Codex / Cursor / Aider / Gemini) working in this repo.

## 1. Project Overview

DeepCode is a coding agent (in the spirit of Claude Code / Codex), built in Python on top of LangGraph, using DeepSeek as the primary LLM. It is currently in the **design phase** — see `docs/design/概要设计.md` (overview, decisions D1–D30) and `docs/design/详细设计.md` (detailed design skeleton). No application code exists yet.

## 2. Tech Stack

- **Language**: Python
- **Env / packaging**: uv (Astral) — virtualenv + dependency management; project manifest in `pyproject.toml`.
- **Orchestration**: LangGraph (ReAct-style tool-calling loop). Avoid LangChain high-level abstractions (Chain / Agent executor); keep tight control of the agent loop.
- **LLM**: DeepSeek (OpenAI-compatible API) as primary, behind a provider abstraction that allows switching models.
- **Execution**: local subprocess execution + permission gating (no container by default; an OS-level sandbox is planned for phase 4). The `Executor` is an interface so an isolated backend can be added later.
- **CLI**: Rich (rendering) + prompt_toolkit (input).
- **Code intelligence**: tree-sitter (symbol index / repo-map).
- **Extensibility**: MCP (client, official Python SDK), Skill system.

## 3. Architecture

Layered (see 概要设计 §4 for the diagram):

- **CLI layer** — Rich + prompt_toolkit; slash-command subsystem (`/rag`, `/effort [low|medium|high|max|auto]`).
- **Orchestration (LangGraph)** — `agent` node ↔ `tool_executor` node (parallel tool calls), conditional edges, checkpointer for resume.
- **Tool layer** — `bash` (P0, local subprocess), `read`/`edit` (exact string replace + retry on mismatch), `grep`/`glob`, `symbol_*`; tool outputs are truncated to fit the context window.
- **Context / retrieval** — unified `Retriever` interface: TextRetriever + SymbolRetriever (phase 1), EmbeddingRetriever (phase 2); repo-map outline injected by default.
- **Provider layer** — DeepSeek adapter; abstraction supports multi-model and (phase 2) a vision model + an Architect planning model.

Phasing: phase 1 = foundation; phase 2 = retrieval/RAG, Architect mode, Hooks, Subagents, image input, web search; phase 3 = Git auto-commit, lint/test self-heal, explicit context, IDE plugin; phase 4 = optimizations (robust edit matching, PageRank repo-map, command-safety policy, OS-level sandbox, prompt caching, persistent memory). See 概要设计 §13.

## 4. Development Rules

### Design conventions
Design for the best architecture, implement with minimal changes. Before implementing a non-trivial feature, propose several solutions ordered by: (1) best performance / long-term architecture, (2) balanced, (3) simplest — each with a brief note on performance, complexity, dependencies, risks, trade-offs.

### Development conventions
Implement strictly to the approved design document, minimal-change principle:
- Keep changes small and focused; reuse existing code and dependencies.
- Do not rewrite unrelated modules, add unnecessary abstractions, or over-engineer.
- Follow existing project style.
- Do not add new dependencies/frameworks/services unless necessary. If a new dependency is required, **stop and ask first**, explaining why, alternatives, and costs.

### Code conventions
- Follow PEP 8; use type hints on public functions.
- Prefer small, single-purpose functions and modules; keep files reasonably small (split when a file grows past ~400 lines).
- Use clear, descriptive names; match the style of surrounding code.
- (Formatter/linter to be fixed once phase-1 scaffolding lands — see Common Commands.)

## 5. Documentation Rules

Design documents live under `docs/design/`. A design document should be concise and answer:
1. What problem is solved / what is implemented? 2. Why this solution? 3. Overall architecture? 4. How does it work? 5. Key data flows / APIs / state transitions? 6. Trade-offs, limits, risks? 7. Planned future improvements? 8. What tests were performed (added after tests exist)?

Prefer diagrams/flowcharts when they improve clarity. Avoid documenting details obvious from the code. Keep docs and code consistent — update affected docs together with the related change.

> Naming convention: the top-level design baselines keep their stable names `概要设计.md` / `详细设计.md`. New **incremental / topic-specific** design docs use `yyyy-mm-dd-xx.md` (date + short summary).

## 6. Workflow

Ask the user before running the full workflow.

- **Design first** — discuss requirements and create/update a design doc; do not start coding until the user approves the design.
- **Development branch** — create/switch to a dedicated branch; do not develop on `main` unless told to.
- **Incremental implementation** — small, logical steps; small focused commits, not monolithic ones.
- **Commit frequently** — commit each meaningful change (feature, fix, refactor, tests, docs, config); end commit messages with the Co-Authored-By trailer.
- **Testing** — run relevant tests before submitting; add/update tests; fix failures you introduce.
- **Human verification** — provide verification steps and ask the user to validate before considering a feature done.
- **CI/CD validation** — CI runs via `.github/workflows/ci.yml` (ruff lint + `ruff format --check` + pytest) on every push/PR to `main`. Before opening a PR, ensure local checks pass and do not bypass a failing CI run.
- **Pull request** — only commit/push when the user asks. Write the PR description following `.github/PULL_REQUEST_TEMPLATE.md` (Summary / Why / Implementation / Modified Files / Commits / Test).

## 7. Common Commands

Environment is managed with **uv**. These mirror what CI runs (`.github/workflows/ci.yml`). Run before pushing:

- Setup env: `uv sync` (installs project + dev deps from `pyproject.toml`)
- Lint: `uv run ruff check .`
- Format: `uv run ruff format .` (CI uses `ruff format --check .`)
- Test: `uv run pytest`
- Run app: `uv run python -m deepcode` *(planned — once phase-1 scaffolding lands)*

## 8. Important Constraints

- **`ref/`** contains third-party source (Claude Code / Codex / Aider) for reference only — gitignored. Read it to learn patterns; never modify it or treat it as project code.
- **Secrets** via environment variables (e.g. `DEEPSEEK_API_KEY`) or a local key file — never commit secrets.
- **Do not commit** local config: `.claude/settings.local.json`, `.agents-local/`, `AGENTS_LOCAL.md`.
- Edits to this `AGENTS.md` / a future `CLAUDE.md` may be made but should not be committed unless the user says otherwise.
- Keep this file under ~200 lines; move detailed rules into `.agents-local/rules/*.md` if it grows.
