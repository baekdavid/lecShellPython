#!/bin/bash

# Demande les informations a l'utilisateur
echo -n "identifiant : "
read identifiant
echo -n "nom complet : "
read nomcomplet

# Affiche le resultat
echo "Je vais creer l'identifiant ${identifiant:=nouveau} pour l'utilisateur ${nomcomplet:-$identifiant}"