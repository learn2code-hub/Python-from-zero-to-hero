from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.db import BaseClass

class Tag(BaseClass):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    todos = relationship("Todo", secondary="todo_tags", back_populates="tags")

    def to_dict(self):
        return {"id": self.id, "name": self.name}
