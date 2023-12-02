from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

import configparser


config = configparser.ConfigParser()
config.read('config.ini')


Base = declarative_base()

# Создаем объект Engine, который будет использоваться объектами ниже для связи с БД
engine = create_engine(URL.create(**config))
# Метод create_all создает таблицы в БД , определенные с помощью  DeclarativeBase
Base.metadata.create_all(engine)
# Создаем фабрику для создания экземпляров Session. Для создания фабрики в аргументе
# bind передаем объект engine
Session = sessionmaker(bind=engine)
# Создаем объект сессии из фабрики Session
session = Session()