# Define variables
APP_NAME = app
MAIN_FILE_NAME = main.py
VENV_NAME = .venv
APP_MODULE_NAME = main
HOST = 0.0.0.0
PORT = 5000

# Create a virtual env
venv:
	uv venv $(VENV_NAME)

# Activating virtual env
activate:
	source $(VENV_NAME)/bin/activate

# Deactivating virtual env
deactivate:
	deactivate

# Install dependencies
install:
	uv pip install -r requirements.txt

# Run the python application:
run-python:
	python3 $(MAIN_FILE_NAME)

# Run the FastAPI app in PROD mode
run:
	uvicorn $(APP_MODULE_NAME):$(APP_NAME) --host $(HOST)

# Run the FastAPI app in DEV mode
run-dev:
	uvicorn $(APP_MODULE_NAME):$(APP_NAME) --host $(HOST) --port $(PORT) --reload

# tests
test:
	pytest

# Clean resources
clean:
	rm -rf $(VENV_NAME)
	rm -rf __pychache__




