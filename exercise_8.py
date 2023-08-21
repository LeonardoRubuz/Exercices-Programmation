from math import sqrt, floor

valeur = int(input("Veuiller renseigner un nombre : \n"))
if sqrt(valeur) - floor(sqrt(valeur)) == 0:
    print(str(valeur) + " est un carré parfait")
else:
    print(str(valeur) + " n'est pas un carré parfait")

