let cout1= 10, cout2=8, prixTotal;  //Déclaration des variables
let nombreDePhotographies= parseInt(prompt("Entrer le nombre de photocopies"));  //Déclaration de la variable et l'initialisation de la variable par l'utilisateur

/*Si le nombre de photographies est supérieur à 20, on soustrait 20 dans ce nombre et puis on multiplie le 20 soustrait fois 
le premier prix:10centimes; Et le reste, on le multiplie fois le deuxième prix:8centimes. Ensuite on additionne les deux nombres qu'on va trouver
en l'affectant à la variable prixTotal*/

if (nombreDePhotographies>20) {
    nombreDePhotographies= nombreDePhotographies - 20;
    prixTotal= (cout1*20) + (nombreDePhotographies*cout2);
} else { //Sinon on multiplie directement le nombre de photographies fois 20 tout en affectant la valeur trouvée à la variable prixTotal
    prixTotal= nombreDePhotographies*cout1;
}
console.log(prixTotal + " centimes")