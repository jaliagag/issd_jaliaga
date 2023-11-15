#Almacenar en una lista de 5 elementos los nombres de empleados de una empresa 
#junto a sus últimos tres sueldos (estos tres valores en una tupla) El programa 
#debe tener las siguientes funciones: 
#a| Cargar una lista de 10 elementos enteros. 
#b| Imprimir el monto total cobrado por cada empleado. 
#c| Imprimir los nombres de empleados que tuvieron un ingreso trimestral mayor a 10000 en los últimos tres meses

lista = [
    ['silvina',(120,130,140)],['mauro',(800,300,200)],['sofia',(1340,3500,5500)],['paula',(10500,550,600)],['demichelis',(900,900,1200)]
    ]

def cargar(cantidad):
    una_lista =[]
    for i in range(cantidad):
        una_lista.append(int(input('ingrese un numero entero: ')))
    return una_lista

def monto_total(una_lista):
    montos = []
    for i in range(len(una_lista)):
        suma = 0
        for h in una_lista[i][1]:
            suma += h
        print('empleado: ',una_lista[i][0],'sueldo total: ',suma)
        montos.append(suma)

    return montos
    
def ingresos_mayores(lista_completa, ingresos_totales):
    nombres = []
    for i in range(len(ingresos_totales)):
        if ingresos_totales[i] > 10000:
            nombres.append(lista_completa[i][0])
    return nombres

#cargar(10)
montos = monto_total(lista)
print(ingresos_mayores(lista,montos))



