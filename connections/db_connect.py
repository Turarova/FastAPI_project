from sqlalchemy.orm import Session
from account.schemas import UserCreate

from core.db import database
from pin.models import *
from pin.schemas import *
from account.models import *


async def get_pin_list():
    return await database.fetch_all(query=pins.select())


async def create_pin(item: PinCreate, user: User):
    pin = pins.insert().values(**item.dict(), user=user.id)
    return await database.execute(pin)





async def get_user_list():
    return await database.fetch_all(query=users.select())


async def create_user(item: UserCreate):
    us = users.insert().values(**item.dict())
    exec_ = await database.execute(us) 
    return item.dict()

