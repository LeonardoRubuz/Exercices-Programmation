def truc(x):
    print(x)
    return(2*x)
    print(3*x)
    return(4*x)

def bidule(x):
    print(x)
    print(2*x)
    return(3*x)
    print(4*x)  

print(truc(10)) # La valeur affichée est 10 et la valeur renvoyée est 20

print(bidule(10)) # Les valeurs affichées sont 10 et 20 et la valeur renvoyée est 30

#Pour ces deux fonctions, Python a ignoré les instructions placées après la première instruction 'return'