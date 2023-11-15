#Desarrollar una función que reciba una lista de string y nos retorne el que 
#tiene más caracteres. Si hay más de uno con dicha cantidad de caracteres debe 
#retornar el que tiene un valor de componente más baja. En el bloque principal 
#iniciamos por asignación la lista de string: 

palabras=["enero", "febrero", "marzo", "abril", "mayo", "junio"] 

def mascaracteres(una_lista):
    palabra = una_lista[0]
    for i in una_lista:
        if len(i) > len(palabra):
            palabra = i
        elif len(i) == len(palabra):
            if i > palabra:
                palabra = i
    return palabra



print("Palabra con mas caracteres:",mascaracteres(palabras))