# Ouverture du fichier
fichier = open("./08 - Acceder aux fichiers/demo1 - fichier texte.txt")
print(fichier) # Element de type TextIOWrapper

# Lecture du contenu
lignes_du_fichier = fichier.readlines()
print(lignes_du_fichier) # Liste de lignes

# Fermeture du fichier
fichier.close()

# Ouverture de fichier avec with
with open("./08 - Acceder aux fichiers/demo1 - fichier texte.txt") as fichier2:
    # Lecture du contenu
    lignes_du_fichier = fichier2.readlines()
    print(lignes_du_fichier) # Liste de lignes

    # Parcours des lignes
    for ligne in lignes_du_fichier:
        print("La ligne contient :", ligne)

# Tente d'accéder au fichier, fermé puisque le bloc with est fermé
# print(fichier2.readlines())
