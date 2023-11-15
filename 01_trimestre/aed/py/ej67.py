def cargar(): 
    empleados=[] 
    for x in range(5): 
        nombre=input("Nombre del empleado:") 
        sueldo=int(input("Ingrese el sueldo:")) 
        empleados.append((nombre,sueldo)) 
    return empleados

def imprimir(empleados): 
    print("Listado de los nombres de empleados y sus sueldos") 
    for nombre,sueldo in empleados: 
        print(nombre,sueldo)

lista = cargar()
imprimir(lista)