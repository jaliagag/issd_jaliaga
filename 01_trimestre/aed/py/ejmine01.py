def somthing(rang):
    nombres = []
    edades = []
    for i in range(rang):
        nombres.append(input('nombre: '))
        edades.append(int(input('edad: ')))
    return [nombres,edades]

names,ages = somthing(2)
print(names)
print(ages)
