.PHONY: docs

install:
	python -m pip install uv 
	uv venv 
	uv pip install bs4 marimo -e .

pypi:
	uv build
	uv publish

docs:
	marimo export html-wasm --mode edit demo.py --output docs
