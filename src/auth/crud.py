from sqlalchemy.orm import Session

from .models import User
from .schemas import UserCreate
from .utils import hash_password, get_random_string


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    salt = get_random_string()
    hashed_password = hash_password(user.password, salt)
    db_user = User(email=user.email, username=user.email, password=f"{salt}${hashed_password}")
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user
