install:
	@echo "installing for dev environment"
	@.venv/bin/python -m pip install -e '.[dev]'

ipython:
	@.venv/bin/ipython

virtualenv:
	@.venv/bin/python -m pip -m venv .venv


