from datetime import datetime

from pydantic import BaseModel


class QuestionModel(BaseModel):
    """Модель вопроса"""
    question_id: int
    question: str
    answer: str
    created_at: datetime

    class Config:
        orm_mode = True