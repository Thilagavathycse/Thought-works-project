from database import *
from flask import request, jsonify


@app.route('/cart', methods=['POST'])
def add_item_to_cart():
    if request. method == "POST":
        item_identity = request.form.get('item_id')
        user_identity = request.form.get('user_identity')
        required_quantity = request.form.get('required_quantity')
        add_item = db.execute('insert into carts values(\'{}\',\'{}\',\'{}\')'.format(item_identity, user_identity, required_quantity))
        select_added_item = db.execute("select * from carts where item_id=\'{}\'".format(item_identity))
        is_added = select_added_item.fetchone()
        if is_added is None:
            return "There is an error occured"
        else:
            return "Successfully added item to cart"

@app.route('/cart', methods=['PUT'])
def update_quantity():
    item_identity = request.form.get('item_id')
    user_identity = request.form.get('user_identity')
    desired_quantity = request.form.get('required_quantity')
    update_item_quantity = db.execute('update carts set quantity= \'{}\' where item_id=\'{}\' and user_id=\'{}\''.format(desired_quantity,item_identity,user_identity))
    return "updated successfuy"

@app.route('/cart/<item_id>', methods=['DELETE'])
def remove_item_from_cart(item_id):
    item_identity = item_id
    user_identity = request.form.get('user_identity')
    remove_item = db.execute('delete  from carts where item_id=\'{}\' and user_id=\'{}\''.format(item_identity, user_identity))
    deleted_item = db.execute('select * from carts where item_id=\'{}\' and user_id=\'{}\''.format(item_identity, user_identity))
    deleted_item = deleted_item.fetchone()
    if deleted_item is None:
        return "item removed from cart successfully"
    else:
        return "There is an error occured"


@app.route('/cart/<user_id>', methods=['GET'])
def view_cart_items(user_id):
    user_identity = user_id
    item_identity = request.form.get('item_id')
    # if user_identity in session:
    cart_items = db.execute("select items.id,items.name,items.price,items.description from items inner join  "
                            "carts on carts.item_id=items.id where user_id=\'{}\'".format(user_id))
    cart_items = [formatted_result(row) for row in cart_items]
    return jsonify(cart_items)
    #else:
        #return "login required"

def formatted_result(row):
    return "product id: " + str(row.item_id) + " " + "product name: " + str(row.name) + " "+"price :"+ str(row.price)


