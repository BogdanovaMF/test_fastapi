from typing import Dict, List, Union

from fastapi.params import Depends
from sqlalchemy.orm import Session

from dependencies import get_db
from models.tables_models import Question
from schemas.question import QuestionSchema


class QuestionRepository:
    """Хранилище с вопросами"""

    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def all(self, q_limit: int = 100) -> List[Question]:
        query = self.db.query(Question)
        return query.limit(q_limit).all()

    def find(self, question_id: int) -> Question:
        query = self.db.query(Question)
        return query.filter(Question.question_id == question_id).first()

    def create(self, question: QuestionSchema) -> Question:

        question_db = Question(
            question_id=question.question_id,
            question=question.question,
            answer=question.answer,
            created_at=question.created_at,
        )

        self.db.add(question_db)
        self.db.commit()
        self.db.refresh(question_db)

        return question_db

    def check_find_result(self, questions: List[QuestionSchema]) -> Dict[str, Union[int, QuestionSchema]]:

        check_questions = {"missing": 0, "last_question": None}

        for question in questions:
            if self.find(question.question_id):
                check_questions["missing"] += 1
            else:
                check_questions["last_question"] = self.create(question)

        return check_questions
