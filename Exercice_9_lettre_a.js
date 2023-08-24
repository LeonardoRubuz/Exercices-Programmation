let s= prompt("Entrer une chaine de caractère"), n=0;
for(let i=0; i<s.length; i++) {
    if(s[i]=="a") {
        n++;
        console.log("La lettre a se trouve à la position " + i);
    }
}
if(n==0) {
    console.log("La chaine entrée ne contient pas de lettre a");
}
