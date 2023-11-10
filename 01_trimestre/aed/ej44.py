#Se tiene que cargar la siguiente información: 
#    | Nombres de 3 empleados 
#    | Ingresos en concepto de sueldo, cobrado por cada empleado, en los últimos 3 meses. 
#Confeccionar el programa para: 
#    a| Realizar la carga de los nombres de empleados y los tres sueldos por cada empleado. 
#    b| Generar una lista que contenga el ingreso acumulado en sueldos en los últimos 3 meses para cada empleado. 
#    c| Mostrar por pantalla el total pagado en sueldos a cada empleado en los últimos 3 meses 
#    d| Obtener el nombre del empleado que tuvo el mayor ingreso acumulado

#empleados = []
#sueldos = []
#
#for i in range(3):
#    empleado = input('Nombre del empleado: ')
#    empleados.append(empleado)
#    s = []
#    for k in range(3):
#        sueldo = int(input(f'sueldo {k+1}: '))
#        s.append(sueldo)
#    sueldos.append(s)


empleados = ['Jose','Paula','Marce']
sueldos = [ [ 300, 350, 250], [2300,2900,3250], [800,700,1100] ]
ingreso_acumulado = []

for i in range(len(sueldos)):
    ingreso = 0
    for k in range(len(sueldos[i])):
        ingreso += sueldos[i][k]
    ingreso_acumulado.append(ingreso)

for i in range(len(empleados)):
    print(empleados[i],'\t',ingreso_acumulado[i])

mayor = ["",0]

for i in range(len(empleados)):
    if ingreso_acumulado[i] > mayor[1]:
        mayor[0] = empleados[i]
        mayor[1] = ingreso_acumulado[i]
        
print(f'{mayor[0]} tuvo el mayor sueldo en los últimos 3 meses con un total de {mayor[1]} USD')



