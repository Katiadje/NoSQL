# Redis Python Configuration

Ce projet Docker configure un conteneur Python avec un script permettant d'interagir avec une base de données Redis. Il inclut un pool de connexions Redis pour gérer l'accès efficace aux ressources Redis et propose un exemple de commandes Redis pour manipuler les données.

## Prérequis

Avant de démarrer, assurez-vous d'avoir Docker installé sur votre machine. Ce projet utilise l'image officielle Python 3.9 et se connecte à un service Redis.

## Fonctionnalités

- Configuration d'une connexion Redis avec un pool de connexions.
- Exemple de commandes Redis : `SET`, `GET`, et `DEL` pour manipuler les clés et les valeurs dans Redis.
- Exposition du port Redis (6379) pour une communication avec le serveur Redis.

## Structure du projet

/NOSQL
  ├── Dockerfile
  ├── docker-compose.yml
  ├── redis_config.py
  ├── README.md

## Installation et Exécution

### 1. Construire l'image Docker

Dans le répertoire racine du projet, ouvrez un terminal et exécutez la commande suivante pour construire l'image Docker :


docker-compose up --build

2. Lancer le conteneur Docker
Une fois l'image construite, vous pouvez exécuter le conteneur avec cette commande :

docker run -p 6379:6379 redis-python-example

Cette commande expose le port 6379 du conteneur (le port par défaut de Redis) sur le même port sur votre machine locale.

3. Vérifier l'exécution du script
Le script Python redis_config.py sera exécuté automatiquement lors du démarrage du conteneur. Vous verrez les résultats des commandes Redis dans les logs du conteneur. Par exemple :


Clé 'username' ajoutée avec la valeur 'JohnDoe'.
Valeur de 'username' : JohnDoe
Clé 'username' supprimée.
La clé 'username' n'existe plus.
Détails de la configuration Redis
Le script Python configure un pool de connexions Redis avec les paramètres suivants :

Host : localhost
Port : 6379
db : 0 (par défaut)
max_connections : 10
timeout : 5 secondes
socket_connect_timeout : 3 secondes
socket_keepalive : True (pour garder la connexion active)
Exemple de commandes Redis
Le script inclut un exemple de gestion des clés Redis avec les commandes suivantes :

SET : Ajouter une clé avec une valeur
GET : Récupérer la valeur d'une clé
DEL : Supprimer une clé
Le script vérifie également l'existence de la clé après sa suppression.


###


### Mongo Docker & Python Configuration
docker pull mongo
docker run --name my-mongo -p 27017:27017 -d mongo
pip install pymongo
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')

###

### Neo4j Setup

1. **Installer Neo4j** :
   sudo apt update
   sudo apt install neo4j

###

###
Tester les container:
### Redis: 
redis-cli ping il envoie PONG
docker exec -it my-redis-service redis-cli
SET hello "world"
GET hello il renvoie "world"


### MongDB:
docker exec -it my-mongo-service bash
docker run --name my-mongo -v ./config/mongodb/mongod.conf:/etc/mongod.conf -p 27017:27017 -d mongo --config /etc/mongod.conf

docker exec -it my-mongo-service mongosh
show dbs
use mydb
db.users.find() pour trouver ceux créer a la main
db.accounts.find() pour retrouver les données du json



### Neo4j
docker start neo4j
pip install neo4j
python3 neo4j_setup.py

http://localhost:7474/browser/
username: neo4j
mdp: password


### Elastic search
sur csv data
📌 1. Vérifier si l'index csv-data existe
Tu peux exécuter cette commande pour voir tous les index disponibles :


curl -X GET "http://localhost:9200/_cat/indices?v"
Si csv-data n'apparaît pas dans la liste, cela signifie qu'il n'a pas encore été créé.

📌 2. Créer l'index csv-data
Si l'index csv-data n'existe pas, crée-le avec la commande suivante :


curl -X PUT "http://localhost:9200/csv-data" -H "Content-Type: application/json" -d '
{
  "settings": {
    "number_of_shards": 1,
    "number_of_replicas": 1
  }
}'
📌 3. Vérifier que l'index est bien créé
Après la création, vérifie qu'il existe bien :

curl -X GET "http://localhost:9200/_cat/indices?v"

Si csv-data apparaît dans la liste, alors l'index est bien créé et tu peux maintenant y insérer des documents.

📌 4. Insérer un document test dans csv-data
Ajoute un premier document pour tester :


curl -X POST "http://localhost:9200/csv-data/_doc/1" -H "Content-Type: application/json" -d '
{
  "name": "Test Document",
  "description": "This is a sample document."
}'
📌 5. Vérifier que le document est bien inséré
Exécute la requête suivante pour récupérer tous les documents de l'index :

curl -X GET "http://localhost:9200/csv-data/_search?q=*"
Status: OK

Tester les recipes:

 curl -X GET "http://localhost:9200/csv-data/_search" -H "Content-Type: applicaticurl -X GET "http://localhost:9200/csv-data/_search" -H "Content-Type: application/json" -d '
{
  "query": {
    "match": {
      "title": "Pasta With Butternut Squash and Sage Brown Butter"
    }
  }
}'
{"took":3,"timed_out":false,"_shards":{"total":1,"successful":1,"skipped":0,"failed":0},"hits":{"total":{"value":0,"relation":"eq"},"max_score":null,"hits":[]}}


###