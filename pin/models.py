from core.db import Base
from account.models import User



from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship




class Pins(Base):
    __tablename__ = "pins"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String, index=True)
    text = Column(Text, index=True)
    author_id = Column(Integer, ForeignKey("user.id"))
    
    author = relationship("User")


pins = Pins.__table__