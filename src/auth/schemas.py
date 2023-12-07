from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    """ Проверяет sign-up запрос """
    email: EmailStr
    username: str
    password: str = Field(min_length=7)


class UserBase(BaseModel):
    """ Формирует тело ответа с деталями пользователя """
    id: Optional[int] = Field(primary_key=True)
    email: EmailStr
    username: str
    registered_at: datetime
