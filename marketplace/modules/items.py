from flask import Blueprint
from models import *
from app import *
# coding=UTF-8

items_pb = Blueprint('items_pb', __name__)


@items_pb.route('/items/<item_id>/', methods=['GET'])
@token_required
def get_items_details(item_id):
    item_details = session.query(Item).join(Seller).filter(Item.id == item_id).all()
    for row in item_details:
            return "product ID:{} product Name:{}  description:{} price:{}".format(row.id, row.name,row.description, row.price)


