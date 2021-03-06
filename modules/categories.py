from flask import session, Blueprint
from models import *
from app import *
# coding=UTF-8


categories_pb = Blueprint('categories_pb', __name__)

@categories_pb.route('/categories', methods=['GET'])
@token_required
def display_categories():
    categories = session.query(Category).all()
    formatted_result = [display(row) for row in categories]
    return jsonify(formatted_result)
def display(row):
    return "id: "+str(row.id)+","+"name: "+str(row.name)


@categories_pb.route('/categories/<category_id>/', methods=['GET'])
@token_required
def get_items(category_id):
    items = session.query(Category).join(Item).filter(Category.id == category_id).all()
    formatted_result = [display(item) for item in items]
    return jsonify(formatted_result)
def display(item):
    return "id: "+str(item.id)+","+"name: "+str(item.name)

