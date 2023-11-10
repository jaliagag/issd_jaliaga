a=input('ingrese una oración: ')
vocales=0
counter=0
while counter<len(a):
    if a[counter].lower() in ['a','e','i','o','u']:
        vocales+=1
    counter+=1

print(f'hay {vocales} vocales en esa oración')
