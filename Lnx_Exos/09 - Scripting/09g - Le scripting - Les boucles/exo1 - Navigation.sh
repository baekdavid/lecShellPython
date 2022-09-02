#!/bin/bash

# Deplacer le shell dans le dossier personnel de l'utilisateur
cd

# Boucle (infinie) principale pour le projet
while :
do
   # Propose les fichiers/dossiers a l'utilisateur
   select el in $(ls) "_remonter au parent" "_creer fichier" "_creer dossier" "_changer dossier" "_quitter"
   do
       # Actions en fonction du choix
       case "$el" in
           # Quitter
           "_quitter")
               exit
           ;;

           # Changer dossier
           "_changer dossier")
               # Demande le chemin a l'utilisateur
               echo -n "Emplacement du nouveau dossier : "
               read chemin
               # Si le dossier existe
               if [[ -d "$chemin" ]]; then
                   cd "$chemin"
               # Si le dossier n'existe pas
               else
                   echo "Le dossier $chemin n'existe pas" >&2
               fi
           ;;

           # Creer fichier
           "_creer fichier")
               # Demande le nom du fichier a l'utilisateur
               echo -n "Nom du nouveau fichier : "
               read fichier
               # Si le fichier existe
               if [[ -e "$fichier" ]]; then
                   echo "Le fichier $fichier existe deja" >&2
               # Si le fichier n'existe pas
               else
                   touch "$fichier"
               fi
           ;;

           # Creer dossier
           "_creer dossier")
               # Demande le nom du dossier a l'utilisateur
               echo -n "Nom du nouveau dossier : "
               read dossier
               # Si le dossier existe
               if [[ -e "$dossier" ]]; then
                   echo "Le dossier $dossier existe deja" >&2
               # Si le dossier n'existe pas
               else
                   mkdir "$dossier"
               fi
           ;;

           # Remonter au parent
           "_remonter au parent")
               cd ..
           ;;

           # Choix dossier/fichier
           *)
               # Si le choix n'est pas valide
               if [[ -z "$el" ]]; then
                   echo "Choix invalide !" >&2
               # Si le choix est valide
               else
                   # Choix sur l'element
                   select choix in "ouvrir" "renommer" "supprimer"
                   do
                       # Choix de l'action sur l'element
                       case "$choix" in
                           # Ouvrir l'element
                           "ouvrir")
                               if [[ -d "$el" ]]; then
                                   cd "$el"
                               else
                                   cat "$el"
                               fi
                           ;;
                           # Renommer l'element
                           "renommer")
                               # Demande le nouveau nom de l'element a l'utilisateur
                               echo -n "Nouveau nom de l'element : "
                               read fichier
                               # Si le fichier existe
                               if [[ -e "$fichier" ]]; then
                                   echo "Le fichier $fichier existe deja" >&2
                               # Si le fichier n'existe pas
                               else
                                   mv "$el" "$fichier"
                               fi
                           ;;
                           # Supprimer l'element
                           "supprimer")
                               if [[ -d "$el" ]]; then
                                   rm -r "$el"
                               else
                                   rm "$el"
                               fi
                           ;;
                       esac
                       # Sort du select
                       break
                   done
               fi
           ;;
       esac

       # Sort du select
       break
   done
done