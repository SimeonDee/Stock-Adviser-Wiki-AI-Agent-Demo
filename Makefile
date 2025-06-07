# Define variables
APP_NAME = main.py
VENV_NAME = .venv
APP_MODULE_NAME = main

# Create a virtual env
venv:
	uv venv $(VENV_NAME)

# Activating virtual env
activate:
	source $(VENV_NAME)/bin/activate

# Install dependencies
install:
	uv pip install -r requirements.txt

# Run the python application:
run-python:
	python3 $(APP_NAME)

# Run the FastAPI app
run-fastapi:
	uvicorn $(APP_MODULE_NAME):app --reload --port 5000

# tests
test:
	pytest

# Clean resources
clean:
	rm -rf $(VENV_NAME)
	rm -rf __pychache__




