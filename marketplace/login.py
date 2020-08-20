import datetime
from flask import Blueprint
from app import *
# coding=UTF-8


login_pb = Blueprint('login_pb', __name__)

@login_pb.route('/user', methods=['POST'])
def validate_user():
    username = request.form.get('username')
    password = request.form.get('password')
    user_details = db.execute("SELECT * from users WHERE name= \'{}\'  and password= \'{}\'".format(username, password))
    data = user_details.fetchone()
    if data is None:
        return jsonify({'message': 'Sorry,cannot access: Unauthorized'}), 401
    else:
        token = jwt.encode({'name': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},app.config['secret_key'])
        return jsonify({'token': token.decode('UTF-8'), 'message': 'logged in successfully'}), 200



