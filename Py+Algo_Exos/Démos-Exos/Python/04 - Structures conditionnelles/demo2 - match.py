message = input("choisissez a, b ou c : ")
a = 2
b = 3

if message == "a":
    print(2 + 3)
elif message == "b":
    print("Bonjour !")
elif message == "c":
    print(2 ** 3)
else:
    print("mauvais choix")

# Comme le if, avec un match
match message:
    case "a":
        print(2 + 3)
    case "b":
        print("Bonjour")
    case "c":
        print(2 ** 3)
    case _:
        print("Mauvais choix")