#Cargar una lista con 5 elementos enteros. 
#Imprimir el mayor y un mensaje si se repite dentro de la lista 
#(es decir si dicho valor se encuentra en 2 o más posiciones en la lista)

array = [7,27,101,101,7,84,101,57]
empty = []
double = []

mayor = array[0]

for i in array:
    if i > mayor:
        mayor = i

    if i not in empty:
        empty.append(i)
    else:
        double.append(i)

for i in double:
    if i == mayor:
        print(f'el número mayor se repite: {i}')
        break
print(f'mayor: {mayor}')
