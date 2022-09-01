#!/bin/bash

# Demande la phrase a l'utilisateur
echo -n "Phrase a developper : "
read phrase

# Converti les acronymes
phrase="${phrase//stp/s\'il te plait}"
phrase="${phrase//rdv/rendez-vous}"
phrase="${phrase//sncf/societe nationale des chemins de fer francais}"

# Affiche la phrase convertie
echo "$phrase"