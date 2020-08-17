from database import *
from flask import Flask,  jsonify

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


