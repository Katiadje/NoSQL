from pymongo import MongoClient
import json

# Connexion à MongoDB sans authentification
client = MongoClient('mongodb://my-mongo-service:27017/')

# Créer une base de données et une collection
db = client.mydb
collection = db.accounts  # Assurez-vous d'utiliser la collection 'accounts'

# Charger les données depuis le fichier JSON
with open("accounts.json", "r") as file:
    data = json.load(file)

# Insérer les documents dans MongoDB
result = collection.insert_many(data)
print(f"Documents insérés avec les IDs : {result.inserted_ids}")
