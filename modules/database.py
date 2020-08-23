from sqlalchemy import create_engine
import os


def connect_db():
    database_connection_string = os.environ.get('DATABASE_CONNECTION_STRING')
    return create_engine(database_connection_string)


db = connect_db()
print("Database connected successfully")

