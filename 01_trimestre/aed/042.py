#Almacenar en una lista los sueldos (valores float) de 5 operarios.
#Imprimir la lista y el promedio de sueldos.
sueldos=[]
suma=0
for i in range(5):
    s = int(input(f'sueldo {i+1}: '))
    sueldos.append(s)
    suma+=s

print(sueldos)
print(f'promedio: {suma/5}')

