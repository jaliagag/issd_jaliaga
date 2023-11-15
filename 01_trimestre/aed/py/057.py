#Se desea saber la temperatura media trimestral de cuatro paises. 
#Para ello se tiene como dato las temperaturas medias mensuales de dichos paises.
#Se debe ingresar el nombre del país y seguidamente las tres temperaturas medias mensuales. 
#Seleccionar las estructuras de datos adecuadas para el almacenamiento de los datos en memoria. 
#a| Cargar por teclado los nombres de los paises y las temperaturas medias mensuales. 
#b| Imprimir los nombres de las paises y las temperaturas medias mensuales de las mismas. 
#c| Calcular la temperatura media trimestral de cada país. 
#d| Imprimir los nombres de los paises y las temperaturas medias trimestrales.
#e| Imprimir el nombre del pais con la temperatura media trimestral mayor.

#paises = ['Argentina','España','Chile','Iran']
#temp_medias_anuales = [33,29,25,30]
paises = []
temp_medias_anuales = []
mayor = ['',0]

def temp_media(temp,medida):
    return temp/medida

q1 = int(input('Cantidad de paises a analizar: '))

for i in range(q1):
    paises.append(input(f'- Nombre del país {i+1}: '))
    temp_medias_anuales.append(int(input(f'\t- Temperatura media anual del país {paises[i]}: ')))

print()
print('b --> paises y temp medias mensuales')
print()

for i in range(len(paises)):
    print(paises[i],'\t-->',temp_media(temp_medias_anuales[i],12))
    #print(paises[i],'\t-->',temp_medias_anuales[i])

print()
print('d --> paises y tem medias trimestrales')
print()

for i in range(len(temp_medias_anuales)):
    calc = temp_media(temp_medias_anuales[i],4)
    if calc > mayor[1]:
        mayor[0] = paises[i]
        mayor[1] = calc
    print(paises[i],'\t-->',calc)

#e| Imprimir el nombre del pais con la temperatura media trimestral mayor.
print()
print(f'e| mayor temp trimestral: {mayor[0]} --> {mayor[1]}')
