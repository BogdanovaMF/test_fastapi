from fastapi import FastAPI

from db.create_conn_db import DATABASE
from routers import questions

DATABASE.model.metadata.create_all(bind=DATABASE.engine)

app = FastAPI()
app.include_router(questions.router)