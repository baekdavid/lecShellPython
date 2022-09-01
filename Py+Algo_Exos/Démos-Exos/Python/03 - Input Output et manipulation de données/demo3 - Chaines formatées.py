a = 2
b = 3
c = 6

print(str(a) + " x " + str(b) + " = " + str(c))
print(a, "x", b, "=", c)
print("{0} x {1} = {2}".format(a, b, c))  # Python 2
print(f"{a} x {b} = {c}")                 # Python 3


print(f"La somme de 2 et 3 est {2+3}") 