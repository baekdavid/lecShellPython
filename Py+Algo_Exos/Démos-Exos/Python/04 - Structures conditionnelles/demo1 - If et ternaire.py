if True:
    print("coucou du if")
    print("Toujours dans if")
print("Je ne suis pas dans le if")

x = 1
if x == 1:
    test = "oui"
else:
    test = "non"

# Structure ternaire
# Souvent dans les autres langages : test = x == 1 ? "oui" : "non"
test = "oui" if x == 1 else "non"
print(test)
print("oui") if x == 1 else print("non")