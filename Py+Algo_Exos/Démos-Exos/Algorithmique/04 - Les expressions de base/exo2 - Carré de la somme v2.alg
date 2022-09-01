<?xml version="1.0" encoding="UTF-8"?>
<Algo>
    <description texte="" courant="AFFICHER resultat"/>
    <extension extnom="inactif"/>
    <fonction fctetat="inactif" fctcode=""/>
    <F2 F2etat="inactif" F2defaut="" F2para="" F2lignes=""/>
    <repere repetat="inactif" repcode="-10#10#-10#10#2#2"/>
    <param epaisseurLigne="2" epaisseurPoint="2" arrondiAuto="vrai" totalBoucles="5000000" maxBoucle="500000" nbDecimales="8" totalAffichages="1000"/>
    <item code="200#declarationfonctions" algoitem="FONCTIONS_UTILISEES"/>
    <item code="100#declarationsvariables" algoitem="VARIABLES">
        <item code="1#NOMBRE#a" algoitem="a EST_DU_TYPE NOMBRE"/>
        <item code="1#NOMBRE#b" algoitem="b EST_DU_TYPE NOMBRE"/>
        <item code="1#NOMBRE#resultat" algoitem="resultat EST_DU_TYPE NOMBRE"/>
        <item code="1#CHAINE#texte" algoitem="texte EST_DU_TYPE CHAINE"/>
    </item>
    <item code="101#debutalgo" algoitem="DEBUT_ALGORITHME">
        <item code="4#Donnez deux nombres, l'un après l'autre#0" algoitem="AFFICHER &quot;Donnez deux nombres, l'un après l'autre&quot;"/>
        <item code="2#a#pasliste" algoitem="LIRE a"/>
        <item code="2#b#pasliste" algoitem="LIRE b"/>
        <item code="5#texte#&quot;(&quot; + a + &quot; + &quot; + b + &quot;) ^ 2&quot;#pasliste" algoitem="texte PREND_LA_VALEUR &quot;(&quot; + a + &quot; + &quot; + b + &quot;) ^ 2&quot;"/>
        <item code="3#texte#1#pasliste" algoitem="AFFICHER texte"/>
        <item code="5#texte#a + &quot; ^ 2 + 2 * &quot; + a + &quot; * &quot; + b + &quot; + &quot; + b + &quot; ^ 2&quot;#pasliste" algoitem="texte PREND_LA_VALEUR a + &quot; ^ 2 + 2 * &quot; + a + &quot; * &quot; + b + &quot; + &quot; + b + &quot; ^ 2&quot;"/>
        <item code="3#texte#1#pasliste" algoitem="AFFICHER texte"/>
        <item code="19# (a + b) ^ 2" algoitem="// (a + b) ^ 2"/>
        <item code="5#resultat#pow(a + b, 2)#pasliste" algoitem="resultat PREND_LA_VALEUR pow(a + b, 2)"/>
        <item code="3#resultat#0#pasliste" algoitem="AFFICHER resultat"/>
    </item>
    <item code="102#finalgo" algoitem="FIN_ALGORITHME"/>
</Algo>
