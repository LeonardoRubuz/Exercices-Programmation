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

#prix(30)

# Alternative : Conversion en dollars dès que le prix dépasse 500 centimes
def prixDollars(n:int):
    if n <= 20:
        price = 10 * n
    else:
        price = (10*20) + 8 * (n-20)

    if price > 500:
        return print(
            str(n) + ' photocopies vous coûteront :',
            str(price/100) + ' dollars'
        )
    else:
        return print(
            str(n) + ' photocopies vous coûteront :',
            str(price) + ' centimes'
        )
    
prixDollars(60)