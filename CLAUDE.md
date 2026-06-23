# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

`rl_framework` is a Python project bootstrapped from [rochacbruno/python-project-template](https://github.com/rochacbruno/python-project-template). It is currently a minimal package template with placeholder modules waiting for implementation.

## Common Commands

All development workflows are driven through the `Makefile`:

| Command | Purpose |
|---------|---------|
| `make virtualenv` | Create a `.venv` and install dev dependencies |
| `make install` | Install the package in editable mode with test extras |
| `make test` | Run `make lint` then `pytest` with coverage (xml + html) |
| `make lint` | Run `flake8`, `black --check`, and `mypy` |
| `make fmt` | Auto-format with `isort` and `black -l 79` |
| `make watch` | Run tests on every `.py` change (requires `entr`) |
| `make docs` | Build mkdocs site and open it in a browser |
| `make clean` | Remove `__pycache__`, `.pytest_cache`, build artifacts, etc. |
| `make release` | Interactive: bump `rl_framework/VERSION`, regenerate `HISTORY.md`, tag, and push |

### Running a single test

```bash
pytest -v tests/test_base.py
```

### Running tests without the lint step

```bash
pytest -v --cov-config .coveragerc --cov=rl_framework -l --tb=short --maxfail=1 tests/
```

## Architecture

This is a setuptools-based package (see `setup.py`). The package structure is flat:

```
rl_framework/
├── __init__.py      # (empty — exports belong here)
├── base.py          # Principal module for core classes/objects
├── cli.py           # CLI entry point (`rl_framework` console script)
├── __main__.py      # Enables `python -m rl_framework`
└── VERSION          # Plain-text semver (e.g., 0.1.0)
```

- **Console script**: `setup.py` registers `rl_framework = rl_framework.__main__:main`.
- **CI**: GitHub Actions (`.github/workflows/main.yml`) runs `linter` → `tests_linux` / `tests_mac` / `tests_win` on Python 3.9.
- **Coverage**: 100% coverage is expected for PRs; coverage reports are uploaded to Codecov.

## Development Conventions

- **Line length**: `79` (enforced by `black` and `flake8`).
- **Commits**: Use [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) (e.g., `feat(module): add something 🎉`).
- **Releases**: Semantic versioning. `make release` updates `rl_framework/VERSION`, regenerates `HISTORY.md` via `gitchangelog`, commits, tags, and pushes. GitHub Actions then publishes the release to PyPI (requires `PYPI_API_TOKEN` in repo secrets).
- **Changelog**: Only update `HISTORY.md` after the user confirms the branch's feature is complete and all commits are finalized. Use `gitchangelog` to generate the changelog entry.
- **Docs**: MkDocs with the `readthedocs` theme; source files live in `docs/`.

## pyproject.toml / Poetry

The project is currently managed with `setuptools` + `setup.py`. To switch to Poetry, run `make switch-to-poetry` (this moves `setup.py` and `requirements*.txt` to `.github/backup`).

## Branching & Commit Workflow

Follow the single-responsibility principle for every change:

1. Create a dedicated `feat/<description>` branch before editing (based on `dev`).
2. Make changes for **one** issue or feature only.
3. Commit incrementally as work progresses — you do not need to finish everything before committing. Push to origin after each meaningful commit.
4. **Wait for explicit user confirmation** that the current branch's feature is complete.
5. After confirmation, switch back to `dev` and pull the latest remote changes before starting the next feature:
   ```bash
   git checkout dev
   git pull origin dev
   git checkout -b feat/<next-feature>
   ```

Do **not** batch unrelated fixes or features into the same branch or commit. Do **not** auto-switch branches — always ask the user first.

## Code Review Workflow

After making any code changes, always run a self-review before returning to the user:

1. Trigger the `code-review` skill (or `simplify` skill) against the current diff.
2. Address any findings flagged by the review; do not skip correctness or cleanup issues.
3. Only once the review reports no issues (or only explicitly acceptable ones), return the final result to the user.
