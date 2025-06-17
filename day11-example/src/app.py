from flask import Flask

from src.config import Config
from src.controllers.todo_controller import todo_blueprint
from src.db import BaseClass, engine, Session
from src.models.todo import Todo
from src.models.user import User
from src.models.tag import Tag


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register controller blueprints
    app.register_blueprint(todo_blueprint)


    # Only if the database has already a different structure
    #BaseClass.metadata.drop_all(bind=engine)

    # Init SQLAlechemy and create db
    BaseClass.metadata.create_all(bind=engine)
    seed_db()

    return app

def seed_db():

    with Session() as session:
        if session.query(Todo).count() == 0:
            demo_todos = [
                Todo(task="Init Project", done=True),
                Todo(task="Init Services", done=False),
                Todo(task="Test Project", done=False),
            ]

            print(demo_todos)
            session.bulk_save_objects(demo_todos)
            session.commit()
