# To-Do
from fastapi import HTTPException, status, Request

from src.models.user import Users
from src.schemas.user import User
from src.config.db import conn


async def ensure_auth(request: Request) -> User:
    # extracting user_id from path
    user_id = request.path_params.get("user_id", None)
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Missing 'user_id' in path variable",
        )
    # Fetch user with id
    authenticated_user = conn.execute(Users.select().where(
        Users.c.id == int(user_id),
    )).one_or_none()
    # if not authenticated
    if authenticated_user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",

        )
    authenticated_user = authenticated_user._asdict()
    return User(
            fullname=authenticated_user.get("fullname"),
            email=authenticated_user.get("email")
        )
