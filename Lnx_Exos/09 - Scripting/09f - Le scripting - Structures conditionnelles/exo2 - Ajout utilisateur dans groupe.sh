#!/bin/bash

# -- Traitement du groupe
# Demande le groupe
echo -n "Groupe a modifier : "
read groupe

# Teste que le resultat est non vide
if [[ -z "$groupe" ]]; then
    # Previent l'utlisateur
    echo "Le nom du groupe ne peut etre vide. Fin du programme." >&2
    # Stoppe l'execution avec une valeur de sortie en erreur
    exit 1
fi

# Teste que le groupe existe
if [[ -z $(grep "^${groupe}:" /etc/group) ]]; then
    # Previent l'utlisateur
    echo "Le groupe ${groupe} n'existe pas. Fin du programme." >&2
    # Stoppe l'execution avec une valeur de sortie en erreur
    exit 1
fi

# -- Traitement de l'utilisateur
# Demande l'utilisateur
echo -n "Utilisateur a ajouter au groupe : "
read utilisateur

# Teste que le resultat est non vide
if [[ -z "$utilisateur" ]]; then
    # Previent l'utilisateur
    echo "Le nom de l'utilisateur ne peut etre vide. Fin du programme." >&2
    # Stoppe l'execution avec une valeur de sortie en erreur
    exit 1
fi

# Teste que l'utilisateur existe
if [[ -z $(grep "^${utilisateur}:" /etc/passwd) ]]; then
    # Previent l'utlisateur
    echo "L'utilisateur ${utilisateur} n'existe pas. Fin du programme." >&2
    # Stoppe l'execution avec une valeur de sortie en erreur
    exit 1
fi

# -- Utilisateur absent du groupe
# Teste si le groupe fait partie de la liste des groupes de l'utilisateur
#   groups "$utilisateur" => Affiche les groupes de l'utilisateur
#   cut -d: -f2 => Ne garde que la liste des groupes
#   grep "$groupe" => Cherche si le groupe est dans la liste
if [[ -n $(groups "$utilisateur" | cut -d: -f2 | grep "$groupe") ]]; then
    # Previent l'utilisateur
    echo "L'utilisateur $utilisateur est deja dans le groupe $groupe. Fin du programme" >&2
    # Stoppe l'execution avec une valeur de sortie en erreur
    exit 1
fi

# -- Ajout de l'utilisateur au groupe
# Commande usermod (necessite root / sudo)
usermod -aG "$groupe" "$utilisateur"