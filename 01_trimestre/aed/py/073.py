#En una empresa se almacenaron los sueldos de 10 personas. Desarrollar las siguientes 
#funciones y llamarlas desde el bloque principal: 
    #a| Carga de los sueldos en una lista. 
    #b| Impresión de todos los sueldos. 
    #c| Cuántos tienen un sueldo superior a $4000. 
    #d| Retornar el promedio de los sueldos. 
    #e| Mostrar todos los sueldos que están por debajo del promedio.

empleados = 5

def cargar_sueldos(q_empleados):
    sueldos = []
    for i in range(q_empleados):
        sueldos.append(int(input(f'ingrese sueldo {i+1}: ')))
    return sueldos

def ver(a_imprimir):
    print(a_imprimir)

def check_sueldos(una_lista):
    mayores = 0
    for i in range(len(una_lista)):
        if una_lista[i] > 4000:
            mayores += 1
    return mayores

def promedio(una_lista,q_empleados):
    suma = 0
    for i in range(len(una_lista)):
        suma += una_lista[i]
    return suma / q_empleados

def menores(una_lista,promedio):
    menores_promedio = []
    for i in range(len(una_lista)):
        if una_lista[i] < promedio:
            menores_promedio.append(una_lista[i])
    return menores_promedio
    

la_lista = cargar_sueldos(empleados)
ver('\tsueldos:')
ver(la_lista)
ver('\tmayores a 4000:')
ver(check_sueldos(la_lista))
prome = promedio(la_lista,empleados)
ver('\tpromedio:')
ver(prome)
ver('\tmenores al promedio:')
ver(menores(la_lista,prome))







