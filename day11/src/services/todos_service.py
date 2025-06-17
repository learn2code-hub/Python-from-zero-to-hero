from src.db import Session
from src.models.todo import Todo


def get_todos():
    with Session() as session:
        todos = session.query(Todo).all()
        return todos

def get_todo(todo_id):
    with Session() as session:
        todo = session.query(Todo).get(todo_id)
        return todo

def add_todo(task):
    with Session() as session:
        todo = Todo(task=task, done=False)
        session.add(todo)
        session.flush()
        session.commit()
        session.refresh(todo)
        return todo

def add_todo_with_dto(task):
    with Session() as session:
        todo = Todo(task=task, done=False)
        session.add(todo)
        session.commit()
        todo_dto = todo.to_dict()
        return todo_dto