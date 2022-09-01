# Demander à l’utilisateur trois nombres puis lui afficher les trois nombres dans l’ordre croissant

# Construit une liste avec les input
# Python bien plus avancé.
ma_liste = [float(input("Nombre : ")) for _ in range(3)].sort()
print(ma_liste)