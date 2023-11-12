#Desarrollar un programa que cree una lista de 50 elementos. 
#El primer elemento es una lista con un elemento entero, el segundo elemento es 
#una lista de dos elementos etc. | La lista debería tener la siguiente estructura 
#y asignarle esos valores a medida que se crean los elementos: 
#    [[1], [1,2], [1,2,3], [1,2,3,4], [1,2,3,4,5], etc....]

lista = []

for i in range(50):
    lista2 = []
    for k in range(i+1):
        lista2.append(k+1)
    lista.append(lista2)
print(lista)
