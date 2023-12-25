# Makefile for WeChat App

# Define the Python interpreter
PYTHON = python3

# Virtual environment settings
VENV_DIR = venv
VENV_ACTIVATE = $(VENV_DIR)/bin/activate

# Flask app settings
FLASK_APP = app.py
FLASK_PORT = 5000

# Dependencies
REQUIREMENTS_FILE = requirements.txt

.PHONY: setup run clean

setup: $(VENV_ACTIVATE)

# Create a virtual environment
$(VENV_ACTIVATE):
	$(PYTHON) -m venv $(VENV_DIR)
	@echo "Virtual environment created. Activate it with: source $(VENV_ACTIVATE)"

# Install dependencies
install: $(VENV_ACTIVATE)
	$(PYTHON) -m pip install -r $(REQUIREMENTS_FILE)

# Run the Flask app
run: install
	$(PYTHON) $(FLASK_APP)

# Clean up generated files
clean:
	rm -rf $(VENV_DIR) __pycache__ routes/__pycache__

# Help target to display available targets
help:
	@echo "Available targets:"
	@echo "  setup         - Create virtual environment"
	@echo "  install       - Install dependencies"
	@echo "  run           - Run the Flask app"
	@echo "  clean         - Clean up generated files"
	@echo "  help          - Display this help message"

# Default target
.DEFAULT_GOAL := help
