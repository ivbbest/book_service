from typing import Optional

from pydantic import BaseModel, EmailStr


class User(BaseModel):
    name: str
    email: EmailStr
    password: str


class ShowUser(BaseModel):
    name: str
    email: EmailStr
    blogs: list = []

    class Config:
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str
