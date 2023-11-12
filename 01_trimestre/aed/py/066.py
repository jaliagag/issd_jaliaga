#• Elaborar una función que reciba tres enteros y nos retorne el valor promedio de los mismos

import random

def promedio(valor1,valor2,valor3):
    prom = (valor1+valor2+valor3)/3
    return int(prom)

num1 = random.randint(0, 90)
num2 = random.randint(0, 90)
num3 = random.randint(0, 90)
print(num1,num2,num3)

print(promedio(num1,num2,num3))


