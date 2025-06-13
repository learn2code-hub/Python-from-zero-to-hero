from src.services.db_service import get_todos, add_todo
from flask import blueprints, jsonify, request
import jsonpickle

todo_blueprint = blueprints.Blueprint('todo', __name__)

@todo_blueprint.route('/todos', methods=['GET'])
def get_todos_list():
    todos = get_todos()
    #json_data = json.dumps(todos, default=lambda o: o.__dict__, indent=4)
    #json_data = jsonpickle.encode(todos)
    json_data = [x.to_json_dict() for x in todos]
    return jsonify(json_data)

@todo_blueprint.route('/todos', methods=['POST'])
def post_todo():
    # get ToDo from request
    todo = request.get_json()
    new_todo = add_todo(todo["task"])
    return jsonify(new_todo.to_json_dict())



