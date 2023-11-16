# Definir una función que cargue una lista con palabras y la retorne. 
#Luego otra función tiene que mostrar todas las palabras de la lista que tienen más de 5 caracteres.

lista = [ 'hola', 'mundo' ]

def cargar(cantidad):
    palabras = []
    for i in range(cantidad):
        palabras.append(input('que desea ingresar?: '))
    return palabras

def mas_cinco(una_lista):
    mayores = []
    for i in una_lista:
        if len(i) >= 5:
            mayores.append(i)
    return mayores

print(mas_cinco(lista))

#print(cargar(2))

