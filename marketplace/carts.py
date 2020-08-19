from main import *

@app.route('/cart', methods=['POST'])
@token_required
def add_item_to_cart():
    item_identity = request.form.get('item_identity')
    user_identity = request.form.get('user_identity')
    required_quantity = request.form.get('required_quantity')
    item_to_be_added = Cart(item_id=item_identity, user_identity=user_identity, required_quantity=required_quantity)
    session.add(item_to_be_added)
    session.commit()
    return "Data added successfully"

@app.route('/cart', methods=['PUT'])
@token_required
def update_quantity():
    item_identity = request.form.get('item_identity')
    user_identity = request.form.get('user_identity')
    desired_quantity = request.form.get('desired_quantity')
    update_quantity = session.query(Cart).filter_by(item_identity=item_identity, user_identity=user_identity,
                                                    desired_quantity=desired_quantity).one()
    update_quantity.desired_quantity = desired_quantity
    session.add(update_quantity)
    session.commit()
    return "Data updated successfully"

@app.route('/cart/<item_id>', methods=['DELETE'])
def remove_item_from_cart(item_id):
    item_identity = item_id
    user_identity = request.form['user_identity']
    remove_item = session.query(Cart).filter_by(item_id=item_identity, user_identity=user_identity).one()
    session.delete(remove_item)
    return "deleted successfully"

@app.route('/cart/<user_id>', methods=['GET'])
def view_cart_items(user_id):
    for item, cart in session.query(Item, Cart).filter(Cart.user_id == user_id).all():
        return "Product ID: {} product Name: {} product price: {} quantity: {}".format(item.item_id, item.name,
                                                                                     item.price, cart.quantity)
