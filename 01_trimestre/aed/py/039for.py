lista=[190,231,23,42,532,453,76,75]
cienmas=[]
mayores=0
for i in range(len(lista)):
#while c < len(lista):
    if lista[i] > 100:
        mayores+=1
#    c+=1
print(f'hay {mayores} números mayores a 100')

