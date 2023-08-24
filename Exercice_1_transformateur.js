let time= 42569;
/* Déclaration et initialisation des variables. Ensuite prise de la partie entière avec Math.trunc pour les variables hours et minutes */
let hours= Math.trunc(time/3600), minutes= Math.trunc((time%3600)/60), secondes=(time%3600)%60;
console.log(hours+"h",minutes+"'",secondes+"s");