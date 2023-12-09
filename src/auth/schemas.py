from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr

    class Config:
        orm_mode = True