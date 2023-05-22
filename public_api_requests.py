from typing import List

import requests

from schemas.question import QuestionSchema


def get_questions(count: int) -> List[QuestionSchema]:
    """Получение  и валидация вопросов"""

    get_query = requests.get(f"https://jservice.io/api/random?count={str(count)}")
    data = get_query.json()
    questions = []

    for question in data:
        question["question_id"] = question["id"]
        question_model = QuestionSchema(**question)
        questions.append(question_model)

    return questions
