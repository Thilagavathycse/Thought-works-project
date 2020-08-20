from flask import session,request,jsonify,Flask
import os
import jwt
from jwt import PyJWT
import datetime
from database import *
from sqlalchemy.orm import sessionmaker
from functools import wraps
from models import *

app = Flask(__name__)
app.config['secret_key'] = os.urandom(50)
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message':'Token is missing'}), 403
        try:
            details = jwt.decode(token,app.config['secret_key'])
        except:
            return jsonify({'message':'Token is invalid'}), 403
        return f(*args, **kwargs)
    return decorated

@app.route('/user', methods=['POST'])
def validate_user():
    username = request.form['username']
    password = request.form['password']
    user_details = session.query(User).filter_by(name=username,password=password).first()
    if user_details:
        token = jwt.encode({'name': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},app.config['secret_key'])
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
@token_required
def get_items(category_id):
    items = session.query(Category).join(Item).filter(Category.id == category_id).all()
    formatted_result = [display(item) for item in items]
    return jsonify(formatted_result)
def display(item):
    return "id: "+str(item.id)+","+"name: "+str(item.name)

@app.route('/items/<id>/', methods=['GET'])
@token_required
def get_items_details(id):
    item_id = id
    item_details = session.query(Item).filter_by(id=item_id).one()
    formatted_result = [dict(row) for row in item_details]
    return jsonify(formatted_result)

@app.route('/cart', methods=['POST'])
def add_item_to_cart():
    item_identity = request.form.get('item_identity')
    user_identity = request.form.get('user_identity')
    required_quantity = request.form.get('required_quantity')
    try:
        item_to_be_added = Cart(item_id=item_identity, user_identity=user_identity, required_quantity=required_quantity)
        session.add(item_to_be_added)
        session.commit()
        return "Data added successfully"
    except Exception as error:
        return "Error occured"

@app.route('/cart', methods=['PUT'])
@token_required
def update_quantity():
    item_identity = request.form.get('item_identity')
    user_identity = request.form.get('user_identity')
    desired_quantity = request.form.get('desired_quantity')
    try:
        update_quantity = session.query(Cart).filter_by(item_identity=item_identity, user_identity=user_identity,
                                                    desired_quantity=desired_quantity).one()
        update_quantity.desired_quantity = desired_quantity
        session.add(update_quantity)
        session.commit()
        return "Data updated successfully",200
    except Exception as error:
        return "error occured",500

@app.route('/cart/<item_id>', methods=['DELETE'])
def remove_item_from_cart(item_id):
    item_identity = item_id
    user_identity = request.form['user_identity']
    try:
        remove_item = session.query(Cart).filter_by(item_id=item_identity, user_identity=user_identity).one()
        session.delete(remove_item)
        return "deleted successfully",200
    except Exception as error:
        return "error occured",str(error)

@app.route('/cart/<user_id>', methods=['GET'])
def view_cart_items(user_id):
    for item, cart in session.query(Item, Cart).filter(Cart.user_id == user_id).all():
        return "Product ID: {} product Name: {} product price: {} quantity: {}".format(item.item_id, item.name,
                                                                                     item.price, cart.quantity)

@app.route('/logout', methods=['DELETE'])
def logout():
    if 'name' in session:
        session.pop('name', None)
        session.pop('password', None)
    return "logged out successfully"

@app.route('/')
def index():
    return "<h1>WELCOME TO MARKET</h1>"


Session = sessionmaker(bind=db)
session = Session()

if __name__ == "__main__":
    app.run(debug=True)