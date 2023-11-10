# Desarrollar un programa que solicite la carga de tres valores y muestre el menor. Desde el blo-
#que principal del programa llamar 2 veces a dicha función (sin utilizar una estructura repetitiva)
#programa principal a ambas funciones.

lista=[]

def evaluate(somelist):
    menor=somelist[0]
    for i in somelist:
        if i < menor:
            menor=i
    print(menor)

for i in range(3):
    ask=int(input('ingrese un número: '))
    lista.append(ask)

evaluate(lista)
