import os

from agno.agent import Agent
from agno.models.openai import OpenAIChat

from agno.tools.wikipedia import WikipediaTools
from agno.tools.yfinance import YFinanceTools
from agno.tools.reasoning import ReasoningTools

from agno.storage.sqlite import SqliteStorage
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory

from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

MODEL_NAME = os.getenv("OPENAI_DEFAULT_MODEL")
SQLITE_DB_PATH = os.getenv("SQLITE_AGENT_STORE_DB_PATH")

# Instructions/Prompt
with open("src/prompts/agent_prompt.txt", "r") as f:
    instructions = f.readlines()

# Storage for a single session store
session_storage = SqliteStorage(
    table_name="agent_sessions",
    db_file=SQLITE_DB_PATH,
)

Memory
user_memory = Memory(
    db=SqliteMemoryDb(table_name="agent_users_memory", db_file=SQLITE_DB_PATH),
    model=OpenAIChat(id=MODEL_NAME),
)

agent = Agent(
    session_id="session_1",
    model=OpenAIChat(id=MODEL_NAME),
    instructions=instructions if instructions else "",
    tools=[
        ReasoningTools(add_instructions=True),
        YFinanceTools(
            stock_price=True,
            company_info=True,
            analyst_recommendations=True,
        ),
        WikipediaTools(),
    ],
    storage=session_storage,
    memory=user_memory,
    add_context=True,
    add_history_to_messages=True,
    enable_agentic_memory=True,
)
