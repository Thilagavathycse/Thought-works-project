from flask import session, request, jsonify, Flask
import codecs
import os
import jwt
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

@app.route('/')
def index():
    return "<h1>WELCOME TO MARKET PLACE</h1>"


Session = sessionmaker(bind=db)
session = Session()

if __name__ == "__main__":
    app.run(debug=True)
