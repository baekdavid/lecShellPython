# Reprendre l’exercice FizzBuzz du cours d’algorithmique

# Pour compteur allant de 1 à 100
for compteur in range(1, 101):
    # Init de la variable texte
    texte = ""

    # Fizz
    if compteur % 3 == 0:
        texte = "Fizz"

    # Buzz
    if compteur % 5 == 0:
        texte += "Buzz"

    # Normal
    if texte == "":
        texte = str(compteur)
        # texte = f"{compteur}"
    
    # Bonus
    if compteur % 10 == 9:
        texte += " Bonus"
    
    # Affichage
    print(texte)