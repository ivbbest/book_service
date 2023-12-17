from fastapi import Depends
from sqlalchemy.orm import Session
from models.UserModel import User
from schemas.UserSchema import UserCreate
from src.auth.utils import hash_password, get_random_string
from configs.database import get_db


class UserRepository:
    db: Session

    def __init__(
            self, db: Session = Depends(get_db)
    ) -> None:
        self.db = db

    def get_user(self, user_id: int) -> User:
        return self.db.query(User).filter(User.id == user_id).first()

    def get_user_by_email(self, email: str) -> User:
        return self.db.query(User).filter(User.email == email).first()

    def get_users(self, skip: int = 0, limit: int = 100) -> list[User]:
        return self.db.query(User).offset(skip).limit(limit).all()

    def create_user(self, user: UserCreate) -> User:
        salt = get_random_string()
        hashed_password = hash_password(user.password, salt)
        db_user = User(email=user.email, password=f"{salt}${hashed_password}")
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)

        return db_user
