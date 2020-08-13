from flask import Flask,session



app = Flask(__name__)


@app.route('/logout', methods=['DELETE'])
def logout():
    if 'name' in session:
        session.pop('name', None)
        return "Thank you ! logged out success fully"""
