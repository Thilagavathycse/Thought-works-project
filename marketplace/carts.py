from flask import session, Blueprint
from models import *
# coding=UTF-8
from app import *
carts_pb = Blueprint('carts_pb', __name__)


@carts_pb.route('/cart', methods=['POST'])
@token_required
def add_item_to_cart():
    item_identity = request.form.get('item_id')
    user_identity = request.form.get('user_id')
    required_quantity = request.form.get('quantity')
    try:
        item_to_be_added = Cart(item_id=item_identity, user_id=user_identity, quantity=required_quantity)
        session.add(item_to_be_added)
        session.commit()
        return "Data added successfully"
    except Exception as error:
        return "error occurred while adding item to cart,Try again!"


@carts_pb.route('/cart', methods=['PUT'])
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
        return "Data updated successfully"
    except Exception as error:
        return "error occurred while updating item to cart,Try again!"


@carts_pb.route('/cart/<item_id>', methods=['DELETE'])
@token_required
def remove_item_from_cart(item_id):
    item_identity = item_id
    user_identity = request.form['user_identity']
    try:
        remove_item = session.query(Cart).filter_by(item_id=item_identity, user_identity=user_identity).one()
        session.delete(remove_item)
        return "deleted successfully"
    except Exception as error:
        return "error occurred while deleting item to cart,Try again!"


@carts_pb.route('/cart/<user_id>', methods=['GET'])
@token_required
def view_cart_items(user_id):
    for item, cart in session.query(Item, Cart).filter(Cart.user_id == user_id).all():
        return "Product ID: {} product Name: {} product price: {} quantity: {}".format(item.id, item.name,
                                                                                     item.price, cart.quantity)
