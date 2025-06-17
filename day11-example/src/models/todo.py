from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.db import BaseClass
from src.models.todo_tag import todo_tags

class Todo(BaseClass):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True)
    task = Column(String(500), nullable=False)
    done = Column(Boolean, nullable=False, default=False)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="todos")

    tags = relationship("Tag", secondary=todo_tags, back_populates="todos")

    def to_dict(self):
        return {"id": self.id, "task": self.task, "done": self.done}

    def __repr__(self):
        return f"ToDo(id={self.id}, task={self.task}, done={self.done})"