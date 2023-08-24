s = input("Entrez une chaine de caractère : ")

indice = s.find('a')

# Si l'indice est différent de -1, alors la chaine contient la lettre 'a'
if indice != -1:
  print("La chaine contient la lettre 'a' à la position", indice + 1)
else:
  print("La chaine ne contient pas la lettre 'a'")
