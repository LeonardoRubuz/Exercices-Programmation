def somme_cubes_chiffres(number:int):
    separatedList = list(str(number))
    for element in separatedList:
        separatedList[separatedList.index(element)] = pow(int(element),3)
    return sum(separatedList)

#print(somme_cubes_chiffres(256))

for i in range(10000):
    if i == somme_cubes_chiffres(i):
        print(i)
    else:
        pass