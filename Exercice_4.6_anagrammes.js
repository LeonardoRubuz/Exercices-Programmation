let mot1= "fleur", mot2= "tennis"
let somme= 1
for(let i=1; i<=mot1.length; i++) {
    somme*= i
}
console.log("Le mot " + mot1 + " a " + somme + " anagrammes")
somme= 1
for(let i=1; i<=mot2.length; i++) {
    somme*= i
}
console.log("Le mot " + mot2 + " a " + somme + " anagrammes")