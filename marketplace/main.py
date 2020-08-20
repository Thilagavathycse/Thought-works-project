from app import *
from login import login_pb
from categories import categories_pb
from items import items_pb
from carts import carts_pb
# coding=UTF-8


@app.route('/')
def index():
    return "<h1>WELCOME TO MARKET PLACE</h1>"


app.register_blueprint(categories_pb)
app.register_blueprint(carts_pb)
app.register_blueprint(items_pb)
app.register_blueprint(login_pb)


if __name__ == "__main__":
    app.run(debug=True)
