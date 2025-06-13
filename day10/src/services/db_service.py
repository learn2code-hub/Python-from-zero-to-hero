from src.db.in_memory import todos
from src.models.todo import ToDo

def get_todos():
    return todos

def add_todo(task):
    new_id = max([x.id for x in todos]) + 1 if len(todos) > 0 else 1
    new_todo = ToDo(new_id, task, False)
    todos.append(new_todo)
    return new_todo

def get_todo(id):
    for x in todos:
        if x.id == id:
            return x
    return None

def delete_todo(id):
    for x in todos:
        if x.id == id:
            deleted_todo = x
            todos.remove(x)
            return deleted_todo
    return None
