counter=0
intentos=0

while counter == 0:
    if intentos != 0:
        print('error - entre 10 y 20, loco')
    a=input('ingrese una oración de entre 10 y 20 caracteres: ')
    intentos+=1
    if len(a)>10 and len(a)<20:
        counter+=1

print('clave válida')
