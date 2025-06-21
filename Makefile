# Spotify Controller Makefile
# Provides common development tasks

.PHONY: setup clean run cli test lint format check setup

# Python and virtual environment settings
PYTHON := python3
VENV := venv
VENV_BIN := $(VENV)/bin
PIP := $(VENV_BIN)/pip
PYTHON_VENV := $(VENV_BIN)/python

# Create virtual environment
setup:
	$(PYTHON) -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

# Run interactive CLI
run:
	@echo "Starting Spotify Controller (Interactive Mode)..."
	$(PYTHON_VENV) cli.py

# Alias for run
cli: run

# Code formatting
format:
	@echo "Formatting code with black..."
	$(VENV_BIN)/black --line-length 88 --target-version py38 .
	@echo "Sorting imports with isort..."
	$(VENV_BIN)/isort --profile black .
	@echo "Code formatting complete!"

# Basic linting
lint: 
	@echo "Running basic linting with flake8..."
	$(VENV_BIN)/flake8 --max-line-length=88 --extend-ignore=E203,W503 \
		--exclude=.venv,__pycache__,.git \
		. || echo "Linting found some issues (non-blocking)"
	@echo "Linting complete!"

# Run tests
test: 
	@echo "Running tests..."
	@if [ -d "tests" ]; then \
		$(VENV_BIN)/pytest tests/ -v; \
	else \
		echo "No tests directory found. Create tests/ directory and add test files."; \
	fi

# Clean up
clean:
	@echo "Cleaning up..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	rm -rf .pytest_cache/
	rm -rf logs/*.log 2>/dev/null || true
	@echo "Cleanup complete!"