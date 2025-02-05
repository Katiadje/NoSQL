from neo4j import GraphDatabase

class Neo4jConnection:
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def execute_query(self, query, parameters=None):
        with self._driver.session() as session:
            result = session.run(query, parameters)
            return [record for record in result]  # Récupère tous les résultats dans une liste

def initialize_data(connection):
    # Exemple de création de noeuds
    queries = [
        "CREATE (p:Person {name: 'Alice', age: 30})",
        "CREATE (p:Person {name: 'Bob', age: 25})",
        "CREATE (c:City {name: 'Paris'})",
        "MATCH (p:Person {name: 'Alice'}), (c:City {name: 'Paris'}) CREATE (p)-[:LIVES_IN]->(c)"
    ]
    for query in queries:
        connection.execute_query(query)

if __name__ == "__main__":
    uri = "bolt://localhost:7687"
    user = "neo4j"
    password = "password"
    
    # Établi la connexion
    conn = Neo4jConnection(uri, user, password)
    
    # Initialise les données
    initialize_data(conn)
    
    # Récupère tous les résultats directement
    records = conn.execute_query("MATCH (n) RETURN n")
    
    # Affiche les résultats
    for record in records:
        print(record)
    
    # Ferme la connexion
    conn.close()
