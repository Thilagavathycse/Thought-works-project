from database import *
from flask import Flask,request
import jwt
from jwt import PyJWT
import datetime
from functools import wraps

app = Flask(__name__)
app.config['secret_key'] = 'onlineshoppingproject'


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message' :'Token is missing'}), 403
        try:
            details = jwt.decode(token,app.config['secret_key'])
        except:
            return jsonify({'message':'Token is invalid'}), 403
        return f(*args, **kwargs)
    return decorated
@app.route('/unprotected')
def unprotected():
    return jsonify({'message': 'anyone can view this'})


@app.route('/protected')
def protected():
    return jsonify({'message': 'This is available for the users who have valid Tokens'})


@app.route('/user', methods=['POST'])

def validate_user():
    username = request.form['username']
    password = request.form['password']
    user_details = db.execute("SELECT * from users WHERE name= \'{}\'  and password= \'{}\'".format(username,password))
    data = user_details.fetchone()
    if data is not None:
        token = jwt.encode({'name': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
                           app.config['secret_key'])
        return jsonify({'token': token.decode('UTF-8'), 'message': 'logged in successfuly'}), 200

    else:
        # return jsonify({"message": "SUCCESS!: Authorized"}), 200
        return jsonify({'message': 'Sorry,cannot access: Unauthorized'}), 401


