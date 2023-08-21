valeur = input("Veuiller renseigner un mot ou une courte phrase : \n")
occurenceA = []
for element in range(len(valeur)):
    if valeur[element] =='a':
        occurenceA.append(element)

if len(occurenceA) == 0:
    print('Le texte renseigné ne comprend pas la lettre "a"')
elif len(occurenceA) == 1:
    print('La lettre "a" se trouve à la position ', str(occurenceA[0]+1))

