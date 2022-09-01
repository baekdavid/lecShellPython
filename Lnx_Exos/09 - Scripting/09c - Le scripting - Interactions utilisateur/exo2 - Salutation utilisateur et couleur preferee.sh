#!/bin/bash

# Demande le prenom
echo -n "Votre prenom : "
read prenom

# Demande la couleur
echo -n "Votre couleur preferee : "
read couleur

# Affiche resultat
echo "Vous avez raison ${prenom}, le $couleur est une belle couleur"