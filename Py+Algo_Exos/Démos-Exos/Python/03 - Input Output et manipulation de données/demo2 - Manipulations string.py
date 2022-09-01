mon_texte = "Je suis une phrase"

# Portion de texte
print(mon_texte)
print(mon_texte[1])
print(mon_texte[1:5])    # "e su", De la position 1 inclue à la position 5 exclue : [1,5[
print(mon_texte[0:8])    # "Je suis " [0:8[
print(mon_texte[:8])     # "Je suis " [0:8[
print(mon_texte[8:18])   # "une phrase" [8:18[
print(mon_texte[8:])     # "une phrase" [8:18[
print(mon_texte[-5])     # "h", cinquième caractère en partant de la droite
print(mon_texte[:-2])    # "Je suis une phra", tout sauf les deux derniers caractères
print(mon_texte[1:9:2])  # "esi", [1,9[ par pas de 2
print(mon_texte[::3])    # "Jssnpa", tout le texte, une lettre sur trois

# Fonctions de chaines de caractères
print(len(mon_texte))              # Longueur de la chaine de caractère, "18"
print(mon_texte.startswith("abc")) # Teste si la chaine commence par "abc", "False"
print(mon_texte.startswith("Je"))  # Teste si la chaine commence par "abc", "True"
print(mon_texte.endswith("bla"))   # Teste si la chaine fini par "bla", "False"
print(mon_texte.endswith("ase"))   # Teste si la chaine fini par "ase", "True"
print(mon_texte.upper())
print(mon_texte.lower())
print(mon_texte.startswith("je"))
print(mon_texte.lower().startswith("je"))