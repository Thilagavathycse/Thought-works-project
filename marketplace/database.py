
from flask import Flask,jsonify
from sqlalchemy import create_engine
import jwt
from jwt import PyJWT
import datetime
from functools import wraps


app = Flask(__name__)


def connect_db():
    db_connection_string = "postgresql://postgres:#Thilaga1094@localhost:5432/online_shopping"
    return create_engine(db_connection_string)
@app.route('/')
def index():
    return "welcome to online shopping", 200
db = connect_db()
print("Database connected successfully")
if __name__ == "__main__":
    app.run(debug=True)
