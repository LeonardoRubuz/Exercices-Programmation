function factorielle(n) {
    let sum=1;
    for(let i=1; i<=n; i++) {
        sum*=i;
    }
    console.log(sum);
}
factorielle(parseInt(prompt("Entrer un nombre entier")));