#!/bin/bash

# Demande les informations a l'utilisateur
echo -n "identifiant : "
read 
identifiant="${REPLY:-nouveau}"
echo -n "nom complet : "
read 
nomcomplet="${REPLY:-$identifiant}"

# Affiche le resultat
echo "Je vais creer l'identifiant $identifiant pour l'utilisateur $nomcomplet"