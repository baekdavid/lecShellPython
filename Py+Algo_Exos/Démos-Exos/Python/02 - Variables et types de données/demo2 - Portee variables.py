def fonction1():
    global masupervar # Précise que masupervar fait référence à la variable globale du meme nom (facultatif)
    var1 = "ma var 1"

    def fonction2():
        var2 = "mon autre var 2"
        print(var1) # var1 de fonction1 est accessible (portée enclosing)
        print(var2)

    fonction2()
    print(var1)
    # print(var2) # Erreur : var2 n'existe que dans la fonction2 (portée locale)
    print(masupervar) # masupervar est accessible (portée globale)

masupervar = "ma super var" # Variable globale, déclarée hors fonctions
fonction1()
# fonction2() # Erreur : fonction2 n'existe que dans fonction1 (fonction locale)
# print(var1) # Erreur : var1 n'existe que dans la fonction1 (portée locale)

# True = 2 # Erreur : Impossible d'assigner à True, qui est un mot-clé réservé (portée Built-In)