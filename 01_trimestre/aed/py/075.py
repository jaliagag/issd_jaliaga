#| Confeccionar un programa que permita: 
#a| Cargar una lista de 10 elementos enteros. 
#b| Generar dos listas a partir de la primera. En una guardar los valores positivos y en otra los negativos. 
#c| Imprimir las dos listas generadas.

q = 10

def cargar(cantidad):
    enteros = []
    for i in range(cantidad):
        enteros.append(int(input('ingrese un entero: ')))
    return enteros

def comparar(lista):
    positivos = []
    negativos = []
    for i in range(len(lista)):
        if lista[i] >= 0:
            positivos.append(lista[i])
        else:
            negativos.append(lista[i])
    return positivos, negativos

print(comparar(cargar(q)))