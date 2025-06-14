# Define variables
APP_NAME = app
SERVER_FILE_NAME = main.py
VENV_NAME = .venv
APP_MODULE_NAME = main
HOST = 0.0.0.0
PORT = 5000


# installs "uv" and use it to Create a virtual env
venv:
	pip install uv
	uv venv $(VENV_NAME) -p 3.12.4 --allow-existing

# Activating virtual env (for linux and MacOS)
activate:
	source $(VENV_NAME)/bin/activate

# Activating virtual env (for Windows, Command Prompts users)
activate-windows:
	source $(VENV_NAME)\Scripts\activate.bat

# Activating virtual env (for Windows, PowerShell users)
activate-windows-ps:
	source $(VENV_NAME)\Scripts\activate.ps1

# Upgrade Python version
python-upgrade:
	uv venv -p 3.12.4 --allow-existing

# Deactivating virtual env
deactivate:
	deactivate

# Install dependencies
install:
	uv pip install -r requirements.txt

# Run the python application:
run-python:
	python3 $(SERVER_FILE_NAME)

# Run the Server (FastAPI) app in DEV mode
run-server:
	uvicorn $(APP_MODULE_NAME):$(APP_NAME) --host $(HOST) --port $(PORT) --reload

# Run the Server (FastAPI) app in PROD mode
run-server-prod:
	uvicorn $(APP_MODULE_NAME):$(APP_NAME) --host $(HOST)

# tests
test:
	pytest

# Clean resources
clean:
	rm -rf $(VENV_NAME)
	rm -rf __pychache__




