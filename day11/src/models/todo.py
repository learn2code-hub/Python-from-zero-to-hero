from sqlalchemy import Column, Integer, String, Boolean
from src.db import BaseClass

class Todo(BaseClass):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True)
    task = Column(String(500), nullable=False)
    done = Column(Boolean, nullable=False, default=False)

    def to_dict(self):
        return {"id": self.id, "task": self.task, "done": self.done}

    def __repr__(self):
        return f"ToDo(id={self.id}, task={self.task}, done={self.done})"