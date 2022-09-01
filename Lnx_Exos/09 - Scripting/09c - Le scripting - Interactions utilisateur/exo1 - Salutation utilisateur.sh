#!/bin/bash

# Demande a l'utilisateur
# echo -n ne met pas de saut de ligne apres echo 
#    on se retrouve donc avec le read a la suite des :
echo -n "Quel est votre prenom : "
read

# Affiche le resultat
echo "Bonjour $REPLY !"