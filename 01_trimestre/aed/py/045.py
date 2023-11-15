#Ingresar por teclado los nombres de 5 personas y almacenarlos en una lista. 
#Mostrar el nombre de persona menor en orden alfabético.

names = ['juan','pedro','palmiro','agustin','zulma']

menor = names[0]

for i in range(len(names)):
    if names[i] > menor:
        menor = names[i]

print(f'la última persona es {menor}')


