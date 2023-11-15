#Se tiene que cargar los votos obtenidos por tres candidatos a una elección.
#En una lista cargar en la primer componente el nombre del candidato y en 
#la segunda componente cargar una lista con componentes de tipo tupla con el nombre 
#de la provincia y la cantidad de votos obtenidos en dicha provincia. Se 
#deben cargar los datos por teclado, pero si se cargaran por asignación tendría 
#una estructura similar a esta: 

candidatos=[("juan", [("cordoba",100),("buenos aires",200)]), ("ana", [("cordoba",55)]), ("luis", [("buenos aires",20)])] 

#a| Función para cargar todos los candidatos, sus nombres y las provincias 
# b| Imprimir el nombre del candidato y la cantidad total de votos obtenidos en todas las provincias.

def cargar(q_cantidatos):
    candidatos = []
    for i in range(q_cantidatos):
        nombre = input('nombre del candidato: ')
        candidatos.append([nombre])
        provincia_voto = []
        provincias = int(input('en cuantas provincias tuvo voto este candidato? '))
        for h in range(provincias):
            pr = input('Nombre de la provincia: ')
            vo = int(input('Votos: '))
            inserta = pr,vo
            provincia_voto.append(inserta)
        candidatos[i].append(provincia_voto)
    return candidatos

def eval(una_lista):
    votos_totales = []
    for i in range(len(una_lista)):
        votos_totales.append([una_lista[i][0]])
        votos = 0
        for k in range(len(una_lista[i][1])):
            votos += una_lista[i][1][k][1]
        votos_totales[i].append(votos)

    return votos_totales


#print(cargar(2))
print(eval(candidatos))