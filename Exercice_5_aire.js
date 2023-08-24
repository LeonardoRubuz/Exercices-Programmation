function aire(d) {
    let surface= (Math.PI * Math.pow(d/2,2));
    console.log(surface.toFixed(2)+" m²");
}
aire(parseInt(prompt("Entrer une valeur pour le diamètre")));