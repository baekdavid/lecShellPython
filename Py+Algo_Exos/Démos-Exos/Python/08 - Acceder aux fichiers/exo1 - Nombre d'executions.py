# Init
chemin_fichier: str = "08 - Acceder aux fichiers/exo1 - fichier texte.txt"

# Lecture du fichier
with open(chemin_fichier) as f:
    contenu = f.readlines()

# Récupération du nombre d'exécution
contenu_ligne = contenu[0]
config = contenu_ligne.split("=")
nb_exec = int(config[1])
nb_exec += 1

# Affichage
print(f"Le script a été exécuté {nb_exec} fois")

# Ecriture du fichier
with open(chemin_fichier, 'w') as f:
    f.write(f"{config[0]}={nb_exec}")