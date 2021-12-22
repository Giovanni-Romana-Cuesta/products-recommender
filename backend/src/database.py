from neo4j import Driver, GraphDatabase, READ_ACCESS

class Database:

    def __init__(self, uri, user, password):
        self.uri = uri
        self.user = user
        self.password = password
    
    def connection(self):
        self.driver = GraphDatabase.driver(self.uri, auth=(self.user, self.password))
    
    def getUsers(self):
        session = self.driver.session(default_access_mode=READ_ACCESS)
        response = session.run('MATCH (u:User) RETURN u')
        return response.data()