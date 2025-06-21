# app/services/user_service.py

from sqlalchemy.orm import Session
from app.models.entity.user import User
from app.models.schemas.user import CreateUserRequest
from app.validations.user_validation import exist_user
from app.repository.user_repository import PersonRepository


class UserService:

    def __init__(self, db: Session):
        self.repository = PersonRepository(db)

    def find(self, user_id: int) -> User | None:
        exist_user(self, user_id)
        return self.repository.get_by_id(user_id)

    def list(self) -> list[type[User]]:
        return self.repository.get_all()

    def create(self, request: CreateUserRequest) -> User:
        return self.repository.create(request)

    def delete(self, user_id: int) -> bool:
        exist_user(self, user_id)
        return self.repository.delete(user_id)

