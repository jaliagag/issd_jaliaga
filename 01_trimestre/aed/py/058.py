# Definir una lista y almacenar los nombres de 3 empleados. 
# | Por otro lado definir otra lista y almacenar en cada elemento una sublista 
# con los números de días del mes que el empleado faltó. Imprimir los nombres de 
# empleados y los días que faltó. Mostrar los empleados con la cantidad de inasistencias. 
# Finalmente mostrar el nombre o los nombres de empleados que faltaron menos días.

empleados = ['jose','paula','mariano']
faltas = [ [12,25], [3,28,29], [] ]
menores = ['',0]

for i in range(len(empleados)):
    dia = 'días'
    if len(faltas[i]) == 1:
        dia = 'día'
        print(f'{empleados[i]} faltó {len(faltas[i])} {dia}')
    elif len(faltas[i]) == 0:
        print(f'{empleados[i]} no faltó ningún día')
    else:
        print(f'{empleados[i]} faltó {len(faltas[i])} {dia}')

    if len(faltas[i]) <= menores[1]:
        menores[0] = empleados[i]
        menores[1] = len(faltas[i])
print(f'empleados que menos faltaron: {menores[0]} con {menores[1]} faltas')


