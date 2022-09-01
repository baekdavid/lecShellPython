<?xml version="1.0" encoding="UTF-8"?>
<Algo>
    <description texte="" courant="FIN_POUR"/>
    <extension extnom="inactif"/>
    <fonction fctetat="inactif" fctcode=""/>
    <F2 F2defaut="" F2lignes="" F2para="" F2etat="inactif"/>
    <repere repetat="inactif" repcode="-10#10#-10#10#2#2"/>
    <param arrondiAuto="vrai" epaisseurPoint="2" totalAffichages="1000" maxBoucle="500000" nbDecimales="8" totalBoucles="5000000" epaisseurLigne="2"/>
    <item code="200#declarationfonctions" algoitem="FONCTIONS_UTILISEES"/>
    <item code="100#declarationsvariables" algoitem="VARIABLES">
        <item code="1#NOMBRE#nombreUtilisateur" algoitem="nombreUtilisateur EST_DU_TYPE NOMBRE"/>
        <item code="1#NOMBRE#compteur1" algoitem="compteur1 EST_DU_TYPE NOMBRE"/>
        <item code="1#NOMBRE#compteur2" algoitem="compteur2 EST_DU_TYPE NOMBRE"/>
        <item code="1#CHAINE#texte" algoitem="texte EST_DU_TYPE CHAINE"/>
    </item>
    <item code="101#debutalgo" algoitem="DEBUT_ALGORITHME">
        <item code="19# Demander le nombre à l'utilisateur" algoitem="// Demander le nombre à l'utilisateur"/>
        <item code="4#Nombre entier supérieur à 1, limite de l'arbre ? #0" algoitem="AFFICHER &quot;Nombre entier supérieur à 1, limite de l'arbre ? &quot;"/>
        <item code="2#nombreUtilisateur#pasliste" algoitem="LIRE nombreUtilisateur"/>
        <item code="12#compteur1#1#nombreUtilisateur" algoitem="POUR compteur1 ALLANT_DE 1 A nombreUtilisateur">
            <item code="13#debutpour" algoitem="DEBUT_POUR"/>
            <item code="5#texte#&quot;&quot;#pasliste" algoitem="texte PREND_LA_VALEUR &quot;&quot;"/>
            <item code="12#compteur2#1#compteur1" algoitem="POUR compteur2 ALLANT_DE 1 A compteur1">
                <item code="13#debutpour" algoitem="DEBUT_POUR"/>
                <item code="5#texte#texte + compteur2#pasliste" algoitem="texte PREND_LA_VALEUR texte + compteur2"/>
                <item code="14#finpour" algoitem="FIN_POUR"/>
            </item>
            <item code="3#texte#1#pasliste" algoitem="AFFICHER texte"/>
            <item code="14#finpour" algoitem="FIN_POUR"/>
        </item>
    </item>
    <item code="102#finalgo" algoitem="FIN_ALGORITHME"/>
</Algo>
