#Almacenar en una lista de 5 elementos tuplas que guarden el nombre de un pais 
#y la cantidad de habitantes. Definir tres funciones, en la primera cargar la 
#lista, en la segunda imprimirla y en la tercera mostrar el nombre del país 
#con mayor cantidad de habitantes.

#lista = [('Argentina',40),('EE.UU',300),('Alemania',80),('Brasil',200),('Chile',23)]

def cargar(rango):
    devolver = []
    for i in range(rango):
        x = input('Nombre del pais: ')
        y = int(input('Cantidad de habitantesi: '))
        z = x,y
        devolver.append(z)

def ver(message):
    print(message)

def mayor_habitantes(una_lista):
    mayor = una_lista[0][1]
    pais = una_lista[0][0]
    for i in range(len(una_lista)):
        if una_lista[i][1] > mayor:
            mayor = una_lista[i][1]
            pais = una_lista[i][0]
    return pais

lista = cargar(5)
ver(lista)
print(mayor_habitantes(lista))

