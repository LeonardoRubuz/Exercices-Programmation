let str= prompt("Entrer une phrase")    // Demande à l'utilisateur d'entrer une phrase
str= str.split(' ')          // Sépare la phrase en mots
let first= str[0]            // Affectation du premier mot à first
str[0]= str[str.length-1]    // Attribution de la valeur du dernier mot au premier
str[str.length-1]= first     // Attribution de la valeur du premier mot au dernier
str= str.join(' ')           // Rassemble tous les mots pour reconstituer la phrase
console.log(str)