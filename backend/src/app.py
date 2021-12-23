from flask import Flask, jsonify
from neo4j.work import result
from database import *
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
db = Database('neo4j://localhost:7687', 'neo4j', '1234')


@app.route('/')
@cross_origin()
def index():
    return '<h1>Bienevenid@</h1>'


@app.route('/users', methods=['GET'])
@cross_origin()
def getUsers():
    users = db.getUsers()
    usersList = []
    for user in users:
        usersList.append(user["u"])
    return jsonify({"users": usersList})


@app.route('/products', methods=['GET'])
@cross_origin()
def getProducts():
    products = db.getProducts()
    result = []
    for product in products:
        result.append(product["p"])
    return jsonify({"products": result})


@app.route('/orders', methods=['GET'])
@cross_origin()
def getOrders():
    orders = db.getOrders()
    result = []
    for order in orders:
        result.append(order["o"])
    return jsonify({"orders": result})

@app.route('/orders/<string:userID>')
@cross_origin()
def getOrdersByUser(userID):
    orders = db.getOrdersByUser(userID)
    result = []
    for order in orders:
        result.append(order["orders"])
    for i in result:
        products = db.getOrderProducts(i["orderID"])
        aux = []
        for p in products:
            aux.append(p["products"])
        i['products'] = aux
    return jsonify([{"orders": result}])



@app.route('/ordersProducts')
@cross_origin()
def getOrdersProducts():
    products = db.getOrderProducts("00001")
    return jsonify(products)


if __name__ == '__main__':
    app.run(debug=True, port=4000)