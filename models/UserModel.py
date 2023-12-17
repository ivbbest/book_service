from sqlalchemy import Boolean, Column, Integer, String
from configs.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String)
    is_active = Column(Boolean, default=True)
