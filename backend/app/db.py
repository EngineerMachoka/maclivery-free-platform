# backend/app/db.py
# This file handles database configuration and connections

# Import SQLModel (ORM) and database utilities
from sqlmodel import SQLModel, create_engine, Session

# Define database URL
# SQLite is a file-based database, requires NO server and is FREE
DATABASE_URL = "sqlite:///maclivery.db"

# Create a database engine
# The engine is responsible for communicating with the database
engine = create_engine(DATABASE_URL, echo=False)

def get_session():
    """
    Creates and returns a database session.
    A session is required whenever we read or write data.
    """
    return Session(engine)

def init_db():
    """
    Creates all database tables defined in models.py.
    This runs automatically when the API starts.
    """
    SQLModel.metadata.create_all(engine)
