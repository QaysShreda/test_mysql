from .database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class DbUser(Base):
    __tablename__='user'
    id =Column(Integer,primary_key=True,index=True)
    username = Column(String(16))
    email= Column(String(16))
    password = Column(String(500))

