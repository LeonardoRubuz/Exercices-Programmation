class Personne:
  def __init__(self, taille, poids, age):
    self.taille = taille
    self.poids = poids
    self.age = age

  def imc(self):
    IMC = self.poids / (self.taille ** 2)
    return IMC

  def interpretation(self):
    IMC = self.imc()
    if IMC <= 18.5:
      print("Insuffisance pondérale")
    elif IMC >= 30:
      print("Obésité")


p1 = Personne(1.8, 70, 25)
print(p1.imc()) # Affiche 21.604938271604937
p1.interpretation() # N'affiche rien car l'IMC est entre 18.5 et 30

p2 = Personne(1.6, 50, 30)
print(p2.imc()) # Affiche 19.531249999999996
p2.interpretation() # N'affiche rien car l'IMC est entre 18.5 et 30

p3 = Personne(1.7, 100, 40)
print(p3.imc()) # Affiche 34.602076124567475
p3.interpretation() # Affiche "Obésité"
