#Desarrollar una aplicación que permita ingresar por teclado los nombres de 5 artículos y sus 
#precios. Definir las siguientes funciones: 
#a| Cargar los nombres de artículos y sus precios. 
#b| Imprimir los nombres y precios. 
#c| Imprimir el nombre de artículo con un precio mayor 
#d| Ingresar por teclado un importe y luego mostrar todos los artículos con un precio menor igual al valor ingresado.

q = 5

def cargar(cantidad):
    articulos = ['papa','cebolla','tomate','manzana','repollo']
    precios = [1500,1300,2500,1350,750]
    #articulos = []
    #precios = []
    #for i in range(cantidad):
    #    articulos.append(input('nombre del articulo: '))
    #    precios.append(int(input(f'precio del articulo {articulos[i]}: ')))
    return articulos, precios

def paralallel_print(lista1,lista2):
    for i in range(len(lista1)):
        print(lista1[i],'|',lista2[i])

def menor_y_mayor(lista1):
    position = [[lista1[0],0],[lista1[0],0]]
    for i in range(len(lista1)):
        if lista1[i] < position[0][0]:
            position[0][0] = lista1[i]
            position[0][1] = i
        elif lista1[i] > position[1][0]:
            position[1][0] = lista1[i]
            position[1][1] = i
    return position


def ver(message):
    print(message)

def compara(importe,precios):
    menores = []
    for i in range(len(precios)):
        if precios[i] < importe:
            menores.append(i)
    return menores


articulos, precios = cargar(q)
paralallel_print(articulos,precios)
menorprecio = menor_y_mayor(precios)
print(menorprecio)
print('menor: ', articulos[menorprecio[0][1]],menorprecio[0][0],'\n','mayor', articulos[menorprecio[1][1]], menorprecio[1][0])
articulos_menores = int(input('precios menores a: '))
index_menores = compara(articulos_menores,precios)
for i in range(len(index_menores)):
    print(articulos[i],precios[i])


