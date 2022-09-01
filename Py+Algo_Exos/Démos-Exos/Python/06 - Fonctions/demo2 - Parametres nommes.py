def ma_fonction(prenom, age=-1):
    print(f"Bonjour {prenom} qui a {age} ans")

ma_fonction("Damien", 33)               # Appel avec arguments
ma_fonction(age=50, prenom="MonPrenom") # Appel avec arguments nommés
ma_fonction("Prenom2")                  # Appel avec argements par défaut