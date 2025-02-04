from neo4j import GraphDatabase

class Neo4jConnection:
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))
    
    def close(self):
        self._driver.close()
    
    def execute_query(self, query, parameters=None):
        with self._driver.session() as session:
            return session.run(query, parameters)

# Exemple d'utilisation
if __name__ == "__main__":
    uri = "bolt://localhost:7687"  
    user = "neo4j" 
    password = "password"  
    
    conn = Neo4jConnection(uri, user, password)
    result = conn.execute_query("MATCH (n) RETURN n")
    for record in result:
        print(record)
    conn.close()
