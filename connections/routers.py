from fastapi import APIRouter
from pin.views import router
from account.views import router as acrouter

routers = APIRouter()


routers.include_router(router, prefix="/pin")
routers.include_router(acrouter, prefix="/user")
