from flask import Flask, request, jsonify,session
from sqlalchemy import create_engine


app = Flask(__name__)
app.secret_key = 'onlineshoppingproject'

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
    user_details = db.execute("SELECT * from users WHERE name= \'{}\'  and password= \'{}\'".format(username,password))
    data = user_details.fetchone()
    if data is None:
        return "user or password is wrong"
    else:
        return "logged in successfuly"


@app.route('/categories', methods=['GET'])
def display_categories():
    categories_name = db.execute("SELECT * FROM categories")
    formatted_result = [dict(row) for row in categories_name]
    return jsonify(formatted_result)


@app.route('/categories/<category_id>/')
def get_items(category_id):
    items = db.execute("select  items.id,items.name from categories "
                       "INNER JOIN items ON items.category_id=categories.id where category_id=\'{}\'".format(category_id))
    formatted_result = [dict(row) for row in items]
    return jsonify(formatted_result)


@app.route('/items/<id>/', methods=['GET'])
def get_items_details(id):
    details = db.execute("select items.id,items.name,sellers.name as seller_name,items.price,items.description from items inner "
                         "join sellers ON items.seller_id=sellers.id where items.id=\'{}\'".format(id))
    formatted_result = [dict(row) for row in details]
    return jsonify(formatted_result)

@app.route('/cart/<item_id>', methods=['POST'])
def add_item_to_cart(item_id):
    item_identity = item_id

    user_identity = request.form.get('user_identity')
    required_quantity = request.form.get('required_quantity')
    add_item = db.execute('insert into carts values(\'{}\',\'{}\',\'{}\')'.format(item_identity,user_identity,required_quantity))
    select_added_item = db.execute("select * from carts where item_id=\'{}\'".format(item_id))
    is_added = select_added_item.fetchone()
    if is_added is None:
        return "There is an error occured"
    else:
        return "Successfully added item to cart"

@app.route('/cart/<item_id>', methods=['PUT'])
def update_quantity(item_id):
    item_identity = item_id
    user_identity = request.form.get('user_identity')
    desired_quantity = request.form.get('required_quantity')
    update_item_quantity = db.execute('update carts set quantity= \'{}\' where item_id=\'{}\' and user_id=\'{}\''.format(desired_quantity,item_identity,user_identity))
    return "updated successfuy"

@app.route('/cart/<item_id>', methods=['DELETE'])
def remove_item_from_cart(item_id):
    item_identity = item_id
    user_identity = request.form.get('user_identity')
    remove_item = db.execute('delete * from carts where item_id=\'{}\' and user_id=\'{}\''.format(item_identity, user_identity))
    deleted_item = db.execute('select * from carts where item_id=\'{}\' and user_id=\'{}\''.format(item_identity, user_identity))
    deleted_item = deleted_item.fetchone()
    if deleted_item is None:
        return "item removed from cart successfully"
    else:
        return "There is an error occured"


@app.route('/cart/<item_id>', methods=['GET'])
def view_cart_items(item_id):
    item_identity = item_id
    user_identity = request.form.get('user_identity')
    if user_identity in session:
        cart_items = db.execute("select items.id,items.name,items.price,items.description from items inner join  carts on carts.item_id=items.id")
        cart_items = [formatted_result(row) for row in cart_items]
        return jsonify(cart_items)
    else:
        return "login required"

def formatted_result(row):
    return "product id: " + str(row.item_id) + " " + "product name: " + str(row.name)+ " "+"price :"+ str(row.price)

@app.route('/logout', methods=['DELETE'])
def logout():
    if 'name' in session:
        session.pop('name', None)
        return "Thank you ! logged out success fully"""


db = connect_db()
print("Database connected successfully")
if __name__ == "__main__":
    app.run(debug=True)

