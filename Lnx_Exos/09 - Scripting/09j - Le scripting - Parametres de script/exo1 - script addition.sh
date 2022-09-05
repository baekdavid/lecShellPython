#!/bin/bash

# -- Gestion des options
# Declare les valeurs par defaut des flags (repere / mode / ...)
mode_verbeux=""

# Parcours les options
while getopts "vh" option
do
  # Traitement de l'option en cours
  case "$option" in
    # Option verbose
    v)
      mode_verbeux="oui"
    ;;
    # Option aide
    h)
      echo "Je suis de l'aide"
      exit # sortie du script, l'aide bloque l'execution
    ;;
  esac
done

# Retrait des options de la liste des arguments
#  $OPTIND represente l'index de la "future option" a traiter
shift $(($OPTIND - 1))

# -- Gestion des arguments
# Initialisation de la somme
somme=0

# Parcours des nombres
for nombre in $*
do
  # Calcul de la somme
  somme=$(($somme + $nombre))
  # Le mode verbeux
  if [[ -n "$mode_verbeux" ]]; then
    echo "Nombre en cours : $nombre | total : $somme"
  fi
done

# Affichage du resultat
echo "Somme : $somme"