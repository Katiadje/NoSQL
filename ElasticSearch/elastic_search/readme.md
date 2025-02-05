# Mise en place d'Elasticsearch et Kibana avec Docker sur Windows

## Introduction
Ce guide explique comment installer et configurer **Elasticsearch** et **Kibana** sur un environnement Windows à l'aide de Docker. Nous verrons également comment indexer des données en utilisant un script Bash.

## 1️⃣ Prérequis
Avant de commencer, assure-toi d’avoir installé :

- **Docker Desktop** [Télécharger ici](https://www.docker.com/products/docker-desktop/)
- **Git Bash** (fourni avec Git for Windows) [Télécharger ici](https://git-scm.com/downloads)
- **Windows Subsystem for Linux (WSL)** (optionnel, mais recommandé)

---

## 2️⃣ Installation d'Elasticsearch et Kibana avec Docker

Crée un fichier **`docker-compose.yml`** et ajoute le contenu suivant :

```yaml
docker-compose.yml

version: '2.2'
services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:7.11.1
    container_name: elasticsearch
    restart: always
    environment:
      - xpack.security.enabled=false
      - discovery.type=single-node
    ulimits:
      memlock:
        soft: -1
        hard: -1
      nofile:
        soft: 65536
        hard: 65536
    cap_add:
      - IPC_LOCK
    volumes:
      - ./elas1:/usr/share/elasticsearch/data
    ports:
      - 9200:9200
      - 9300:9300
    networks:
      - esnet

  kibana:
    container_name: kibana
    image: docker.elastic.co/kibana/kibana:7.11.1
    restart: always
    ports:
      - 5601:5601
    depends_on:
      - elasticsearch
    networks:
      - esnet

networks:
  esnet:
    driver: bridge
```

**➡️ Lancement des conteneurs :**

```bash
docker-compose up -d
```

Cela va lancer **Elasticsearch** et **Kibana**. 
Une fois que c'est prêt, accède à Kibana :  
📌 **http://localhost:5601/app/dev_tools#/console**

Vérifie si Elasticsearch fonctionne avec :
```bash
curl http://localhost:9200/_cluster/health
```

---

## 3️⃣ Indexation des données dans Elasticsearch

Crée un fichier **`insert_data.sh`** pour insérer des données JSON dans Elasticsearch :

```bash
#!/bin/bash

curl -s -H "Content-Type: application/x-ndjson" -XPOST localhost:9200/receipe/_bulk --data-binary "@receipe.json" &&\
printf "\n✅ Insertion receipe index to elastic node OK ✅ "

curl -s -H "Content-Type: application/x-ndjson" -XPOST localhost:9200/accounts/docs/_bulk --data-binary "@accounts.json"
printf "\n✅ Insertion accounts index to elastic node OK ✅ "

curl -s -H "Content-Type: application/x-ndjson" -XPOST localhost:9200/movies/_bulk --data-binary "@movies.json"
printf "\n✅ Insertion movies index to elastic node OK ✅ "

curl -s -H "Content-Type: application/x-ndjson" -XPOST localhost:9200/products/_bulk --data-binary "@products.json"
printf "\n✅ Insertion products index to elastic node OK ✅ "
```

Place ce fichier dans le même dossier que tes fichiers JSON (**receipe.json, accounts.json, movies.json, products.json**).

**➡️ Exécution du script sur Windows avec Git Bash**

```bash
bash insert_data.sh
```

---

## 4️⃣ Visualisation des données avec Kibana

Dans Kibana, va dans **Dev Tools** et exécute la requête suivante pour voir les indices :





