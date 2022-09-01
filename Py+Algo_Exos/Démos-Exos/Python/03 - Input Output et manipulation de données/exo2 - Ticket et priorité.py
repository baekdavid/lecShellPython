# Demander à l’utilisateur un nom de ticket sous la forme "[code_priorité]-[nom_ticket]" et afficher la phrase "Le ticket ‘[nom_ticket]’ a la priorité [nom_priorité]"
#   - Correspondance code_priorité / libellé_priorité
#       - 1 = critique
#       - 2 = forte
#       - 3 = moyenne
#       - 4 = faible
#   - Par exemple : "2-test" -> "Le ticket ‘test’ a la priorité forte"

# Tableau de correspondance
correspondance_priorite = {
    "1": "critique",
    "2": "forte",
    "3": "moyenne",
    "4": "faible"
}

# Demande à l'utilisateur
titre: str = input("Titre du ticket : ")
titre_decompose = titre.split("-")

# Décompose les info
code_priorite = titre_decompose[0]
nom = titre_decompose[1]

# Recherche le label correspondant au code de priorite
label_priorite = correspondance_priorite[code_priorite]

# Affichage final
print(f"Le ticket '{nom}' a 2*la priorite {label_priorite}")