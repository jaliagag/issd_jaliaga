lista=[190,231,23,42,532,453,76,75]
cienmas=[]
mayores=0
c=0
while c < len(lista):
    if lista[c] > 100:
        mayores+=1
    c+=1
print(f'hay {mayores} números mayores a 100')

