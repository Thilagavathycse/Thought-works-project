from main import *
import datetime

@app.route('/user', methods=['POST'])
def validate_user():
    username = request.form['username']
    password = request.form['password']
    user_details = db.execute("SELECT * from users WHERE name= \'{}\'  and password= \'{}\'".format(username, password))
    data = user_details.fetchone()
    if data is not None:
        token = jwt.encode({'name': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},app.config['secret_key'])
        return jsonify({'token': token.decode('UTF-8'), 'message': 'logged in successfuly'}), 200
    else:
        return jsonify({'message': 'Sorry,cannot access: Unauthorized'}), 401

