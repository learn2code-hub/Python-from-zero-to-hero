from sqlalchemy import Table, Column, Integer, ForeignKey
from src.db import BaseClass

# relation table for Todo-Tags M-M relation

todo_tags = Table('todo_tags', BaseClass.metadata,
    Column('todo_id', Integer, ForeignKey('todos.id'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tags.id'), primary_key=True)
)
