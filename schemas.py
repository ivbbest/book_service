from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class User(BaseModel):
    id: Optional[int] = Field(primary_key=True)
    email: EmailStr
    username: str
    password: str = Field(min_length=7)
    registered_at: datetime
