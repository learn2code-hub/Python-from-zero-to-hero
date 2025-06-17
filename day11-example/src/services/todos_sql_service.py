import sqlite3
from src.config import Config
from src.models.todo import Todo


def get_connection():
    return sqlite3.connect(Config.DATABASE)


def get_all_todos():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT id, task, done FROM todos')
    todos = cursor.fetchall()
    connection.close()
    return [Todo(id=int(row[0]), task=row[1], done=bool(row[2])) for row in todos]


def get_todo_by_id(todo_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT id, task, done FROM todos WHERE id = ?', (todo_id,))
    todo = cursor.fetchone()
    connection.close()
    print(todo)
    return Todo(id=todo[0], task=todo[1], done=bool(todo[2]))


def add_todo(task):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO todos (task, done) VALUES (?, ?)", (task, True))
    connection.commit()
    todo_id = cursor.lastrowid
    connection.close()
    return get_todo_by_id(todo_id)
