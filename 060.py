#Crear dos listas paralelas. En la primera ingresar los nombres de empleados y en la segunda los sueldos de cada empleado.
#Ingresar por teclado cuando inicia el programa la cantidad de empleados de la empresa.
#Borrar luego todos los empleados que tienen un sueldo mayor a 10000 (tanto el sueldo como su nombre)

#empleados = ['jose','paula','mariano']
#sueldos = [9000,15000,14500]

empleados = []
sueldos = []

q_empleados = int(input('Cuántos empleados? '))
for i in range(q_empleados):
    empleado = empleados.append(input('Nombre del empleado: '))
    sueldo = sueldos.append(int(input('Sueldo del empleado: ')))

position = 0
while position < len(empleados):
    if sueldos[position] > 10000:
        empleados.pop(position)
        sueldos.pop(position)
    else:
        position += 1

print(empleados,sueldos)


