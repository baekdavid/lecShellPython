def f1():
    x = 2
    return "nope"
    # La suite du code est ignoré, return stoppe immédiatement l'execution de la fonction
    if x == 1:
        # ...du code
        return "le return quand x == 1"
    else:
        return "x est différent de 1"

toto = f1()
print(toto)