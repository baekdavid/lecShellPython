class Vehicule:
    # Constructeur
    def __init__(self, couleur, plaque, date_achat):
        self.couleur = couleur
        self.plaque = plaque
        self.date_achat = date_achat
        self.est_demarre = False
    
    # Actions
    def demarrer(self):
        print("vroum")
        self.est_demarre = True

    def arreter(self):
        print("Pas vroum")
        self.est_demarre = False

# La classe voiture "herite" de vehicule
class Voiture(Vehicule):
    # Constructeur
    def __init__(self, couleur, plaque, date_achat, nb_places):
        # Appelle le constructeur du parent
        super().__init__(couleur, plaque, date_achat)
        self.nb_places = nb_places
    pass

class Decapotable(Voiture):
    # Constructeur
    def __init__(self, couleur, plaque, date_achat, nb_places):
        super().__init__(couleur, plaque, date_achat, nb_places)
        self.toit_ouvert = False

    def decapoter(self):
        self.toit_ouvert = True
    def recapoter(self):
        self.toit_ouvert = False

class Camion:
    pass

class TransPalette:
    pass

voiture1 = Voiture("bleue", "aa-111-aa", "01/01/2022", 4)
print(voiture1.couleur)
voiture1.demarrer()
try:
    voiture1.decapoter()
except:
    print("Voiture1 n'est pas décapotable")

decapotable1 = Decapotable("verte", "bb-111-bb", "01/01/2020", 2)
print(decapotable1.couleur)     # couleur vient de Vehicule
print(decapotable1.nb_places)   # nb_places vient de Voiture
decapotable1.demarrer()         # Vient de Vehicule
print(decapotable1.toit_ouvert) # Vient de Decapotable
decapotable1.decapoter()
print(decapotable1.toit_ouvert)
