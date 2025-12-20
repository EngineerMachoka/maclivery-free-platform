# Import SQLModel to manage database models and sessions
from sqlmodel import SQLModel, create_engine, Session

# Define the database URL
# SQLite is used for the free version because it needs no setup
DATABASE_URL = "sqlite:///database.db"

# Create the database engine
# echo=True prints SQL queries for learning/debugging
engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    """
    Provides a database session.
    Used in every file that talks to the database.
    """
    return Session(engine)
