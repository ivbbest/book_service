import hashlib
import random
import string


def get_random_string(length=12):
    """ Генерирует случайную строку"""
    return "".join(random.choice(string.ascii_letters + string.punctuation) for _ in range(length))


def hash_password():
    """ Хеширует пароль с солью """
    salt = get_random_string()
    password = get_random_string()
    enc = hashlib.pbkdf2_hmac("sha256", password.encode(), salt.encode(), 100_000)
    return enc.hex()


def validate_password(password: str, hashed_password: str):
    """ Проверяет, что хеш пароля совпадает с хешем из БД """
    salt, hashed = hashed_password.split("$")
    return hash_password(password, salt) == hashed
#
#
# async def get_user_by_email(email: str):
#     """ Возвращает информацию о пользователе """
#     query = users_table.select().where(users_table.c.email == email)
#     return await database.fetch_one(query)
#
#
#
#
# async def create_user(user: user_schema.UserCreate):
#     """ Создает нового пользователя в БД """
#     salt = get_random_string()
#     hashed_password = hash_password(user.password, salt)
#     query = users_table.insert().values(
#         email=user.email, name=user.name, hashed_password=f"{salt}${hashed_password}"
#     )
#     user_id = await database.execute(query)
#     token = await create_user_token(user_id)
#     token_dict = {"token": token["token"], "expires": token["expires"]}
#
#     return {**user.dict(), "id": user_id, "is_active": True, "token": token_dict}
