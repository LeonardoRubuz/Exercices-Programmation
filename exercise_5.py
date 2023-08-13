from math import pi

def circleSurface(diameter:float):
    return round(pi * pow(diameter/2, 2), 3)

print(str(circleSurface(10.5)) + "m²" )