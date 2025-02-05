# Utiliser l'image officielle Python comme base
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier requirements.txt et installer les dépendances
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copier tous les autres fichiers nécessaires dans le conteneur
COPY . /app

# Exposer les ports MongoDB et Redis (optionnel)
EXPOSE 27017 6379

# Commande pour exécuter le script Python
CMD ["python", "mongo_setup.py"]
