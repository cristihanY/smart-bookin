from typing import Optional

from sqlmodel import Field
from app.db.base import UserBase
from datetime import datetime, UTC

class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    updated_at: Optional[datetime] = None