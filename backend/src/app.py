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


if __name__ == '__main__':
    app.run(debug=True, port=4000)