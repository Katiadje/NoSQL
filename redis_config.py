import redis

# Configuration du pool de connexions avec l'adresse du conteneur Redis
pool = redis.ConnectionPool(
    host='localhost',             # Utilisez l'adresse localhost si vous accédez à Redis depuis votre machine hôte
    port=6379,                    # Le port du conteneur Redis
    db=0,                         # Numéro de la base de données Redis
    max_connections=10,           # Nombre maximal de connexions dans le pool
    timeout=5,                    # Temps d'attente pour obtenir une connexion avant de lever une exception
    socket_connect_timeout=3,     # Temps d'attente pour établir une connexion au serveur Redis
    socket_keepalive=True         # Activer TCP keepalive
)

# Création de l'objet Redis avec le pool de connexions
r = redis.Redis(connection_pool=pool)

# Fonction d'exemple pour ajouter et récupérer des valeurs
def example_redis_commands():
    try:
        # SET : Ajouter une nouvelle clé avec une valeur
        r.set('username', 'JohnDoe')
        print("Clé 'username' ajoutée avec la valeur 'JohnDoe'.")

        # GET : Récupérer la valeur de la clé
        value = r.get('username')
        print(f"Valeur de 'username' : {value.decode('utf-8')}")  # Utilisation de decode pour afficher la chaîne

        # DEL : Supprimer une clé
        r.delete('username')
        print("Clé 'username' supprimée.")

        # Vérification après suppression
        value = r.get('username')
        if value is None:
            print("La clé 'username' n'existe plus.")
        else:
            print(f"Valeur de 'username' : {value.decode('utf-8')}")

    except redis.RedisError as e:
        print(f"Erreur Redis : {e}")

# Appel de la fonction d'exemple
example_redis_commands()
