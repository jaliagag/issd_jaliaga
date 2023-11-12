#| Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8 empleados 
#(4 por la mañana y 4 por la tarde) Confeccionar un programa que permita almacenar 
#los sueldos de los empleados agrupados en dos listas. Imprimir las dos listas de sueldos.

morning = ['Luis','Pedro','Luisa','Petra']
night = ['Marisa','Roberto','Macarena','Juan']

s_morning=[1000,1200,1300,2000]
s_night=[1500,1600,1900,2110]

for i,g in enumerate(morning):
    print(f'el sueldo de {g} es {s_morning[i]}')
print('#############################')
for i,g in enumerate(night):
    print(f'el sueldo de {g} es {s_night[i]}')
