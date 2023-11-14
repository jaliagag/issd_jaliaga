#Confeccionar un programa con las siguientes funciones: 
#a| Cargar el nombre de un empleado y su sueldo. Retornar una tupla con dichos valores. 
#b| Una función que reciba como parámetro dos tuplas con los nombres y sueldos 
#   de empleados y muestre el nombre del empleado con sueldo mayor. En el bloque 
#   principal del programa llamar dos veces a la función de carga y seguidamente llamar a la 
#   función que muestra el nombre de empleado con sueldo mayor. 

def cargar_empleado():
    empleado = []
    empleado.append(input('nombre del empleado: '))
    empleado.append(int(input('sueldo del empleado: ')))
    return empleado

def mayor_sueldo(tuple1,tuple2):
    mayor = ''
    if tuple1[1] > tuple2[1]:
        mayor = tuple1[0]
    else:
        mayor = tuple2[0]
    return mayor


# bloque principal 
empleado1=cargar_empleado() 
empleado2=cargar_empleado() 
print('mayor sueldo:',mayor_sueldo(empleado1,empleado2))
