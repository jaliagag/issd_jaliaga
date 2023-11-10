lista=[[1], [1,2], [1,2,3], [1,2,3,4], [1,2,3,4,5]] 
suma=0 
for k in range(len(lista)): 
    for x in range(len(lista[k])): 
        suma=suma+lista[k][x] 
print(suma)
