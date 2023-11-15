#Crear un diccionario en Python que defina como clave el número de documento de 
#una persona y como valor un string con su nombre. Desarrollar las siguientes funciones: 

#a| Cargar por teclado los datos de 4 personas.
#b| Listado completo del diccionario. 
#c| Consulta del nombre de una persona ingresando su número de documento

def cargar(cantidad):
    personas = {}
    for i in range(cantidad):
        id = int(input('DNI: '))
        nombre = input('Nombre: ')
        personas[id] = nombre
    return personas

#print(cargar(4))

def consulta(id,diccionario):
    if id in diccionario:
        print(diccionario[id])
    else:
        print('user not found')

personas = {123: 'jose', 342: 'paula', 125: 'marce', 129: 'carla'}

seguir = 0
while seguir == 0:
    print('##############################')
    print('1 para salir, 0 para continuar')
    q1 = int(input('consultar padron? '))
    if q1 == 1:
        seguir = 1
    else:
        id = int(input('ingrese el documento: '))
        consulta(id,personas)

