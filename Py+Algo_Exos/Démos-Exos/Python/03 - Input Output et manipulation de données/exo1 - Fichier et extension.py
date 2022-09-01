# Demander un chemin absolu vers un fichier et renvoyer le nom du fichier et son extension
#   - Le chemin est une chaine de caractère demandée à l’utilisateur (inutile d’utiliser le module os)
#   - L’extension, si connue, donnera le type nommé
#       - Utiliser un dictionnaire
#   - Par exemples
#       - "c:\users\python\abc.xlsx" renverra "abc : Excel (xlsx)"
#       - "c:\users\python\def.alg" renverra "def : Extension inconnu (alg)"

# Tableau correspondance extension - nom
correspondance_extension_programme = {
    'xlsx': 'Excel',
    'pptx': 'Powerpoint'
}

# Demande le chemin
chemin_absolu: str = input("Chemin absolu du fichier : ")

# Récupère nom et extension (dernier élément de la string split par \)
fichier_avec_extension: str = chemin_absolu.split("\\")[-1]

# Sépare nom et extension
nom_fichier: str = fichier_avec_extension.split(".")[0]
extension_fichier: str = fichier_avec_extension.split(".")[1]

# Nom de l'extension
# Teste si l'extension est une clé dans le dictionnaire de correspondance
if extension_fichier in correspondance_extension_programme:
    programme = correspondance_extension_programme[extension_fichier]
else:
    programme = "Extension inconnue"

# Affichage final
print(f"{nom_fichier} : {programme} ({extension_fichier})")