from main import *
import datetime

@app.route('/user', methods=['POST'])
def validate_user():
    username = request.form['username']
    password = request.form['password']
    user_details = session.query(User).filter_by(name=username, password=password).first()
    if user_details:
        token = jwt.encode({'name': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},app.config['secret_key'])
        return jsonify({'token': token.decode('UTF-8'), 'message': 'logged in successfuly'}), 200
    else:
        return jsonify({'message': 'Sorry,cannot access: Unauthorized'}), 401

