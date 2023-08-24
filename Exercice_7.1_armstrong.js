function somme_cubes_chiffres(n) {
    n= n.toString();
    let sum= 0;
    for(let i=0; i<n.length; i++) {
        sum+= Math.pow(n[i],3);
    }
    console.log(sum);
}
somme_cubes_chiffres(parseInt(prompt("Entrer un nombre entier pour voir si c'est un nombre armstrong")));
