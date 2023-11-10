#En un curso de 4 alumnos se registraron las notas de sus exámenes y se deben procesar 
#de acuerdo a lo siguiente: 
#    a| Ingresar nombre y nota de cada alumno (almacenar los datos en dos listas paralelas) 
#    b| Realizar un listado que muestre los nombres, notas y condición del alumno. 
#        En la condición, colocar "Muy Bueno" si la nota es mayor o igual a 8, "Bueno" si 
#        la nota está entre 4 y 7, y colocar "Insuficiente" si la nota es inferior a 4. 
#    c| Imprimir cuantos alumnos tienen la leyenda “Muy Bueno”.

alumnos = ['jose','mariano','guillermo','walter','martin']
notas = [2,4,6,8,3]
condicion = []
counter = 0

for i in range(len(alumnos)):
    if notas[i] < 4:
        condicion.append([alumnos[i],notas[i],'Insuficiente'])
    elif notas[i] > 4 and notas[i] < 7:
        condicion.append([alumnos[i],notas[i],'Bueno'])
    else:
        condicion.append([alumnos[i],notas[i],'Muy Bueno'])

for i in condicion:
    if i[2] == 'Muy Bueno':
        counter += 1

if counter > 1:
    print(f'{counter} alumnos tienen la leyenda "Muy Bueno"')
else:
    print(f'{counter} alumno tiene la leyenda "Muy Bueno"')



