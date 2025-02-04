# Utiliser l'image officielle Python comme base
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le script Python dans le conteneur
COPY redis_config.py /app/redis_config.py

# Installer les dépendances nécessaires
RUN pip install --no-cache-dir redis

# Exposer le port Redis (facultatif, si tu veux exposer le port)
EXPOSE 6379

# Exécuter le script Python lorsque le conteneur démarre
CMD ["python", "redis_config.py"]
