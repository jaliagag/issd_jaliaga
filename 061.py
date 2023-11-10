#| Crear una lista de 5 enteros y cargarlos por teclado.
#Borrar los elementos mayores o iguales a 10 y generar una nueva lista con dichos valores.

lista = [ 10,11,4,-1,120,56,0,30,9]
nueva_lista = []

position = 0
while position < len(lista):
    if lista[position] > 9:
        nueva_lista.append(lista[position])
        lista.pop(position)
    else:
        position += 1

print('final original', lista)
print('final nueva', nueva_lista)
