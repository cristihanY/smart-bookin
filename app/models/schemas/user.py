from typing import List
from pydantic import BaseModel
from app.db.base import UserBase

class CreateUserRequest(UserBase):
    pass

class UserResponse(UserBase):
    id: int

class UserListResponse(BaseModel):
    people: List[UserResponse]
    total: int
