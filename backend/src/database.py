from neo4j import Driver, GraphDatabase, READ_ACCESS

class Database:

    def __init__(self, uri, user, password):
        self.uri = uri
        self.user = user
        self.password = password
    
    def connection(self):
        # Establece la conexión con base de datos usando el driver de no4j para python
        self.driver = GraphDatabase.driver(self.uri, auth=(self.user, self.password))
    
    def getUsers(self):
        # Método para obtener todos los usuarios guardados en la base de datos
        session = self.driver.session(default_access_mode=READ_ACCESS)
        result = session.run('MATCH (u:User) RETURN u')
        return result.data()

    def getProducts(self):
        session = self.driver.session(default_access_mode=READ_ACCESS)
        result = session.run('MATCH (p:Product) RETURN p')
        return result.data()

    def getOrders(self):
        session = self.driver.session(default_access_mode=READ_ACCESS)
        result = session.run('MATCH (o:Order) RETURN o')
        return result.data()