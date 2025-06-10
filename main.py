from fastapi import FastAPI

from agno.agent import RunResponse
from agent import agent
from schemas.query import Query

app = FastAPI()


@app.post("/run/{user_id}")
async def run_agent(user_id: str, query: Query):
    agent.user_id = user_id
    response: RunResponse = agent.run(
            message=query.message,
            user_id=user_id,
        )

    return {
        "response": response.content
    }
