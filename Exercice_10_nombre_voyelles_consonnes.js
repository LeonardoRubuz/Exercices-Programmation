let s= prompt("Entrer une chaine"), v=0, c=0;
for(let i=0; i<s.length; i++) {
    if(s[i]=="a" || s[i]=="e" || s[i]=="i" || s[i]=="o" || s[i]=="u" || s[i]=="y") {
        v++;
    } else if(s[i]== "") {
        continue;
    } else {
        c++;
    }
}
console.log("La chaine entrée contient " + v + " voyelles et " + c + " consonnes");