from pymongo import MongoClient
import json

# Connexion à MongoDB
client = MongoClient('mongodb://root:example@mongo_container:27017/')

# Créer une base de données et une collection
db = client.mydb
collection = db.mycollection

# Insérer un document
document = {"name": "John Doe", "email": "john.doe@example.com", "age": 30}
result = collection.insert_one(document)
print(f"Document inséré avec l'ID : {result.inserted_id}")

# Insérer plusieurs documents
documents = [
    {"name": "Alice", "email": "alice@example.com", "age": 25},
    {"name": "Bob", "email": "bob@example.com", "age": 35}
]
result = collection.insert_many(documents)
print(f"Documents insérés avec les IDs : {result.inserted_ids}")

# Charger des données depuis un fichier JSON (exemple : accounts.json)
with open("accounts.json", "r") as file:
    data = json.load(file)
result = collection.insert_many(data)
print(f"Documents insérés avec les IDs : {result.inserted_ids}")

# Exemple de requête pour récupérer les documents
query = {"age": {"$gt": 25}}
documents = collection.find(query)
for doc in documents:
    print(doc)
