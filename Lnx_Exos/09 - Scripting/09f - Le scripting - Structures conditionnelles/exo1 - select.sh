#!/bin/bash

# Demande le chemin du fichier
echo -n "Chemin du fichier : "
read chemin

# Le fichier existe
if [[ -e "$chemin" ]] ; then
    select choix in "Afficher" "Modifier" "Ne rien faire" ; do
        case "$choix" in
            # Afficher le fichier
            "Afficher")
                cat "$chemin"
                break
            ;;
            # Modifier le fichier
            "Modifier")
                nano "$chemin"
                break
            ;;
            # Ne rien faire
            "Ne rien faire")
                break
            ;;
            # Choix non valide
            *)
                echo "Choix non valide"
            ;;
       esac
    done

# Le fichier n'existe pas
else
    # Previent l'utilisateur
    echo "ATTENTION, le fichier $chemin n'existe pas !"

    # Demande du choix
    select choix in "Creer le fichier" "Ne rien faire" ; do
        case "$choix" in
            # Choix creation
            "Creer le fichier")
                touch "$chemin"
                break
            ;;
            # Choix non creation
            "Ne rien faire")
                break
            ;;
            # Choix non valide
            *)
                echo "Choix non valide"
            ;;
        esac
    done
fi

