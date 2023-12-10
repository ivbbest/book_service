from fastapi import FastAPI
from fastapi.security import OAuth2PasswordRequestForm

from src.auth.schemas import UserCreate, UserBase
from src.auth.database import get_db
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from src.auth import crud, utils


app = FastAPI(title="Book service", version="0.0.1")


@app.post("/sign-up/", response_model=UserBase)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[UserBase])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=UserBase)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/auth")
async def auth(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.get_user_by_email(db, email=form_data.username)

    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")

    elif not utils.validate_password(
            password=form_data.password, hashed_password=user.password
    ):
        raise HTTPException(status_code=400, detail="Incorrect email or password")

    return {
        "detail": "Вход разрешен",
        "id": user.id,
        "username": user.email
    }
