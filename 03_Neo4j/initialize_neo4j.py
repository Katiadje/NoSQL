from neo4j_setup import Neo4jConnection

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
    conn = Neo4jConnection("bolt://localhost:7687", "neo4j", "password")
    initialize_data(conn)
    conn.close()
