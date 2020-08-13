
from database import db
from flask import Flask,jsonify

app = Flask(__name__)


@app.route('/items/<id>/', methods=['GET'])
def get_items_details(id):
    details = db.execute("select items.id,items.name,sellers.name as seller_name,items.price,items.description from items inner "
                         "join sellers ON items.seller_id=sellers.id where items.id=\'{}\'".format(id))
    formatted_result = [dict(row) for row in details]
    return jsonify(formatted_result)
