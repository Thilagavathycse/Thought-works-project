from database import db
from flask import Flask,request

app = Flask(__name__)

@app.route('/user', methods=['POST'])

def validate_user():
    username = request.form['username']
    password = request.form['password']
    user_details = db.execute("SELECT * from users WHERE name= \'{}\'  and password= \'{}\'".format(username,password))
    data = user_details.fetchone()
    if data is None:
        return "user or password is wrong"
    else:
        return "logged in successfuly"


