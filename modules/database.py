from sqlalchemy import create_engine


def connect_db():
    database_connection_string = "postgresql://postgres:#Thilaga1094@localhost:5432/online_shopping"
    return create_engine(database_connection_string)


db = connect_db()
print("Database connected successfully")
