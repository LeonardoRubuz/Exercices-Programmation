# Script 1
for i in range(3):
 print("bidule")
print("truc")
"""Donc, la boucle for exécute trois fois l’instruction print('bidule'),
ce qui affiche le mot bidule sur trois lignes différentes. 
Ensuite, le script exécute l’instruction print('truc') qui n’est pas dans la boucle for, donc elle n'est exécutée qu'une seule fois."""

# Script 2 
for i in range(3):
 print("bidule")
for j in range(4):
 print("truc")
"""
 elle affiche le mot ‘bidule’ sur trois lignes différentes.
la boucle for exécute quatre fois l’instruction print('truc')
"""
# Script 3
for i in range(3):
 print("bidule")
 for j in range(4):
 print("truc")
 """
  La première boucle for est identique à celle du script 1, elle affiche le mot 
  bidule sur trois lignes différentes. Mais pour chaque itération de la première boucle for,
 il y a une deuxième boucle for qui s’exécute.
 la boucle for exécute quatre fois l’instruction print('truc')"""