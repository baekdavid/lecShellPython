ma_liste: list = [1, 2, 3, 4]

def ajouter2(nb):
    return nb + 2

print(list(map(lambda nb: nb + 2, ma_liste)))