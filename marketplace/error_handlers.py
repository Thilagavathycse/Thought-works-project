#from database import *

@app.errorhandler(401)
def unauthorized_error(error):
    return "<h1> you are not authorized to access this page!</h1>"

@app.errorhandler(404)
def not_fount_error(error):
    return "<h1>page not found!</h1>"

