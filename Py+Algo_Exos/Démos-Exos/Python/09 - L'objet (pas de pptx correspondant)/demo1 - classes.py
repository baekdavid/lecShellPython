class Chien:
    # Définition des propriétés
    # "Constructeur"
    def __init__(self, prenom, race, date_naissance):
        self.prenom = prenom
        self.race = race
        self.date_naissance = date_naissance
        self.taille_poils = 10
    # prenom
    # race
    # date de naissace

    # Aboyer
    def aboyer(self):
        print("Waff")
    # Manger
    def manger(self):
        print("nom"*5)
    # Se faire raser
    def sefaireraser(self):
        self.taille_poils = 2

chien1 = Chien('toto', 'labrador', '01/01/2020')
chien2 = Chien('maxou', 'pékinois', '08/06/2018')

print(chien1.race)
print(chien2.date_naissance)

chien1.manger()
chien2.aboyer()

print(chien1.taille_poils)
chien1.sefaireraser()
print(chien1.taille_poils)

print(chien2.taille_poils)