.PHONY: docs

install:
	python -m pip install uv 
	uv venv 
	uv pip install bs4 marimo -e .

pypi:
	uv build
	uv publish

docs:
	uv run marimo export html nbs/__init__.py --output docs/index.html
