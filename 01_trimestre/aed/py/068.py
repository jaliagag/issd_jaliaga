#Confeccionar una función que calcule la superficie de un rectángulo y la retorne, la función recibe como parámetros los valores de dos lados distintos:
#def retornar_superficie(lado1,lado2):
#En el bloque principal del programa cargar los lados de dos rectángulos y luego mostrar cuál de los dos tiene una mayor superficie.

lista = []

def retornar_superficie(lado1,lado2):
    return lado1*lado2

for i in range(2):
    print(f'Rectangulo {i+1}')
    l1 = int(input('Lado 1: '))
    l2 = int(input('Lado 2: '))
    lista.append(retornar_superficie(l1,l2))

if lista[0] > lista[1]:
    print('el rectangulo 1 es mayor al 2')
elif lista[1] > lista[0]:
    print('el rectangulo 2 es mayor al 1')
else:
    print('ambos rectangulos tienen la misma superficie')


