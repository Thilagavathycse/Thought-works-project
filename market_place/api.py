from flask import session, request, jsonify, Flask
import jwt
from jwt import PyJWT
import datetime
from database import *
from sqlalchemy.orm import sessionmaker
from functools import wraps
from models import *

app = Flask(__name__)
app.config['secret_key'] = 'onlineshoppingproject'
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message': 'Token is missing'}), 403
        try:
            details = jwt.decode(token, app.config['secret_key'])
        except:
            return jsonify({'message': 'Token is invalid'}), 403
        return f(*args, **kwargs)

    return decorated

@app.route('/')
def index():
    return "<h1>WELCOME TO MARKET PLACE</h1>"


@app.route('/user', methods=['POST'])
def validate_user():
    username = request.form['username']
    password = request.form['password']
    user_details = db.execute("SELECT * from users WHERE name= \'{}\'  and password= \'{}\'".format(username, password))
    data = user_details.fetchone()
    if data is not None:
        token = jwt.encode({'name': username, 'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=30)}, app.config['secret_key'])
        return jsonify({'token': token.decode('UTF-8'), 'message': 'logged in successfuly'}), 200
    else:
        return jsonify({'message': 'Sorry,cannot access: Unauthorized'}), 401


@app.route('/categories', methods=['GET'])
def display_categories():
    categories = session.query(Category).all()
    formatted_result = [display(row) for row in categories]
    return jsonify(formatted_result)


def display(row):
    return "id: "+str(row.id)+","+"name: "+str(row.name)


@app.route('/categories/<category_id>/', methods=['GET'])
def get_items(category_id):
    item_details = session.query(Item).join(Category).filter(Category.id == category_id).all()
    for item in item_details:
        return "Product ID: {} Product Name: {} ".format(item.id, item.name)


@app.route('/items/<item_id>/', methods=['GET'])
def get_items_details(item_id):
    item_details = session.query(Item).join(Seller).filter(Item.id == item_id).all()
    for row in item_details:
            return "product ID:{} product Name:{}  description:{}".format(row.id, row.name, row.price, row.description)


@app.route('/cart', methods=['POST'])
@token_required
def add_item_to_cart():
    item_id = request.form.get('item_id')
    user_id = request.form.get('user_id')
    quantity = request.form.get('quantity')
    item_to_be_added = Cart(item_id=item_id, user_id=user_id, quantity=quantity)
    session.add(item_to_be_added)
    session.commit()
    return "Data added successfully"

@app.route('/cart', methods=['PUT'])
@token_required
def update_quantity():
    item_id = request.form.get('item_id')
    user_id = request.form.get('user_id')
    quantity = request.form.get('quantity')
    update_quantity = session.query(Cart).filter_by(item_id=item_id, user_id=user_id).one()
    update_quantity.quantity = quantity
    session.add(update_quantity)
    session.commit()
    return "Data updated successfully"


@app.route('/cart/<item_id>', methods=['DELETE'])
@token_required
def remove_item_from_cart(item_id):
    item_id = item_id
    user_id = request.form['user_id']
    remove_item = session.query(Cart).filter_by(item_id=item_id, user_id=user_id).one()
    session.delete(remove_item)
    session.commit()
    return "deleted successfully"


@app.route('/cart/<user_id>', methods=['GET'])
@token_required
def view_cart_items(user_id):
    cart_items = db.execute("select items.id,items.name,items.price,items.description from items inner join  "
                            "carts on carts.item_id=items.id where user_id=\'{}\'".format(user_id))
    cart_items = [dict(row) for row in cart_items]
    return jsonify(cart_items)


@app.route('/logout', methods=['DELETE'])
def logout():
    if 'name' in session:
        session.pop('name', None)
        session.pop('password', None)
    return "logged out successfully"


Session = sessionmaker(bind=db)
session = Session()

if __name__ == "__main__":
    app.run(debug=True)
