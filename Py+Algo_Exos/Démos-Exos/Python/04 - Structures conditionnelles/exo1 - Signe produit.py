# Demander à l’utilisateur deux nombres puis lui afficher le signe du produit des deux

# Récupérer les deux nombres
nombre1: float = float(input("Premier nombre : "))
nombre2: float = float(input("Deuxième nombre : "))

# Calculer le produit
produit = nombre1 * nombre2

# Tester le signe du produit
if produit < 0:
    print("Le signe du produit est négatif")
elif produit > 0:
    print("Le signe du produit est positif")
else:
    print("Le produit est nul")