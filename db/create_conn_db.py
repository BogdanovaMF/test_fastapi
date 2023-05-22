import os

import sqlalchemy.orm
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()


class Postgres_Loader:
    """Класс для подключения к базе данных"""

    drivername = "postgresql"
    host = os.environ.get("DB_HOST")
    port = 5435
    username = os.environ.get("DB_USER")
    password = os.environ.get("DB_PASSWORD")
    database = os.environ.get("DB_NAME")

    def __init__(self):
        self.engine = None
        self.model = sqlalchemy.orm.declarative_base()
        self.__create_engine()
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def __create_engine(self) -> None:
        """Создание подключения к PostgreSQL"""

        self.engine = create_engine(f'{self.drivername}://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}')
        self.engine.connect()


DATABASE = Postgres_Loader()