class Config:
    DATABASE="todos.db"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + DATABASE
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True