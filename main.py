from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response


from core.db import database
# from core.db import SessionLocal
from connections.routers import routers
# from core.fast_users import fastapi_users
from core.db import engine
from core.base import Base

app = FastAPI()

Base.metadata.create_all(bind=engine)



app.include_router(routers)
# app.include_router(fastapi_users.router, prefix="/users", tags=["users"])


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


# @app.middleware("http")
# async def db_session_middleware(request: Request, call_next):
#     response = Response("Internal server error", status_code=500)
#     try:
#         request.state.db = SessionLocal()
#         response = await call_next(request)
#     finally:
#         request.state.db.close()
#     return response