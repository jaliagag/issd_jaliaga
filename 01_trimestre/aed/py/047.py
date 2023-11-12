# | Crear y cargar dos listas con los nombres de 5 productos 
#en una y sus respectivos precios en otra. Definir dos listas 
#paralelas. Mostrar cuántos productos tienen un precio mayor al primer producto ingresado.

productos = ['la leche','el aceite','el fiambre','el atún','la cerveza']
precios = [400,1500,300,800,700]

counter = 0
for i in range(len(productos)):
    if precios[i] > precios[0]:
        #print(f'el producto {productos[i]} es más caro que la leche')
        counter += 1

if counter == 1:
    print(f'un producto es más caro que la leche')
elif counter > 1:
    print(f'{counter} productos son más caros que {productos[0]}')

    
