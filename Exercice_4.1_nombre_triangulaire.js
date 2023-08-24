function triangle(n) {
    let sum= 0;
    for(let i=1; i<=n; i++) {
        sum= sum + i;
    }
    console.log(sum);
}
triangle(parseInt(prompt("Entrer un nombre")));