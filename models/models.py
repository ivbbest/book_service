from sqlalchemy import Column, Integer, String
from database.configuration import Base

class User(Base):
    """
    User class
    Args:
        Base (sqlalchemy.ext.declarative.api.Base): Base class
    """

    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)