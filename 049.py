#Realizar un programa que pida la carga de dos listas numéricas 
#enteras de 4 elementos cada una. Generar una tercer lista que 
#surja de la suma de los elementos de la misma posición de cada 
#lista. Mostrar esta tercer lista.

lista1 = []
lista2 = []

for i in range(1,3):
    for x in range(4):
        q = int(input(f'cargar número para lista {i}: '))
        if i == 1:
            lista1.append(q)
        elif i == 2:
            lista2.append(q)

lista3 = []

for i in range(len(lista1)):
    suma = lista1[i] + lista2[i]
    lista3.append(suma)

#print(lista1)
#print(lista2)
print(lista3)

