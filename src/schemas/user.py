from pydantic import BaseModel


class User(BaseModel):
    fullname: str = ""
    email: str = ""


class UserCreate(User):
    password: str


class UserWithID(User):
    id: int


class UserLogin(BaseModel):
    email: str
    password: str
