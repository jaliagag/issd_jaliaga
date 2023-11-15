a=['jose','paula','martin','marcelo','ana']
counter=0
for i in a:
    if len(i) >= 5:
        counter+=1

print(f'{counter} nombres tienen 5 o más caracteres')

