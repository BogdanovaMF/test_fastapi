from sqlalchemy import Integer, String, Column, DateTime
from db.create_conn_db import DATABASE

Model = DATABASE.model


class Question(Model):
    """Создание модели таблицы вопроса в базе данных"""

    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, nullable=False)
    question_id = Column(Integer, index=True, unique=True)
    question = Column(String(300), nullable=False)
    answer = Column(String(300), nullable=False)
    created_at = Column(DateTime, nullable=False)