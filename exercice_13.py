class Personne:
    def __init__(self, taille, poids, age):
        self.taille = taille
        self.poids = poids
        self.age = age
        self.final_imc = 0

    def imc(self):
        self.final_imc = self.poids / (self.taille)**2

    def interpretation(self):
        if (self.final_imc <= 18.5):
            return print('Insuffisance pondérale')
        elif (self.final_imc >= 30):
            return print('Obésité')
        else:
            return print('IMC normale') 
        

leonardo = Personne(1.93, 100, 21)
leonardo.imc()
leonardo.interpretation()