from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from usee import User
from flask_sqlalchemy import SQLAlchemy
import psycopg2


app = Flask(__name__)

def connect_db():
    db_connection_string = "postgresql://postgres:#Thilaga1094@localhost:5432/online_shopping"
    return create_engine(db_connection_string)
@app.route('/')
def index():
    return 'Welcome to online shopping'

@app.route('/user', methods=['POST'])
def validate_user():
    username = request.form['username']
    password = request.form['password']
    user_details = db.execute("SELECT * from purchase.users WHERE name= \'{}\'  and password= \'{}\'".format(username,password))
    data = user_details.fetchone()
    if data is None:
        return "user or password is wrong"
    else:
        return "loggeded in successfuly"


@app.route('/categories', methods=['GET'])
def display_categories():
    categories_name = db.execute("SELECT * FROM purchase.categories")
    formatted_result = [dict(row) for row in categories_name]
    return jsonify(formatted_result)


@app.route('/categories/<category_id>/')
def get_items(category_id):
    items = db.execute("select  items.item_id,items.item_name from purchase.categories "
                       "INNER JOIN purchase.items ON items.category_id=categories.id where category_id=\'{}\'".format(category_id))
    formatted_result = [dict(row) for row in items]
    return jsonify(formatted_result)


@app.route('/categories/<category_id>/<item_id>/')
def get_items_details(item_id , category_id):
    details = db.execute("select items.item_id,items.item_name,sellers.name as seller_name,items.price,items.description from purchase.items inner "
                         "join purchase.sellers ON items.seller_id=sellers.id where item_id=\'{}\'".format(item_id))
    formatted_result = [dict(row) for row in details]
    return jsonify(formatted_result)


db = connect_db()


print("Database connected successfully")
if __name__ == "__main__":
    app.run(debug=True)

