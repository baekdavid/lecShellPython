<?xml version="1.0" encoding="UTF-8"?>
<Algo>
    <description courant="AFFICHER texte" texte=""/>
    <extension extnom="inactif"/>
    <fonction fctcode="" fctetat="inactif"/>
    <F2 F2para="" F2etat="inactif" F2defaut="" F2lignes=""/>
    <repere repcode="-10#10#-10#10#2#2" repetat="inactif"/>
    <param totalAffichages="1000" epaisseurPoint="2" totalBoucles="5000000" nbDecimales="8" maxBoucle="500000" arrondiAuto="vrai" epaisseurLigne="2"/>
    <item code="200#declarationfonctions" algoitem="FONCTIONS_UTILISEES"/>
    <item code="100#declarationsvariables" algoitem="VARIABLES">
        <item code="1#CHAINE#prenom" algoitem="prenom EST_DU_TYPE CHAINE"/>
        <item code="1#CHAINE#nom" algoitem="nom EST_DU_TYPE CHAINE"/>
        <item code="1#CHAINE#texte" algoitem="texte EST_DU_TYPE CHAINE"/>
    </item>
    <item code="101#debutalgo" algoitem="DEBUT_ALGORITHME">
        <item code="4#Votre prénom ?#0" algoitem="AFFICHER &quot;Votre prénom ?&quot;"/>
        <item code="2#prenom#pasliste" algoitem="LIRE prenom"/>
        <item code="4#Votre nom ?#0" algoitem="AFFICHER &quot;Votre nom ?&quot;"/>
        <item code="2#nom#pasliste" algoitem="LIRE nom"/>
        <item code="5#texte#&quot;Bonjour &quot; + prenom + &quot; &quot; + nom#pasliste" algoitem="texte PREND_LA_VALEUR &quot;Bonjour &quot; + prenom + &quot; &quot; + nom"/>
        <item code="3#texte#0#pasliste" algoitem="AFFICHER texte"/>
    </item>
    <item code="102#finalgo" algoitem="FIN_ALGORITHME"/>
</Algo>
