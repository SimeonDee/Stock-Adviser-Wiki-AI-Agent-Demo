import os
from dotenv import load_dotenv

from agno.agent import Agent
from agno.models.openai import OpenAIChat

from agno.tools.wikipedia import WikipediaTools
from agno.tools.yfinance import YFinanceTools
from agno.tools.reasoning import ReasoningTools

from agno.storage.sqlite import SqliteStorage
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
MODEL_NAME = os.getenv("OPENAI_DEFAULT_MODEL")

DB_URL = "tmp/test_agno_agent.db"

# Instructions/Prompt
with open("prompts/agent_prompt.txt", "r") as f:
    instructions = f.readlines()

# Storage for a single session store
session_storage = SqliteStorage(table_name="agent_sessions", db_file=DB_URL)

Memory
user_memory = Memory(
    db=SqliteMemoryDb(table_name="agent_users_memory", db_file=DB_URL),
    model=OpenAIChat(id=MODEL_NAME)
)

agent = Agent(
    user_id="user_1",
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
        WikipediaTools()
    ],
    storage=session_storage,
    memory=user_memory,
    add_context=True,
    add_history_to_messages=True,
    enable_agentic_memory=True,
)
