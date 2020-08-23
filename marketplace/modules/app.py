from flask import Flask, request, jsonify
# coding=UTF-8
from sqlalchemy.orm import sessionmaker
import jwt
from functools import wraps
import os
from database import *

app = Flask(__name__)
app.config['secret_key'] = os.urandom(50)
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message': 'Token is missing'}), 403
        try:
            details = jwt.decode(token, app.config['secret_key'])
        except:
            return jsonify({'message': 'Token is invalid'}), 403
        return f(*args, **kwargs)
    return decorated


Session = sessionmaker(bind=db)
session = Session()
