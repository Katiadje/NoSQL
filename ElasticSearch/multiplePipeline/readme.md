# TP ELK-MultiplePipeline

Ce TP permet d'ingérer des logs générés en Python via la stack ELK (Elasticsearch, Logstash, Kibana) en utilisant Docker et Filebeat pour transférer les logs vers Logstash et Elasticsearch.

## Étapes à suivre

### 1. Génération des logs en Python `send_logs.py`

Le script Python génère des logs de manière aléatoire, qui sont ensuite envoyés dans un fichier local.


### 1. Installation d'un fichier `docker-compose.yml`

- **Mise en place des containers** : Lancez la commande suivante pour démarrer les services Elasticsearch, Logstash, Kibana et filebeat avec Docker Compose :
    ```bash
    docker-compose up -d 
    ```

### 2. Vérification des services

Une fois les containers démarrés, tu peux vérifier leur état avec la commande suivante :
    ```bash
    docker-compose ps
    ```

### 3. Configuration du pipeline Logstash

Le pipeline Logstash est configuré pour ingérer des logs générés par le script Python ainsi que des logs Apache :

- **Fichier Filebeat** : Le fichier `filebeat.yml` est configuré pour surveiller le répertoire `./logs` et envoyer les logs générés par le script Python, notamment le fichier `python_logs.log`, à Logstash.

- **Logs Python** : Les logs générés par le script Python sont formatés en JSON et envoyés à Logstash, où ils sont ensuite traités et envoyés vers Elasticsearch.

Les fichiers de configuration nécessaires se trouvent dans les répertoires `logstash` et `filebeat` :

- **`logstash.conf`** : Définition du pipeline Logstash qui réceptionne les logs, les transforme (en utilisant un filtre JSON) et les indexe dans Elasticsearch sous l'index `python-logs-%{+YYYY.MM.dd}`.
  
- **`filebeat.yml`** : Configuration de Filebeat pour surveiller les fichiers de logs (notamment `python_logs.log`), et les envoyer vers Logstash pour traitement.


### 4. Arrêter et nettoyer les containers

Si tu souhaites arrêter les containers, utilise la commande suivante :
    ```bash
    docker-compose down
    ```
Pour supprimer également les volumes et les données, exécute :
    ```bash
    docker-compose down -v
    ```

---

## commande et lien à utilisées
Lancer notre script py
    ```bash
        python send_logs.py
    ```
vérifier si les indices sont créés :
    ```bash
     curl http://127.0.0.1:9200/_cat/indices?v 
    ```
