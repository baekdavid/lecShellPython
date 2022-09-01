# Faire un système de to-do avec un menu pour :
#   - Afficher les to-do
#   - Ajouter un to-do
#   - Valider un to-do

# Initialise la liste de todo
liste_todos: list = []

# Initialisation choix ordinateur invalide (pour rentrer dans la boucle)
menu: str = "init"

# Tant que l'utilisateur ne demande pas à quitter
while menu != "4":
    # Afficher le menu
    print("\n")
    print("-==  Menu principal  ==-")
    print(" 1 - Afficher les to-do")
    print(" 2 - Ajouter un to-do")
    print(" 3 - Changer statut to-do")
    print(" 4 - Quitter")
    menu = input("Votre choix : ")

    # Selon le choix dans le menu
    match menu:
        # Afficher les todos
        case "1":
            # Titre
            print("\n - Liste des todos -")
            # Parcours de la liste
            for todo in liste_todos:
                # Affichage des todos
                print(f"{todo['texte']} [{'Fait' if todo['statut'] else 'A faire'}]")

        # Ajouter un todo
        case "2":
            # Titre
            print("\n - Ajouter un todo -")
            # Demande le contenu à l'utilisateur
            texte: str = input("Contenu du todo : ")
            # Ajoute à la liste des todos
            liste_todos.append({ "texte": texte, "statut": False })
            
        # Modifier statut todo
        case "3":
            print("\n - Modifier statut todo -")
            # Affichage de la liste
            for i in range(len(liste_todos)):
                # Récupération du todo
                todo: dict = liste_todos[i]
                # Affichage du todo
                print(f"{i + 1} - {todo['texte']} [{'Fait' if todo['statut'] else 'A faire'}]")
            
            # Position du todo à modifier
            position: str = input("Position du todo pour changement de statut : ")
            index: int = int(position) - 1

            # Modification
            liste_todos[index]["statut"] = not liste_todos[index]["statut"]

        # Quitter
        case "4":
            # Quitte la boucle (donc le programme)
            break
        # Choix invalide
        case _:
            print("Choix invalide")