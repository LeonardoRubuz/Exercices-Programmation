let i=1, somme=0
while(somme<50) {
    somme=0
    for(let j=1; j<=i; j++) {
        if(i%j==0) {
            somme++
        }
    }
    if(somme>=50) {
        console.log(i)
    }
    i++
}