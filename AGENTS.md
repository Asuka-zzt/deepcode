# Repository Guidelines

## Project Structure & Module Organization

This repository is currently a minimal scaffold: no application source, tests, or build manifest have been committed. Keep the root directory reserved for project-wide files such as `README.md`, dependency manifests, and CI configuration. When implementation begins, use a predictable layout:

- `src/` for production code, grouped by feature or domain.
- `tests/` for automated tests that mirror the `src/` structure.
- `assets/` for static fixtures, images, or sample data.
- `docs/` for architecture notes and longer operational guidance.

Do not commit editor-specific settings, generated output, dependency caches, or secrets.

## Build, Test, and Development Commands

No build or test toolchain is configured yet. Before submitting code, inspect the working tree with:

```bash
git status --short
git diff --check
```

When adding a language or framework, provide standard entry points such as `make test`, `npm test`, or `pytest`, and document the exact setup and run commands in `README.md`. Prefer reproducible commands over machine-specific scripts.

## Coding Style & Naming Conventions

Follow the formatter and linter native to the chosen language, and commit their configuration with the first source files. Use spaces rather than tabs unless the formatter requires otherwise. Choose descriptive names: `snake_case` for Python modules and functions, `camelCase` for JavaScript variables, and `PascalCase` for classes or exported types. Keep modules focused and avoid unrelated formatting changes in feature commits.

## Testing Guidelines

Every behavior change should include tests. Place tests under `tests/` or beside source files when that is the framework convention. Name tests after observable behavior, for example `test_rejects_invalid_token.py` or `auth.spec.ts`. Cover success paths, boundary conditions, and expected failures. Bug fixes should include a regression test.

## Commit & Pull Request Guidelines

There is no existing commit history to establish a local convention. Use concise, imperative subjects, preferably Conventional Commits such as `feat: add request parser` or `fix: reject empty input`.

Pull requests should explain the problem, summarize the approach, list verification commands, and link related issues. Include screenshots or sample output for user-visible changes. Keep each PR narrowly scoped and call out follow-up work explicitly.
