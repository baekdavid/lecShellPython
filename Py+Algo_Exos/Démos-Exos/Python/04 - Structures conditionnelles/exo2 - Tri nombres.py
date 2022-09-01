# Demander à l’utilisateur trois nombres puis lui afficher les trois nombres dans l’ordre croissant

# Récupérer les trois nombres
nombre1: float = float(input("Premier nombre : "))
nombre2: float = float(input("Deuxième nombre : "))
nombre3: float = float(input("Troisième nombre : "))

# nb1 le plus grand
if nombre1 >= nombre2 and nombre1 >= nombre3:
    # 1 2 3
    if nombre2 > nombre3:
        print(nombre1, nombre2, nombre3)
    # 1 3 2
    else:
        print(nombre1, nombre3, nombre2)
# nb2 le plus grand
elif nombre2 >= nombre3 and nombre2 >= nombre1:
    # 2 1 3
    if nombre2 > nombre3:
        print(nombre2, nombre1, nombre3)
    # 2 3 1
    else:
        print(nombre2, nombre3, nombre1)

# Regroupe les nombres dans une liste
ma_liste = [nombre1, nombre2, nombre3]
ma_liste.sort()
print(ma_liste)