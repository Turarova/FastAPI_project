from core.db import Base


from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy_utils import URLType



class Pins(Base):
    __tablename__ = "pins"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String, index=True)
    description = Column(Text, index=True)
    author_id = Column(Integer, ForeignKey("user.id"))

    author = relationship("User", back_populates="pins")
    image = relationship("PinsImage", back_populates="pins")


class PinsImage(Base):
    __tablename__ = "pin_images"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    url = Column(URLType, nullable=True)
    name = Column(String, nullable=True)
    pins_id = Column(Integer, ForeignKey("pins.id"), nullable=False)

    pins = relationship("Pins", back_populates="image")