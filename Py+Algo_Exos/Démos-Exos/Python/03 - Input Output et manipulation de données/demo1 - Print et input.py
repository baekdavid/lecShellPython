# Afficher
x = 123

# print("x vaut " + x) # Impossible de concaténer un str avec un int
print("x vaut " + str(x)) # On "cast" x en string
print("x vaut", x) # print s'occupe de "caster" x

# Lire
prenom = input("Votre prénom : ")
print("Vous avez entré :", prenom)
