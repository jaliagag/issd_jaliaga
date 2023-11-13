# Confeccionar un programa con las siguientes funciones: 
#a| Cargar una lista de 5 enteros. 
#b| Retornar el mayor y menor valor de la lista mediante una tupla. 
#Desempaquetar la tupla en el bloque principal y mostrar el mayor y menor

q = 9

def cargar(cantidad):
    enteros = []
    for i in range(cantidad):
        enteros.append(int(input('ingrese un entero: ')))
    return enteros

def mayormenor(lista):
    mayor = lista[0]
    menor = lista[0]
    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
        elif lista[i] > mayor:
            mayor = lista[i]
    return mayor, menor

carga = cargar(q)
#carga = [5,6,7,6,5,4,56,43,23,2,3]
x = mayormenor(carga)
print(x)
print(type(x))









