#Desarrollar una función que reciba un string como parámetro y nos muestre la cantidad de
#vocales. Llamar a la función desde el bloque principal del programa 3 veces con string distintos

def vocales(evaluate):
    counter=0
    voca=['a','e','i','o','u']
    for i in evaluate:
        if i in voca:
            counter+=1

    print('vocales: ',counter)

for i in range(3):
    stringme=input('ingrese un texto: ')
    vocales(stringme)


