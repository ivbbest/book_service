from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    """Тело запроса при регистрации пользователя"""
    email: EmailStr
    password: str = Field(min_length=7)

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    """ Тело ответа с деталями пользователя """
    id: int
    email: EmailStr
