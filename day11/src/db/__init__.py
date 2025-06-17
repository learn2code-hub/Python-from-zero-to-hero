from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from src.config import Config

# Init BaseClass for ORM models
BaseClass = declarative_base()

# Init ORM engine and session
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, echo=False)
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False, expire_on_commit=True)
