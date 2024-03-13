from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Index
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from .db import Base

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String(64))
    user_token = Column(String(16), unique=True)

    documents = relationship("Document", back_populates='owner')

class Document(Base):
    __tablename__ = 'documents'

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(50))
    contents = Column(String(2000), nullable=True)
    created_at = Column(DateTime(), server_default=func.now())
    updated_at = Column(DateTime(), onupdate=func.now())
    owner_id = Column(Integer, ForeignKey("user.id"))

    owner = relationship('User', back_populates='documents')





