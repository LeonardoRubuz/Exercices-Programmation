class personne {
    constructor(taille, poids, age) {
        this.taille= taille
        this.poids= poids
        this.age= age
    }
    imc() {
        return this.poids/Math.pow(this.taille,2)
    }
    interpretation() {
        if(res.imc()<=18.5) {
            return "INSUFFISANCE PONDERALE"
        } else if(res.imc()>=30) {
            return "OBESITE"
        } else {
            return "C'EST BON"
        }
    }
}

let res= new personne(parseFloat(prompt("Entrer votre taille en mètre")), parseFloat(prompt("Entrer votre poids en kg")), parseInt(prompt("Entrer votre âge")))
console.log("Vous avez " + res.age + " an(s)")
console.log("Votre imc est " + res.imc().toFixed(1))
console.log(res.interpretation())
