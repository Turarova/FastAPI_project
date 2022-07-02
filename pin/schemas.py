from typing import Optional
from pydantic import BaseModel
from account.schemas import UserBase




class PinCreate(BaseModel):
    title: str
    text: str

    class Config:
        orm_mode = True

class PinBase(PinCreate):
    id: int
    user: UserBase