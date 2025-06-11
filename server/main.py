from typing import List

from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy import and_

from agno.agent import RunResponse
from server.src.agent import agent

from server.src.schemas.query import Query
from server.src.schemas.user import (
    User,
    UserWithID,
    UserLogin,
    UserCreate,
)

from server.src.models.user import Users
from server.src.config.db import conn
from server.src.middlewares.middlewares import ensure_auth


app = FastAPI()


@app.get("/health")
async def health_check() -> dict:
    return {"Health": "Ok"}


@app.get("/users")
async def get_users() -> List[UserWithID]:
    return conn.execute(Users.select()).all()


# Register new user
@app.post("/users/register")
async def register_user(user: UserCreate) -> UserWithID:
    existing_user = conn.execute(
        Users.select().where(
            Users.c.email == user.email,
        )
    ).one_or_none()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with that email already exists, kindly login",
        )
    new_user = {
        "fullname": user.fullname,
        "email": user.email,
        "password": user.password,
    }
    result = conn.execute(Users.insert().values(new_user))
    conn.commit()
    if result.is_insert:
        response = result.last_inserted_params()
        # print("Inserted ID", result.inserted_primary_key)
        response["id"] = result.inserted_primary_key[0]
        return response
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Bad Request: Failed registering user.",
        )


# Login user
@app.post("/users/login")
async def login_user(user: UserLogin) -> UserWithID:
    logged_in_user = conn.execute(
        Users.select().where(
            and_(
                Users.c.email == user.email,
                Users.c.password == user.password,
            )
        )
    ).one_or_none()
    if logged_in_user:
        return logged_in_user._asdict()
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
        )


# Login user
@app.get("/users/{user_id}")
async def get_user(user_id: int) -> User:
    found_user = conn.execute(
        Users.select().where(
            Users.c.id == user_id,
        )
    ).one_or_none()
    if found_user:
        return found_user._asdict()
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found.",
        )


@app.post("/run/{user_id}")
async def run_agent(
    user_id: int,
    query: Query,
    current_user: User = Depends(ensure_auth),
):
    agent.user_id = current_user.email
    response: RunResponse = agent.run(
        message=query.message,
        user_id=current_user.email,
    )

    return {"response": response.content}
