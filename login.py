import database_connection
from flask import Flask,request,render_template,session, redirect, url_for, escape, request
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import psycopg2
from flask import request

app = Flask(__name__)
app.secret_key = "thisissecretkey"

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/users', methods=['GET','POST'])
def all_user():
    user_details = {'thilaga': '@123','sangeetha': '@456','kaali': '@789'}

    """formatted_result = [dict(id=row[0], username=row[1], password=row[2]) for row in user_name.fetchall()]
    return formatted_result
    formatted_result = [dict(row) for row in user_name]
    return formatted_result"""
    name1 = request.form['username']
    pwd = request.form['password']
    if name1 not in user_details :
        return render_template("login.html" , info="invalid user")
    else:
        if user_details[name1] != pwd:
            return render_template("login.html", info="invalid pwd")
        else:
            return render_template("home.html", name=name1)
@app.route('/categories', methods=['GET'])
def all_categories():
    categories = database_connection.db.execute("select name from purchase.categories")
    formatted_result = [dict(row) for row in categories]
    return jsonify(formatted_result)
    #return render_template('home.html', value=formatted_result)

@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
