#• Desarrollar un programa con dos funciones.
#La primera solicite el ingreso de un entero y muestre el cuadrado de dicho valor. La segunda que
#solicite la carga de dos valores y muestre el producto de los mismos. Llamar desde el bloque del
#programa principal a ambas funciones.
#
def cuadrado():
    valor1=int(input('ingrese un número: '))
    c=valor1*valor1
    print('el cuadrado de',valor1,'es',c)

def mult():
    valor1=int(input('ingrese un número: '))
    valor2=int(input('ingrese otro número: '))
    print('resultado',valor1*valor2)

cuadrado()
mult()

