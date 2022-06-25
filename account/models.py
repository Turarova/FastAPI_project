from typing import Collection
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from pin.models import *

from core.base import Base



class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    email = Column(String, unique=True, index=True, nullable=False)
    date = Column(DateTime)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean,default=False)
    
    # pins = relationship("Pins", back_populates="author")
    # profile = relationship("Profile", back_populates="owner", uselist=False)



class Profile(Base):
    __tablename__ = "profile"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    is_active = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    owner = relationship("User", back_populates="profile")  