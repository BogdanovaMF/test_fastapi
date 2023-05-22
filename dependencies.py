from sqlalchemy.orm import Session
from db.create_conn_db import DATABASE


def get_db() -> Session:
    db = DATABASE.SessionLocal()
    try:
        yield db
    finally:
        db.close()