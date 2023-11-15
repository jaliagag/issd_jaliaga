# Elaborar una función que nos retorne el perímetro de un cuadrado pasando como parámetros el valor de un lado.

def perimetro(lado):
    return lado*4

seguir = 0 

while seguir == 0:
    p2 = int(input('Lado del cuadrado: '))
    print(perimetro(p2))
    p = int(input('Continuar? 0 para si, 1 para no: '))
    seguir = p


