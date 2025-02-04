import redis

# Configuration du pool de connexions avec l'adresse du conteneur Redis
pool = redis.ConnectionPool(
    host='my-redis',             
    port=6379,                    
    db=0,                          
    max_connections=10,           
    timeout=5,                    
    socket_connect_timeout=3,    
    socket_keepalive=True       
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
