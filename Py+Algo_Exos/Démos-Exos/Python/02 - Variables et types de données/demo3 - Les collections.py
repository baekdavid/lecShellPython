# Liste
print("== Liste ==")
ma_liste = ["a", "b", "c"]
print(ma_liste[1])
ma_liste = ["a", 1, False, 2.4, [0, "z"], {1, 2, 3}] # Les listes ne sont pas typées
print(ma_liste)
mon_autre_liste = [] # liste vide
mon_autre_autre_liste = list() # liste vide

# Tuple
print("== Tuple ==")
mon_tuple = ("a", "b", "c")
print(mon_tuple[1])
# mon_tuple[0] = "coucou" # Le tuple est immuable, c'est-à-dire que l'on ne peut changer son contenu
mon_tuple = ("a", 1, "c") # Pas d'erreur, on écrase l'ancien tuple pour le remplacer par celui-ci
mon_autre_tuple = () # tuple vide
mon_autre_autre_tuple = tuple() # tuple vide
print(mon_autre_autre_tuple)

# Set
print("== Set ==")
mon_set = {1, 2, 3}
print(mon_set)
mon_set.add("a")  # Ajoute "a" au set
print(mon_set)
mon_set.add(1)    # 1 est déjà présent, l'ajout est ignoré
print(mon_set)
# mon_autre_set = {} # Attention! cela déclare un dictionnaire
mon_autre_autre_set = set() # set vide

# Dictionnaire
print("== Dictionnaire ==")
mon_dico = {"test1": "Bonjour"}
print(mon_dico)
mon_dico["test2"] = "Pouet"
print(mon_dico)
print(mon_dico["test2"])
mon_dico["test3"] = (1, 2, 3)
print(mon_dico["test3"])
mon_dico["test3"] = "coucou"
print(mon_dico)
mon_autre_dico = {} # dictionnaire vide
mon_autre_autre_dico = dict() # dictionnaire vide

# Accéder à un sous élément
vehicules = [
    {
        'couleur': 'rouge',
        'marque': 'alfa',
        'nbProprietaires': 2,
        'proprietaires': ['tom', 'james']
    },
    {
        'couleur': 'vert',
        'marque': 'land rover',
        'nbProprietaires': 1,
        'proprietaires': ['alison']
    }
]

vehicule = vehicules[0]
proprios = vehicule['proprietaires']
tom = proprios[0]

tom = vehicules[0]['proprietaires'][0]
