# Demande les informations
print("Merci de renseigner les deux indicateurs  A (horizontal) et B (vertical)")
A: int = int(input("A : "))
B: int = int(input("B : "))

# Recherche hors tableau
if A < 98 or A > 208 or B < 10 or B > 58:
    print("Les indicateurs sont hors tableau")
# Recherche dans le tableau
# Ligne 1
elif B <= 20:
    # Zone 1
    if A <= 172:
        print("Zone 1")
    # Zone 2
    elif A <= 189:
        print("Zone 2")
    # Hors zone
    else:
        print("Hors zone")
# Ligne 2
elif B <= 27:
    # Zone 1
    if A <= 167:
        print("Zone 1")
    # Zone 2
    elif A <= 189:
        print("Zone 2")
    # Hors zone
    else:
        print("Hors zone")
# Ligne 3
elif B <= 35:
    # Zone 1
    if A <= 153:
        print("Zone 1")
    # Zone 2
    elif A <= 189:
        print("Zone 2")
    # Zone 3
    else:
        print("Zone 3")
# Ligne 4
elif B <= 45:
    # Zone 3
    if A >= 181:
        print("Zone 3")
    # Zone 2
    elif A >= 141:
        print("Zone 2")
    # Hors zone
    else:
        print("Hors zone")
# Ligne 5
else:
    # Zone 3
    if A >= 168:
        print("Zone 3")
    # Hors zone
    else:
        print("Hors zone")
