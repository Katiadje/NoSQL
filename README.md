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