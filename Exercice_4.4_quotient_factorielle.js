
let somme= 0, nbre1= parseInt(prompt("Entrer un nombre"));
for(let i=0; i<=nbre1; i++) {
    if(i==0) {
        somme++;
    } else {
        somme*= i;
    }
}
console.log(somme);

let somme1= 0, nbre2= parseInt(prompt("Entrer un nombre"));
for(let i=0; i<=nbre2; i++) {
    if(i==0) {
        somme1++;
    } else {
        somme1*= i;
    }
}
console.log(somme1);

console.log("Le quotient des factorielles donne " + somme/somme1);