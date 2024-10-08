PIP := pip
PYTHON := python
BEHAVE := behave
PYCLEAN := pyclean

all: help
help:
	$(PYTHON) main.py --help

.PHONY: clean
clean:
	$(PYCLEAN) --verbose .

.PHONY: build
build:
	$(PYTHON) -m venv .venv
	$(PIP) install --no-cache-dir -r requirements.txt

.PHONY: deps
deps:
	$(PIP) install --no-cache-dir -r requirements.txt

.PHONY: test
test:
	$(BEHAVE) tests/apps/quickstore/backend/features
	$(BEHAVE) tests/apps/backoffice/backend/features/users
	$(BEHAVE) tests/apps/backoffice/backend/features/products
	$(PYTHON) -m unittest discover -s ./tests/contexts/backoffice/users -p '*Test.py'
	$(PYTHON) -m unittest discover -s ./tests/contexts/backoffice/products -p '*Test.py'

.PHONY: run/backoffice-backend
run/backoffice-backend:
	$(PYTHON) main.py --context backoffice-backend

.PHONY: run/quickstore-backend
run/quickstore-backend:
	$(PYTHON) main.py --context quickstore-backend