# Calcul de prix avec remise
def prix(n:int):
    if n <= 20:
        price = 10 * n
    else:
        price = (10*20) + 8 * (n-20)
    return print(
        str(n) + ' photocopies vous coûteront :',
        str(price) + ' centimes'
    )

prix(30)