# Coder une fonction prenant un entier N en paramètre et retournant la valeur à la position N dans la suite de fibonacci

# Fonction fibonacci
def fibo(index):
    # Vérifie que le nombre est >= 1
    if index < 1:
        print("L'index doit être supérieur ou égal à 1")
        return -1
    
    # Constuire la liste de fibonacci jusqu'à index
    suite_fibo: list = [1, 1]
    # _ représente l'absence de variable. Le programme n'a pas besoin du compteur
    for _ in range(2, index):
        # append permet d'ajouter un élément à une liste
        suite_fibo.append(suite_fibo[-1] + suite_fibo[-2])
    # Si on ne veut pas utiliser append:
    # for i in range(2, index):
    #     suite_fibo[i] = suite_fibo[-1] + suite_fibo[-2]

    # Retourne la valeur à la fin de la liste
    return suite_fibo[-1]

# Tests
print(fibo(1))
print(fibo(5))
print(fibo(10))
print(fibo(16))