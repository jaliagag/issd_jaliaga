#Definir una lista de enteros por asignación en el bloque principal. Llamar a 
#una función que reciba la lista y nos retorne el producto de todos sus 
#elementos. 
#Mostrar dicho producto en el bloque principal de nuestro programa.

lista=[3, 7, 8, 10, 2] 

def list_mult(una_lista):
    resultado = 1
    for i in una_lista:
        resultado = resultado * i
    return resultado

print(list_mult(lista))

