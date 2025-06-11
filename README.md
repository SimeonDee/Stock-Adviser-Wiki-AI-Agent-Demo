# Stock-Adviser-Wiki-AI-Agent-Demo

A demo AI Agent, implemented using [Agno Agentic Framework](https://docs.agno.com/), equiped with `yfinance` and `wikipedia` tools that can provide stock data, analysis and recommendations, and answer user queries from wikipedia knowledge base.

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
12. `Streamlit`: The Client. Used to provide a simple user-facing interface for interacting with the agent.
13. `requests`: For making RESTful API request to the server from the client (Streamlit) App.

### Project management tools used
- `uv`: Fast and efficient package manager used for managing project dependencies.
- `Makefile`: For managing commands for creating and activating virtual envs, installing dependencies, running the app and clean-up, all in one place.

## Setup
- Clone repo
- Change directory into repo
- open terminal (Unix-based) or Command Prompt (Windows) or Powershell

### 1. Setup the Server

#### Create virtual environment
```bash
~ $ make venv
```

#### Activate virtual environment
- for Linux and MacOS users
```bash
~ $ make activate
```

- for Windows users
```bash
~ $ make activate-window
```

#### Install dependencies
```bash
(.venv) ~ $ make install
```

#### Start the FastAPI Server (to serve the agent)
- For PROD mode
```bash
(.venv) ~ $ make run-server
```

- For DEV mode
```bash
(.venv) ~ $ make run-server-dev
```

### 1. Setup the Client (Streamlit)

#### Start the client (Streamlit app)
```bash
(.venv) ~ $ make run-client
```
