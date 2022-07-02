from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from core.utils import get_db
from connections.db_connect import *
from pin.schemas import *
from account.models import *
# from core.fast_users import fastapi_users


router = APIRouter()


@router.get("/", response_model=List[PinBase])
async def pin_list():
    return await get_pin_list()


@router.post("/", response_model=PinCreate)
async def pin_create(item: PinCreate, user: User):
    return await create_pin(item, user)


# user: User = Depends(fastapi_users.get_current_active_user)


