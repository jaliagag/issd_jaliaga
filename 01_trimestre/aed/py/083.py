#Se desea almacenar los datos de 3 alumnos. Definir un diccionario cuya clave sea el número 
#de documento del alumno. Como valor almacenar una lista con componentes de tipo tupla 
#donde almacenamos nombre de materia y su nota. 
#Crear las siguientes funciones: 

#a| Carga de los alumnos (de cada alumno solicitar su dni y los nombres de las materias y sus notas) 
# b| Listado de todos los alumnos con sus notas 
#c| Consulta de un alumno por su dni, mostrar las materias que cursa y sus notas.

alumnos = [{'DNI': 123, 'notas': [('mate', 8), ('historia', 2), ('geografia', 9)]}, 
           {'DNI': 678, 'notas': [('mate', 2)]}]

def cargar(cantidad):
    alumnos = []
    for i in range(cantidad):
        alumno = {
            'DNI': 0,
            'notas': []
        }
        id = int(input('ingrese el DNI: '))
        notas = []
        materias = 's'
        while materias == 's':
            materia = input('nombre de la materia: ')
            nota = int(input('nota: '))
            notas.append((materia,nota))
            materias = input('mas materias? [s/n]')
            print('##################')
        alumno['DNI'] = id
        alumno['notas'] = notas
        alumnos.append(alumno)
    return alumnos

#print(cargar(2))
# [{'DNI': 123, 'notas': [('mate', 8), ('historia', 2), ('geografia', 9)]}, {'DNI': 678, 'notas': [('mate', 2)]}]

def consultar(id, diccionario):
    found = 0
    for i in diccionario:
        if i['DNI'] == id:
            for h in i['notas']:
                print('\t',h[0],h[1])
            found = 1
    if found == 0:
        print('\tUser not found')
    print('##############')


continuar = 's'
while continuar == 's':
    id = int(input('DNI del alumno: '))
    consultar(id, alumnos)
    continuar = input('continuar? [s/n] ')
