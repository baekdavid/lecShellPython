#!/bin/bash
# Lecture du fichier
while read ligne
do
    # Lignes vides
    if [[ -z "$ligne" ]]; then
        echo "[LIGNE VIDE]"

    # Les commentaires
    # Version cut : elif [[ $(echo "$ligne" | cut -c 1) == "#" ]]; then
    # Version grep : elif [[ -n $(echo "$ligne" | grep "^#") ]]; then
    elif [[ "${ligne:0:1}" == "#" ]]; then
        echo "[COMMENTAIRE] ${ligne:2}"

    # Les lignes de donnees
    else
        # Recherche des cles valeurs
        #    -s permet de ne pas afficher la ligne si elle ne contient pas le delimiteur
        cle="$(echo $ligne | cut -sd "=" -f1)"
        valeur="$(echo $ligne | cut -sd "=" -f2)"

        # Ligne invalide
        #    || : OU (operateur logique)
        if [[ -z "$cle" || -z "$valeur" ]]; then
            echo "[CONTENU] ERREUR - format invalide : $ligne"
        # Ligne valide
        else
            echo "[CONTENU] $ligne"
        fi
    fi
# < ~/corrections/09i/fichier.conf : Fourni le contenu du fichier a la boucle
# > fichierconverti.txt : Redirige tous les echo dans fichierconverti.txt
done < ~/corrections/09i/fichier.conf > fichierconverti.txt