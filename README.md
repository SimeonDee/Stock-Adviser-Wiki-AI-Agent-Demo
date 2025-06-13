# Stock-Adviser-Wiki-AI-Agent-Demo

A demo AI Agent, implemented using [Agno Agentic Framework](https://docs.agno.com/), equiped with `yfinance` and `wikipedia` tools that can provide stock data, analysis and recommendations, and answer user queries from wikipedia knowledge base.

The Agent is provided as a `RESTful API service` implemented using `FastAPI` (see `server` dir of this repo). A user-facing Streamlit `client application` for interacting with the agent is also implemented in the [Stock-Adviser-Wiki-AI-Agent-Client](https://github.com/SimeonDee/Stock-Adviser-Wiki-AI-Agent-Client) repo.

## Contacts

`Adedoyin Simeon Adeyemi` | [LinkedIn](https://www.linkedin.com/in/adedoyin-adeyemi-a7827b160/)

## Tools and Tech Stack

1. `Agno`: is a full-stack framework for building Multi-Agent Systems and workflows with memory, knowledge and reasoning. Formerly known as `Phidata`. Visit [Agno docs here](https://docs.agno.com/introduction).
2. `openai`: OpenAI API for accessing ChatGPT LLM and resources.
3. `LLM model`: ChatGPT-4o
4. `yfinance`: A Yahoo Finance tool, an API used for stock data retrieval, advisory and analytics stock data API. An open-source tool that uses Yahoo's publicly available APIs.
5. `wikipedia`: A wikipedia tool for querying Wikipedia knowledge base.
6. `uv`: Python Package Manager, runs and installs tools published as Python packages.
7. `sqlalchemy`: is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL. Used for interacting with MySQL for agent users data management, and SQLite for Agent's session storage and memory for storing conversation histories.
8. `MySQL`: for agent users data management.
9. `SQLite`: For agent's memory and session storage of conversation histories.
10. `PyMySQL`: MySQL connector for Python.
11. `FastAPI`: Used to provide agent service as a RESTful API service.
12. `uvicorn`: FastAPI server.

### Project management tools used

- `uv`: Fast and efficient package manager used for managing project dependencies.
- `Makefile`: For managing commands for creating and activating virtual envs, installing dependencies, running the app and clean-up, all in one place.

## API Specs

- **BASE URL:** `http://localhost:5000`

---

### Routes

- GET `/docs`: API documentation and testing using Swagger-UI

- GET `/health`: Health check

  **_Response_**:

  ```json
  {
    "Health": "Ok"
  }
  ```

- GET `/users`: Fetch all registered agent users

  **_Response_**:

  ```json
  [
    {
      "fullname": "",
      "email": "",
      "id": 0
    }
  ]
  ```

- GET `/users/{user_id}`: Fetch details of a user with supplied `user_id`.

  **_Response_**:

  ```json
  {
    "fullname": "Sampple User Name",
    "email": "user@mail-server.com"
  }
  ```

- POST `/users/register`: Registers a new user

  **_Request Body_**:

  ```json
  {
    "fullname": "",
    "email": "",
    "password": "string"
  }
  ```

  **_Response_**:

  ```json
  {
    "fullname": "",
    "email": "",
    "id": 0
  }
  ```

- POST `/users/login`: Login a user

  **_Request Body_**:

  ```json
  {
    "email": "",
    "password": "string"
  }
  ```

  **_Response_**:

  ```json
  {
    "fullname": "",
    "email": "",
    "id": 0
  }
  ```

- POST `/agents/run/{user_id}`: Sends the query of user with `user_id` to the AI agent for processing.

  **_Request Body_**:

  ```json
  {
    "message": "user query"
  }
  ```

  **_Response_**:

  ```json
  {
    "fullname": "",
    "email": "",
    "id": 0
  }
  ```

## Setup

- Clone repo
- Change directory into repo dir
- Open terminal (Unix-based) or Command Prompt (Windows) or Powershell
- Install `uv` package manager if not already installed, using the command below:

  ```bash
  ~ $ pip install uv
  ```

### 1. Setup the Server

- Ensure the terminal/command prompt is opened
- Change directory into the `server` directory and follow the rest of the setup steps

  ```bash
  ~ $ cd server
  ```

#### Create virtual environment

```bash
~ server $ make venv
```

#### Activate virtual environment

- for Linux and MacOS users

  ```bash
  ~ server $ make activate
  ```

- for Windows (Command Prompts) users

  ```bash
  ~ server $ make activate-windows
  ```

- for Windows (PowerShell) users

  ```bash
  ~ server $ make activate-windows-ps
  ```

#### Install dependencies

```bash
(.venv) ~ server $ make install
```

#### Start the FastAPI Server (to serve the agent)

- For DEV mode

  ```bash
  (.venv) ~ server $ make run-server
  ```

- For PROD mode

  ```bash
  (.venv) ~ server $ make run-server-prod
  ```

### Test the Server API with Swagger-UI

- If running the server locally on "localhost"
- Visit `<BASE_URL>/docs` e.g. `localhost:5000/docs` to access the Swagger-UI for testing the agent API routes

### Test the server using a client

- Clone the [Client Repo here](https://github.com/SimeonDee/Stock-Adviser-Wiki-AI-Agent-Client)
- Follow the README instructions in the client repo to set-up the app.

## Teardown

### 1. Stopping the Server (FastAPI app)

- Navigate to the running client terminal
- Press `Cntrl` + `C` key combination to stop the client
- Navigate to the running server terminal
- Press `Cntrl` + `C` key combination to stop the client

### 2. Deactivate virtual envs

```bash
(.venv) ~ $ make deactivate
```

## Running the tests

```bash
(.venv) ~ $ make test
```

## Clean ups

Deletes the `.venv` and `__pycache__` directories

```bash
(.venv) ~ $ make clean
```
