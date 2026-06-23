Changelog
=========


(unreleased)
------------
- Docs(claude): add changelog update rule to conventions. [WanChengXue]

  - Specify that HISTORY.md should only be updated after feature confirmation
- Build(uv): remove setuptools artifacts and migrate Makefile to uv.
  [WanChengXue]

  - Delete setup.py, requirements.txt, requirements-test.txt, MANIFEST.in
  - Rewrite Makefile: replace pip/venv/ENV_PREFIX with uv run / uv sync
  - Remove obsolete targets: virtualenv, switch-to-poetry, init
  - drop --cov-config .coveragerc (coverage reads pyproject.toml now)
- Build(uv): migrate to uv with pyproject.toml. [WanChengXue]

  - Add pyproject.toml using hatchling build backend
  - Drop version constraints to resolve latest dependencies
  - Bump minimum Python to 3.13
  - Generate uv.lock with latest resolved versions
  - Update GitHub Actions CI to use astral-sh/setup-uv@v5
  - Update release workflow to use uv build and uv publish
- Merge pull request #8 from WanChengXue/feat/clean-unnecessary-files.
  [WanChengXue]

  cleanup(repo): remove template boilerplate and enrich .gitignore
- Cleanup(repo): remove template boilerplate and enrich .gitignore.
  [WanChengXue]

  Removed after project initialization:
  - ABOUT_THIS_TEMPLATE.md (template documentation)
  - .github/init.sh (template initialization script)
  - .github/rename_project.sh (template renaming script)
  - .github/workflows/rename_project.yml (one-time template workflow)

  Added to .gitignore:
  - Editor/IDE files (.idea, .vscode, *.swp, *.swo, *~)
  - OS files (.DS_Store, Thumbs.db)
- Merge pull request #7 from WanChengXue/feat/use-uv. [WanChengXue]

  docs(readme): add uv as the project package manager
- Docs(readme): add uv as the project package manager. [WanChengXue]

  - Add uv installation instructions
  - Update development section with uv-based workflow examples


0.1.2 (2021-08-14)
------------------
- Fix release, README and windows CI. [Bruno Rocha]
- Release: version 0.1.0. [Bruno Rocha]


0.1.0 (2021-08-14)
------------------
- Add release command. [Bruno Rocha]
