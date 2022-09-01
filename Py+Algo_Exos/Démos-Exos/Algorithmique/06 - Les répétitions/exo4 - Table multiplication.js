// Demande le chiffre à l'utilisateur
const chiffreUtilisateur = prompt("Pour quel chiffre souhaitez-vous la table de multiplication ?");

// Calcul de la table
for(let multiplicateur = 1; multiplicateur <= 10; multiplicateur++) {
    const produit = multiplicateur * chiffreUtilisateur;
    console.log(multiplicateur + "x" + chiffreUtilisateur + "=" + produit)
}