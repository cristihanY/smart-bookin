# endpoints/user.py
from typing import Annotated
from app.db.session import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from app.services.user_service import UserService
from app.models.schemas.user import CreateUserRequest, UserResponse

router = APIRouter(prefix="/users", tags=["Users"])
session_db = Annotated[Session, Depends(get_db)]

@router.get("/", response_model=list[UserResponse])
def list_user(db: session_db):
    user_service = UserService(db = db)
    return user_service.list()

@router.post("/", response_model=UserResponse)
def create_user(request: CreateUserRequest, db: session_db):
    user_service = UserService(db = db)
    return user_service.create(request)

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: session_db):
    user_service = UserService(db = db)
    return user_service.find(user_id)

@router.delete("/{user_id}", response_model=bool)
def delete_user(user_id: int, db: session_db):
    user_service = UserService(db =db)
    return user_service.delete(user_id)