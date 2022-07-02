from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime

from core.base import Base



class User(Base, SQLAlchemyBaseUserTable):

    id = Column(Integer, primary_key=True, index=True, unique=True)
    # password = Column(String, index=True)
    nickname = Column(String, unique=True)
    date = Column(DateTime)

users = User.__table__





# from typing import Collection
# from sqlalchemy.orm import relationship
# from pin.models import *



# class User(Base):
#     __tablename__ = "user"

    
#     email = Column(String, unique=True, index=True, nullable=False)
#     hashed_password = Column(String, nullable=False)
#     is_active = Column(Boolean, default=True)
#     is_superuser = Column(Boolean,default=False)
    
#     # pins = relationship("Pins", back_populates="author")
#     profile = relationship("Profile", back_populates="owner", uselist=False)



# class Profile(Base):
#     __tablename__ = "profile"

#     id = Column(Integer, primary_key=True, index=True, unique=True)
#     first_name = Column(String(50), nullable=False)
#     last_name = Column(String(50), nullable=False)
#     is_active = Column(Boolean, default=False)
#     user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

#     owner = relationship(User, back_populates="profile")  