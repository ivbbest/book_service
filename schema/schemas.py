from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str
    blogs: list = []

    class Config:
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str
