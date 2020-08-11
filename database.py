from flask import Flask
from sqlalchemy import create_engine
import psycopg2

app = Flask(__name__)
greet = "Welcome to flask"
db_connection_string = "postgresql://postgres:#Thilaga1094@localhost:5432/online_shopping"
def connect_db():
    db_connection_string = "postgresql://postgres:#Thilaga1094@localhost:5432/online_shopping"
    return create_engine(db_connection_string)

db = connect_db()

if __name__ == '__main__':
    app.run(debug=True)
