#Cargar por teclado y almacenar en una lista las alturas de 5 personas 
#(valores float) Obtener el promedio de las mismas. Contar cuántas personas 
#sor más altas que el promedio y cuántas más bajas.

estatura=[]
suma=0
altas=0
bajas=0

for i in range(5):
    valor=float(input(f'estatura persona {i+1}: '))
    estatura.append(valor)
    suma+=valor

promedio=suma/5

for i in estatura:
    if i >= promedio:
        altas+=1
    else:
        bajas+=1

print(f'promedio: {suma/5}')
print(f'personas más altas que el promedio: {altas}')
print(f'personas más bajas que el promedio: {bajas}')
    
    



