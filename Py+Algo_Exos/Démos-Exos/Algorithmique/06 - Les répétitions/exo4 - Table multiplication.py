# Demande le chiffre à l'utilisateur
chiffreUtilisateur: int = int(input("Pour quel chiffre souhaitez-vous la table de multiplication ? "))

# Calcul de la table
for multiplicateur in range(1, 11):
    produit = multiplicateur * chiffreUtilisateur
    print(str(multiplicateur) + "x" + str(chiffreUtilisateur) + "=" + str(produit))