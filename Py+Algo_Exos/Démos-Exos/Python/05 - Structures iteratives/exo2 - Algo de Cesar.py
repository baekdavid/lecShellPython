# Chiffrer un message fourni par l’utilisateur avec l’algorithme de César (décalage de 3)

# Import de l'alphabet minuscule
from string import ascii_lowercase

# Demande le message a l'utilisateur
message: str = input("Message à chiffrer : ")
message = message.lower()

# Initialisation variables message chiffré
message_chiffre: str = ""

# Pour chaque lettre dans mon message
# for lettre in list(message):
# for lettre in message.split():
for lettre in message:
    # Cas hors alphabet
    if not lettre in ascii_lowercase:
        # Ajoute directement la lettre en l'état dans le message chiffré
        message_chiffre += lettre
        # Passe directement à la lettre suivante
        continue
    
    # Retrouve la position de la lettre dans l'alphabet grâce à la fonction index
    position: int = ascii_lowercase.index(lettre)

    # Calcul de la position chiffrée (modulo 26 pour retourner à a après z)
    position_chiffree: int = (position + 3) % 26

    # Recupère la lettre chiffrée
    lettre_chiffree: str = ascii_lowercase[position_chiffree]

    # Ajoute la lettre chiffrée à message chiffré
    message_chiffre += lettre_chiffree

# Affiche le message chiffré
print(message_chiffre)