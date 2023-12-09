from sqlalchemy import Boolean, Column, Integer, String

from src.auth.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String)
    is_active = Column(Boolean, default=True)

#
# from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP
#
# metadata = MetaData()
#
# users = Table(
#     "user",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("email", String, nullable=False),
#     Column("username", String, nullable=False),
#     Column("password", String, nullable=False),
#     Column("registered_at", TIMESTAMP, default=datetime.utcnow),
# )
