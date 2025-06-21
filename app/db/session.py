# app/db/session.py
from typing import Any, Generator
from sqlalchemy import create_engine
from app.core.config import settings
from sqlalchemy.orm import sessionmaker, Session

SQLALCHEMY_DATABASE_URL = settings.sqlalchemy_database_url
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Generator[Session, Any, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()