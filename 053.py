#Crear y cargar en un lista los nombres de 5 países y en otra lista paralela
#la cantidad de habitantes del mismo. Ordenar alfabéticamente e
#imprimir los resultados. Por último ordenar con respecto a la cantidad de
#habitantes (de mayor a menor) e imprimir nuevamente

paises = ['Alemania','Argentina','Francia','EEUU     ','Brasil   ']
habitantes = [85,45,93,320,280]

for i in range(len(paises)):
    print(paises[i],'\t',habitantes[i])

print('\nAlfabéticamente\n')

for i in range(len(paises)-1):
    for x in range(len(paises)-1):
        if paises[x] > paises[x+1]:
            aux = paises[x]
            paises[x] = paises[x+1]
            paises[x+1] = aux

            aux2 = habitantes[x]
            habitantes[x]=habitantes[x+1]
            habitantes[x+1]=aux2

for i in range(len(paises)):
    print(paises[i],'\t',habitantes[i])

for i in range(len(habitantes)-1):
    for x in range(len(habitantes)-1):
        if habitantes[x] > habitantes[x+1]:
            aux = habitantes[x]
            habitantes[x] = habitantes[x+1]
            habitantes[x+1] = aux

            aux2 = paises[x]
            paises[x] = paises[x+1]
            paises[x+1] = aux2

print('\npor habitantes reverso\n')

for i in range(len(paises)):
    print(paises[i],'\t',habitantes[i])

for i in range(len(habitantes)-1):
    for x in range(len(habitantes)-1):
        if habitantes[x] < habitantes[x+1]:
            aux = habitantes[x]
            habitantes[x] = habitantes[x+1]
            habitantes[x+1] = aux

            aux2 = paises[x]
            paises[x] = paises[x+1]
            paises[x+1] = aux2

print('\npor habitantes\n')

for i in range(len(paises)):
    print(paises[i],'\t',habitantes[i])
