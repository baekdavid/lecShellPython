# Faire un pierre, feuille, ciseaux contre l’ordinateur, avec détection de victoire

# Import du module permettant l'aléatoire
from random import choice

# Liste des choix
choix_possibles: tuple = ("pierre", "feuille", "ciseaux")

# Choix de l'ordinateur
choix_ordi: str = choice(choix_possibles)

# Choix utilisateur
choix_user: str = input("pierre/feuille/ciseaux : ")

# Affichage combat
print(f"User : {choix_user} | ordi : {choix_ordi}")

# Test victoire
if choix_ordi == choix_user:
    print("Egalité")
elif choix_user == "pierre" and choix_ordi == "ciseaux" or choix_user == "feuille" and choix_ordi == "pierre" or choix_user == "ciseaux" and choix_ordi == "feuille":
    print("Utilisateur gagne")
else:
    print("Ordinateur gagne")