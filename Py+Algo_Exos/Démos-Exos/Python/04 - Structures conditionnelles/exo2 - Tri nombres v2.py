# Demander à l’utilisateur trois nombres puis lui afficher les trois nombres dans l’ordre croissant

# Récupérer les trois nombres
nombre1: float = float(input("Premier nombre : "))
nombre2: float = float(input("Deuxième nombre : "))
nombre3: float = float(input("Troisième nombre : "))

# Regroupe les nombres dans une liste que l'on trie
ma_liste = [nombre1, nombre2, nombre3]
ma_liste.sort()

# Affichage final
print(ma_liste)