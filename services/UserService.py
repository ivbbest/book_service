from fastapi import Depends
from models.UserModel import User
from schemas.UserSchema import UserCreate
from repositories.UserRepository import UserRepository


class UserService:
    userRepository: UserRepository

    def __init__(
            self, userRepository: UserRepository = Depends()
    ) -> None:
        self.userRepository = userRepository

    def get_user(self, user_id: int) -> User:
        return self.userRepository.get_user((User(email=user_id)))

    def get_user_by_email(self, email: str) -> User:
        return self.userRepository.get_user_by_email(User(email=email))

    def get_users(self, skip: int = 0, limit: int = 100) -> list[User]:
        return self.userRepository.get_users(skip, limit)

    def create_user(self, user: UserCreate) -> User:
        return self.userRepository.create_user(
            User(email=user.email, password=user.password)
        )
