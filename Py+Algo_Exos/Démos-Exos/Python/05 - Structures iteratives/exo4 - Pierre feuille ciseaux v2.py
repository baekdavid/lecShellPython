# Faire un pierre, feuille, ciseaux contre l’ordinateur, avec détection de victoire

# Import du module permettant l'aléatoire
from random import choice

# Liste des choix
choix_possibles: tuple = ("pierre", "feuille", "ciseaux")

# Liste des victoires possibles
victoires_possibles: tuple = (
    ("pierre", "ciseaux"),
    ("feuille", "pierre"),
    ("ciseaux", "feuille")
)

# Choix de l'ordinateur
choix_ordi: str = choice(choix_possibles)

# Choix utilisateur
choix_user: str = input("pierre/feuille/ciseaux : ")

# Affichage combat
print(f"User : {choix_user} | ordi : {choix_ordi}")

# Test victoire
if choix_ordi == choix_user:
    print("Egalité")
elif (choix_user, choix_ordi) in victoires_possibles:
    print("Utilisateur gagne")
else:
    print("Ordinateur gagne")