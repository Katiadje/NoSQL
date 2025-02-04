import redis

# Connexion à Redis
r = redis.Redis(host='my-redis', port=6379, db=0)

# Ajouter une clé avec une valeur
r.set('username', 'JohnDoe')
print("Clé 'username' ajoutée avec la valeur 'JohnDoe'.")

# Récupérer la valeur de la clé
value = r.get('username')
if value:
    print(f"Valeur de 'username' : {value.decode('utf-8')}")
else:
    print("Clé 'username' non trouvée.")

# Modifier la valeur de la clé
r.set('username', 'JaneDoe')
print("Clé 'username' modifiée avec la nouvelle valeur 'JaneDoe'.")

# Supprimer la clé
r.delete('username')
print("Clé 'username' supprimée.")

# Vérifier si la clé existe après suppression
value = r.get('username')
if value:
    print(f"Valeur de 'username' : {value.decode('utf-8')}")
else:
    print("La clé 'username' n'existe plus.")
