import re
from neo4j import Driver, GraphDatabase, READ_ACCESS

class Database:

    def __init__(self, uri, user, password):
        # Establece la conexión con base de datos usando el driver de no4j para python
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        self.session = self.driver.session(default_access_mode=READ_ACCESS)
        
    def getUsers(self):
        # Método para obtener todos los usuarios guardados en la base de datos
        result = self.session.run('MATCH (u:User) RETURN u')
        return result.data()

    def getProducts(self):
        result = self.session.run('MATCH (p:Product) RETURN p')
        return result.data()

    def getOrders(self):
        result = self.session.run('MATCH (o:Order) RETURN o')
        return result.data()

    def getOrdersByUser(self, userID):
        query = "MATCH (:User {userID: $userID})-[:BOUGHT]->(orders:Order) RETURN orders "
        result = self.session.run(query, userID=userID)
        return result.data()

    def getOrderProducts(self, orderID):
        query = "MATCH (:Order {orderID: $orderID})-[:HAS]->(products:Product) RETURN products"
        result = self.session.run(query, orderID=orderID)
        return result.data()