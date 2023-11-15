#| Cargar una lista con 5 elementos enteros.
#Ordenarla de menor a mayor y mostrarla por pantalla, luego ordenar
#de mayor a menor e imprimir nuevamente
import random

lista = []

for i in range(5):
    lista.append(random.randint(1,1000))

print('orig:',lista)

for i in range(len(lista)-1):
    for x in range(len(lista)-i-1):
        if lista[x] > lista[x+1]:
            aux = lista[x]
            lista[x] = lista[x+1]
            lista[x+1] = aux

print('menor a mayor:',lista)

for i in range(len(lista)-1):
    for x in range(len(lista)-i-1):
        if lista[x] < lista[x+1]:
            aux = lista[x]
            lista[x] = lista[x+1]
            lista[x+1] = aux

print('mayor a menor:',lista)
