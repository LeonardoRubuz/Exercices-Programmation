"""Quand on exécute truc(10), la fonction affiche 10 et renvoie 20. 
La fonction s’arrête après le premier return et n’exécute pas les instructions suivantes.
Donc, 30 et 40 ne sont pas affichés.
Quand on exécute bidule(10), la fonction affiche 10 et 20, puis renvoie 30.
La fonction s’arrête également après le premier return et n’exécute pas l’instruction suivante.
Donc, 40 n’est pas affiché"""
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