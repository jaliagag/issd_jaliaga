#Confeccionar una función que reciba tres enteros y los muestre ordenados de menor a mayor.
#En otra función solicitar la carga de 3 enteros por teclado y proceder a llamar a la primer
#función definida

import random

def check_two(num1,num2):
    if num1 > num2:
        #print('valor',num1,'mayor')
        #return num1
        return True
    else:
        #print('valor',num2,'mayor')
        #return num2
        return False

def menor_mayor(valor1,valor2,valor3):
    lista=[0,0,0]
    unodos = check_two(valor1,valor2)
    dostres = check_two(valor2,valor3)
    unotres = check_two(valor1,valor3)
    if unodos and unotres:
        print('opción 1')
        lista[2]=valor1
        if dostres:
            lista[0]=valor3
            lista[1]=valor2
        else:
            lista[0]=valor2
            lista[1]=valor3

    if not unodos and dostres: # dos > a uno y dos > a tres
        print('opción 2')
        lista[2] = valor2
        if unotres:
            lista[0]=valor3
            lista[1]=valor1
        else:
            lista[0]=valor1
            lista[1]=valor3
    
    if not dostres and not unotres: # tres mayor a dos y tres mayor a uno
        print('opción 3')
        lista[2]=valor3
        if unodos:
            lista[1]=valor1
            lista[0]=valor2
        else:
            lista[1]=valor2
            lista[0]=valor1

    print(lista)
    
num1=random.randint(0, 100)
num2=random.randint(0, 100)
num3=random.randint(0, 100)

print(num1,num2,num3)
    
menor_mayor(num1,num2,num3)

