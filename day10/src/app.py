from flask import Flask, jsonify
from src.config import Config
from src.controllers.api_controller import api_blueprint
from src.controllers.todo_controller import todo_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    #register blueprint controllers
    app.register_blueprint(todo_blueprint)
    app.register_blueprint(api_blueprint)

    return app


todos = [
    {"id": 1, "task": "Install Flask", "done": False},
    {"id": 2, "task": "Change port", "done": False},
]




