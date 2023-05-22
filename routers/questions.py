from typing import List

from fastapi import APIRouter, Depends, status
from pydantic import parse_obj_as

from public_api_requests import get_questions
from repositories.question import QuestionRepository
from schemas.question import QuestionSchema


router = APIRouter(prefix="", tags=["main"])


@router.get("/", response_model=List[QuestionSchema])
def all_questions(q_limit: int = 10, questions: QuestionRepository = Depends()):
    """Получение всех вопросов"""
    db_questions = questions.all(q_limit=q_limit)
    return parse_obj_as(List[QuestionSchema], db_questions)


@router.post("/{question_num}", response_model=QuestionSchema, status_code=status.HTTP_201_CREATED)
def create_questions_in_db(question_num: int, questions: QuestionRepository = Depends()):
    """Создание уникальных вопросов в базе данных"""
    if question_num < 1:
        return []

    api_questions = all_questions(question_num)

    check_results = questions.check_find_result(api_questions)
    while check_results["missing"] > 0:
        api_questions = get_questions(check_results["missing"])
        check_results = questions.check_find_result(api_questions)

    return QuestionSchema.from_orm(check_results["last_question"])