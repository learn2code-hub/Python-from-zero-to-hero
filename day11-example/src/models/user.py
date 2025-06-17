from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.db import BaseClass

class User(BaseClass):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)

    todos = relationship("Todo", back_populates="user", cascade="all, delete-orphan")

    def to_dict(self):
        return {"id": self.id, "username": self.username}
