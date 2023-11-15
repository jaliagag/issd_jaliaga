#Solicitar por teclado la cantidad de empleados que tiene la empresa.
#Crear y cargar una lista con todos los sueldos de dichos empleados.
#Imprimir la lista de sueldos ordenados de menor a mayor

import random

q_empleados = int(input('cantidad de empleados: '))
sueldos = []

for i in range(q_empleados):
    sueldos.append(random.randint(1000, 5000))

print(sueldos)

for k in range(q_empleados-1):
    for x in range(q_empleados-k-1):
        if sueldos[x]>sueldos[x+1]:
            aux = sueldos[x]
            sueldos[x]=sueldos[x+1]
            sueldos[x+1]=aux

print('ordenado',sueldos)
