from typing import Optional

from sqlmodel import Field, SQLModel
from datetime import date, datetime, UTC
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class UserBase(SQLModel):
    first_name: str
    last_name: str
    email: str = Field(index=True, unique=True)
    phone: Optional[str] = None
    birth_date: Optional[date] = None
    gender: Optional[str] = None

    is_active: bool = True
    is_verified: bool = False
    role: Optional[str] = "user"

    last_login: Optional[datetime] = None
    profile_picture: Optional[str] = None
    address: Optional[str] = None