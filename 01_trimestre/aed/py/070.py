#Crear una lista de enteros por asignación. Definir una función que reciba una 
#lista de enteros y un segundo parámetro de tipo entero. Dentro de la función 
#mostrar cada elemento de la lista multiplicado por el valor entero enviado. 

lista=[3, 7, 8, 10, 2] 

def multiplicar(una_lista, un_int):
    for i in una_lista:
        print(i*un_int)

multiplicar(lista,3)