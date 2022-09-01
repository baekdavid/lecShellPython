# *mots permet de définir mots comme le tuple contenant tous les arguments/paramètres
def concat(*mots):
    """Je suis un message pour décrire la fonction"""
    # Affiche le tuple
    print(mots)
    # Affiche la version concaténée
    # Converti le tableau mots en une chaine de caractère, en séparant chaque
    #   élément par un espace
    print(" ".join(mots))

concat("aaa")
concat("a", "b", "c")
concat("Bonjour", "tout", "le", "monde")
concat()
concat(a="2", b="f")