# Nombre: Jose Manuel Francisco Aliaga
# DNI: 34767514


def agregar_vuelo():
    vuelo = {
        'numero_vuelo': '',
        'destino': '',
        'hora_salida': ''
    }
    vuelo['numero_vuelo'] = input('Ingrese el numero de vuelo: ')
    vuelo['destino'] = input('Ingrese el destino: ')
    vuelo['hora_salida'] = input('Ingrese la hora de salida: ')

    # creo un diccionario modelo con los valores que necesito 
    # y voy cargando la "base de datos" que es la variable 
    # externa vuelos, que es una lista de diccionarios que se va
    # actualizando

    return vuelo

def actualizar_hora_salida(una_lista):
    # ver vuelos
    # se me ocurrio llamar aca la funcion de ver vuelos
    # para saber que vuelos se pueden modificar
    #ver_vuelos(una_lista)
    found = 0
    vuelo = input('Ingrese el numero de vuelo a modificar: ')
    for i in una_lista:
        if i['numero_vuelo'] == vuelo:
            i['hora_salida'] = input('Ingrese el nuevo horario: ')
            found = 1
            print('El horario del vuelo',vuelo,'ha sido actualizado correctamente')
    if found == 0:
        print('\tEl vuelo',vuelo,'no fue encontrado')
        

def ver_vuelos(una_lista):
    print('NUMERO DE VUELO\t\tDESTINO\t\tHORA DE SALIDA')
    for i in una_lista:
        print(i['numero_vuelo'],'\t\t\t',i['destino'],'\t\t',i['hora_salida'])


# codigo principal
vuelos = []
seguir = 's'
while seguir == 's':
    seguir = input('Desea cargar un vuelo? [s/n] ')
    if seguir == 's':
        vuelos.append(agregar_vuelo())
        print('Vuelo agregado correctamente\n')

print('##########################')
actualizar_hora_salida(vuelos)
# podria poner otra estructura iterativa con un while para saber si 
# quiere modificar mas de un vuelo, pero no es requerido
print('##########################')
ver_vuelos(vuelos)
# si bien no es perfecto (cuando las ciudades tienen nombres cortos, el
# output queda raro), creo que se llega a formar una mini tabla :) 
