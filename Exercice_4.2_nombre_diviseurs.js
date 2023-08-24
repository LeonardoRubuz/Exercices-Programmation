function nbre_diviseurs(n) {
    let sum=0;
    for(let i=1; i<=n; i++) {
        if(n%i==0) {
            sum++;
        }
    }
    console.log(sum);
}
nbre_diviseurs(parseInt(prompt("Entrer un nombre")));