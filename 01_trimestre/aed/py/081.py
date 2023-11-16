#| Almacenar los nombres de 5 productos y sus precios. Utilizar una lista y cada
#elemento una tupla con el nombre y el precio. Desarrollar las funciones: 

#a| Cargar por teclado. 
#b| Listar los productos y precios. 
#c| Imprimir los productos con precios comprendidos entre 10 y 15

productos = [ ('manzana', 15), ('pera', 10), ('banana', 11), ('tomate', 55), ('papa', 12) ]

def cargar(cantidad):
    productos = []
    for i in range(cantidad):
        producto = input('nombre del producto: ')
        costo = int(input('precio: '))
        productos.append((producto,costo))
        #productos.append([producto,costo])
    return productos

def imprimir(una_lista):
    for fruta,precio in una_lista:
        if precio >= 10 and precio <= 15:
            print(fruta)

imprimir(cargar(2))
