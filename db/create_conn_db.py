import os

from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()


class Postgres_Loader:
    """Класс для подключения к базе данных"""

    config_db = {
        "drivername": "postgresql",
        "host": os.environ.get("DB_HOST"),
        "port": os.environ.get("DB_PORT"),
        "username": os.environ.get("DB_USER"),
        "password": os.environ.get("DB_PASSWORD"),
        "database": os.environ.get("DB_NAME"),
    }

    def __init__(self):
        self.engine = None
        self.model = declarative_base()
        self.__create_engine()
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def __create_engine(self) -> None:
        """Создание подключения к PostgreSQL"""

        self.engine = create_engine(URL(**Postgres_Loader.config_db))
        self.engine.connect()


DATABASE = Postgres_Loader()