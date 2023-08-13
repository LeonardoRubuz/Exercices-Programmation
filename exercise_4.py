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

 