# Demander à l'utilisateur de saisir une chaine de caractère s
s = input("Entrez une chaine de caractère : ")

voyelles = 0
consonnes = 0

liste_voyelles = ['a', 'e', 'i', 'o', 'u', 'y']

for c in s:
  if c.lower() in liste_voyelles:
    voyelles += 1
  elif c.isalpha():
    consonnes += 1

print("La chaine", s, "possède", voyelles, "voyelle(s) et", consonnes, "consonne(s).")
#Encore une petite modifications
#une deuxieme petite modification