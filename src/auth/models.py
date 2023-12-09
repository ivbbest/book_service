from sqlalchemy import Boolean, Column, Integer, String

from src.auth.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, nullable=False, unique=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
