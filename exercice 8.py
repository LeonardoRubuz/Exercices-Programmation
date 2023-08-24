n = int(input("Entrez un nombre entier : "))

import math

racine = math.sqrt(n)

# Si la racine est un entier, alors n est un carré parfait
if racine == int(racine):
  print(n, "est un carré parfait")
else:
  print(n, "n'est pas un carré parfait")
