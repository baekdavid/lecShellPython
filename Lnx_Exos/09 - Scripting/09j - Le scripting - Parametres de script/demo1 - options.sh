#!/bin/bash

# Initialisation des valeurs par defaut
NBMOTDEPASSE=0
LONGUEURMOTDEPASSE=8

# Utilisation des options
#   "l:" défini l'option l, les : precisent qu'un argument est attendu
#   "n:" défini l'option n, les : precisent qu'un argument est attendu
while getopts "l:n:" option;
do
  if [[ "$option" == "l" ]]; then
    LONGUEURMOTDEPASSE=$OPTARG
  elif [[ "$option" == "n" ]]; then
    NBMOTDEPASSE=$OPTARG
  fi
done

function monGenerateurDeMotDePasse () {
  # Recuperation de la longueur en parametre avec un defaut a 8
  longueur=${1:-8}

  # Construction de la liste de tous les caracteres possibles
  caracteres="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

  # Preparation de la variable mot de passe
  motdepasse=""

  # Pour chaque caractere du mot de passe
  for index in $(seq 1 $longueur); do
    # Construction du caractere aleatoire
    # Si vous utilisez un tableau : car=${tableau[$(($RANDOM % ${#tableau[@]}))]}
    car=${caracteres:$(($RANDOM % ${#caracteres})):1}

    # Mise a jour du mot de passe
    motdepasse="$motdepasse$car"
  done

  # Affichage du mot de passe final
  echo "$motdepasse"
}

# Generer les mots de passe
for i in $(seq $NBMOTDEPASSE)
do
  monGenerateurDeMotDePasse $LONGUEURMOTDEPASSE
done