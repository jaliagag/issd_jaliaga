a=input('escribi algo: ')
espacios=0
counter=0
while counter < len(a):
#for i in len(a):
    if a[counter] == " ":
        espacios+=1
    counter+=1

print(f'hay {espacios} espacios en esa oración')
