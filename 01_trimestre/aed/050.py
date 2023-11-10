#| Crear una lista y almacenar los nombres de 5 países.
#Ordenar alfabéticamente la lista e imprimirla

paises = ['Bolivia','Uruguay','Paraguay','Argentina','Brasil'] # len5
paises = ['Wellington','Estados Unidos','España','Alemania','Francia'] # len5

for k in range(len(paises)-1):
    for x in range(len(paises)-k-1):
        if paises[x] > paises[x+1]:
            aux=paises[x]
            paises[x]=paises[x+1]
            paises[x+1]=aux
    
print(paises)
