# app/repository/user_repository.py

from sqlalchemy.orm import Session
from app.models.entity.user import User
from app.models.schemas.user import CreateUserRequest

class PersonRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[type[User]]:
        return self.db.query(User).all()

    def create(self, request: CreateUserRequest) -> User:
        user = User(**request.model_dump())
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_by_id(self, user_id: int) -> User | None:
        return self.db.query(User).filter_by(id = user_id).first()

    def delete(self, person_id: int) -> bool:
        user = self.get_by_id(person_id)
        if not user:
            return False
        self.db.delete(user)
        self.db.commit()
        return True
