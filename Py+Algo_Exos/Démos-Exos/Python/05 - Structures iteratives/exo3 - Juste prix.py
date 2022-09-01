# Le juste prix : Faire deviner un nombre entre 1 et 100 en ne répondant que “c’est plus” ou “c’est moins”

# Import du module permettant l'aléatoire
from random import randint

# - Manche 1 : Utilisateur devine
print("== Manche 1 ==")
# Choix de l'ordinateur
choix_ordi: int = randint(1, 100)

# Choix de l'utilisateur invalide (pour rentrer dans la boucle)
choix_user: int = -1

# Tant que l'utilisateur ne trouve pas
while choix_ordi != choix_user:
    # Demande du choix à l'utilisateur
    choix_user = int(input("Devine mon nombre entre 1 et 100 : "))
    # Choix trop grand 
    if choix_user > choix_ordi : print("C'est moins")
    # Choix trop petit
    elif choix_user < choix_ordi : print("C'est plus")

# Victoire
print('Victoire !')

# - Manche 2 : Ordinateur devine
print("== Manche 2 ==")
# Initialisation min et max
min: int = 1
max: int = 100

# Réponse de l'utilisateur invalide (pour rentrer dans la boucle)
reponse_user: str = "init"

# Tant que l'utilisateur n'a pas dit à l'ordinateur qu'il a gagné
while reponse_user != "gagné":
    # L'ordinateur pense à un nombre et le donne
    choix_ordi = randint(min, max)
    print("Je pense à", choix_ordi)

    # L'utilisateur donne sa réponse
    reponse_user = input("Est-ce plus/moins/gagné : ")

    # En fonction de la réponse
    match reponse_user:
        # Trop grand
        case "moins":
            # Définition du max à nb - 1
            max = choix_ordi - 1
        # Trop petit
        case "plus":
            # Définition du min à nb + 1
            min = choix_ordi + 1

# Victoire
print('Victoire !')