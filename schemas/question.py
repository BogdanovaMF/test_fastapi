from datetime import datetime

from pydantic import BaseModel


class QuestionSchema(BaseModel):
    """Модель вопроса"""
    id: int
    question_id: int
    question: str
    answer: str
    created_at: datetime

    class Config:
        orm_mode = True