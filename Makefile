.ONESHELL:

.PHONY: help
help:             ## Show the help.
	@echo "Usage: make <target>"
	@echo ""
	@echo "Targets:"
	@fgrep "##" Makefile | fgrep -v fgrep


.PHONY: show
show:             ## Show the current environment.
	@echo "Current environment:"
	@uv run python -V

.PHONY: install
install:          ## Install the project in dev mode.
	@uv sync --extra test

.PHONY: fmt
fmt:              ## Format code using black & isort.
	@uv run isort rl_framework/
	@uv run black -l 79 rl_framework/
	@uv run black -l 79 tests/

.PHONY: lint
lint:             ## Run pep8, black, mypy linters.
	@uv run flake8 rl_framework/
	@uv run black -l 79 --check rl_framework/
	@uv run black -l 79 --check tests/
	@uv run mypy rl_framework/

.PHONY: test
test: lint        ## Run tests and generate coverage report.
	@uv run pytest -v --cov=rl_framework -l --tb=short --maxfail=1 tests/
	@uv run coverage xml
	@uv run coverage html

.PHONY: watch
watch:            ## Run tests on every change.
	ls **/**.py | entr uv run pytest -s -vvv -l --tb=long --maxfail=1 tests/

.PHONY: clean
clean:            ## Clean unused files.
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '__pycache__' -exec rm -rf {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	@rm -rf .cache
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@rm -rf build
	@rm -rf dist
	@rm -rf *.egg-info
	@rm -rf htmlcov
	@rm -rf .tox/
	@rm -rf docs/_build

.PHONY: release
release:          ## Create a new tag for release.
	@echo "WARNING: This operation will create s version tag and push to github"
	@read -p "Version? (provide the next x.y.z semver) : " TAG
	@echo "$${TAG}" > rl_framework/VERSION
	@uv run gitchangelog > HISTORY.md
	@git add rl_framework/VERSION HISTORY.md
	@git commit -m "release: version $${TAG} 🚀"
	@echo "creating git tag : $${TAG}"
	@git tag $${TAG}
	@git push -u origin HEAD --tags
	@echo "Github Actions will detect the new tag and release the new version."

.PHONY: docs
docs:             ## Build the documentation.
	@echo "building documentation ..."
	@uv run mkdocs build
	URL="site/index.html"; xdg-open $$URL || sensible-browser $$URL || x-www-browser $$URL || gnome-open $$URL || open $$URL
