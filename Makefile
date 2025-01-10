install:
	@echo "installing for dev environment"
	@.venv/bin/python -m pip install -e '.[dev]'

virtualenv:
	@.venv/bin/python -m pip -m venv .venv
