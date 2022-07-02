from passlib.context import CryptContext
from fastapi import APIRouter
from typing import List

from .schemas import *
from connections.db_connect import get_user_list, create_user

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str):
    return pwd_context.hash(password)

router = APIRouter()


@router.get("/", response_model=List[UserBase])
async def user_list():
    return await get_user_list()


@router.post("/", response_model=UserCreate)
async def user_create(item: UserCreate):
    return await create_user(item)