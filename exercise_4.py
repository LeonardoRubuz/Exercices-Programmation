# Un tas d'exercices

# Fonction triangle
def triangle(n):
    nombre = 0
    for i in range(n+1):
        nombre += i
    return nombre
#print(triangle(8))

# Fonction nombre de diviseurs
def nbre_diviseurs(n):
    compte = 0
    for i in range(1, n+1):
        if n % i == 0:
            compte+=1
    return compte
#print(nbre_diviseurs(7))

# Quotient de deux factorielles
def factorielle(n):
    fact = 1
    if n == 0:
        fact = 1
        return fact
    else:
        for i in range(1, n+1):
            fact *= i
        return fact

#print(factorielle(15)/factorielle(10))

def factorielleParité():
    factPair = factImpair = 1
    for i in range(1, 101):
        if i % 2 == 0:
            factPair *= i
        elif i % 2 == 1:
            factImpair *= i
    print('Factoriel des nombres pairs : ',str(factPair), '\n', 'Factoriel des nombres impairs : ', str(factImpair))

#factorielleParité()    