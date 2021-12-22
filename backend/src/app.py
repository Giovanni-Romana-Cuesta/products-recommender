from flask import Flask, jsonify
from database import *

app = Flask(__name__)

db = Database('neo4j://localhost:7687', 'neo4j', '1234')
db.connection()


@app.route('/')
def index():
    return '<h1>Bienevenid@</h1>'

@app.route('/users', methods=['GET'])
def getUsers():
    users = db.getUsers()
    usersList = []
    for user in users:
        usersList.append(user["u"])
    return jsonify({"users": usersList})


@app.route('/products', methods=['GET'])
def getProducts():
    products = db.getProducts()
    result = []
    for product in products:
        result.append(product["p"])
    return jsonify({"products": result})


@app.route('/orders', methods=['GET'])
def getOrders():
    orders = db.getOrders()
    result = []
    for order in orders:
        result.append(order["o"])
    return jsonify({"orders": result})






if __name__ == '__main__':
    app.run(debug=True, port=4000)