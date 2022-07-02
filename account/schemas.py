from datetime import datetime
from typing import Optional
import uuid

from fastapi_users import schemas
from pydantic import BaseModel



class UserBase(schemas.BaseUser[uuid.UUID]):
    pass

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: str
    hashed_password: str
    is_active: bool
    is_superuser: bool
    is_verified: bool
    nickname: str
    date: Optional[datetime]

    class Config:
        orm_mode = True


class UserUpdate(schemas.BaseUserUpdate):
    pass

class UserDB(schemas.BaseOAuthAccount):
    pass