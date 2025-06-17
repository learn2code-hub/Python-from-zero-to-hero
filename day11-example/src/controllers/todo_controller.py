from sys import dont_write_bytecode

from flask import blueprints, jsonify, request
from src.models.todo import Todo
from src.services.todos_service import get_todos, get_todo, add_todo, add_todo_with_dto
from src.services.todos_sql_service import get_all_todos

todo_blueprint = blueprints.Blueprint('todo', __name__)


@todo_blueprint.route('/todos', methods=['GET'])
def get_todos_list():
    # use method from todos_service based on ORM
    # todos = get_todos()

    # use method from todos_sql_service based on SQL plain query
    todos = get_all_todos()
    return jsonify([todo.to_dict() for todo in todos])


@todo_blueprint.route('/todos/<int:id>', methods=['GET'])
def get_todo_by_id(id):
    todo = get_todo(id)
    return jsonify(todo.to_dict())


# GET /todos/filter?id=5
@todo_blueprint.route('/todos/filter', methods=['GET'])
def get_todos_filter():
    todo_id = request.args.get('id')
    if todo_id:
        todo = get_todo(int(todo_id))
        return jsonify(todo.to_dict())
    else:
        return jsonify([])


@todo_blueprint.route('/todos', methods=['POST'])
def post_todo():
    # get ToDo from request
    todo = request.get_json()
    # new_todo = add_todo(todo["task"])
    new_todo = add_todo_with_dto(todo["task"])
    if isinstance(new_todo, Todo):
        return jsonify(new_todo.to_dict())
    else:
        return jsonify(new_todo)
