
## clase 7

### listas

- agregar elementos al final mediante el método `append`: lista.append('holis').
- eliminar cualquiera de sus componentes llamando al método `pop` e indicando la posición del elemento a borrar: `lista.pop(0)`. cuando un elemento de la lista se elimina no queda una posición vacía, sino se desplazan todos los elementos de la derecha una posición. por eso, tenemos que usar una estructura iterable `while` (no `for`):

```
lista = [ 10,11,4,-1,120,56,0,30,9]

position = 0
while position < len(lista):
    if lista[position] > 9:
        lista.pop(position)
    else:
        position += 1
```

## clase 8

### programación estructurada

- programación lineal: problemas chicos, sin funciones
- programación estructurada: busca dividir o descomponer un problema complejo en pequeños problemas. La solución de cada uno de esos pequeños problemas nos trae la solución del problema complejo. el planteo de esas pequeñas soluciones al problema complejo se hace dividiendo el programa en funciones. la división en pequeñas funciones nos permitirá tener un programa más ordenado y fácil de entender y por lo tanto en mantener
- función o método: fracción de programa que cumple una misión específica. Generalmente el término Función es utilizado en la Programación Estructurada y el término Método, es utilizado en la Programación Orientada a Objetos (POO).
- parámetros para recibir datos. Los parámetros nos permiten comunicarle algo a la función y la hace más flexible. Podemos imaginar a un parámetro, como una variable que solo se puede utilizar dentro de la función y el valor se carga cuando se la llama. los parámetros son la forma para que una función reciba datos para ser procesados.
- return: devolver un dato a quien invocó la función. Después de la palabra return no se ejecuta nada.

## clase 9

### parámetros de tipo lista en funciones

 una función puede recibir tanto datos simples como estructuras de datos. Ya hemos estudiado en clases anteriores una estructura de datos: la lista. una función también puede retornar una estructura de datos tipo lista. Con esto estamos logrando que una función retorne varios datos ya que una lista es una colección de dato.

Python también nos permite descomponer los valores devueltos por la función en varias variables que reciban cada elemento de esa lista: # bloque principal del programa lista=carga_lista() mayor, menor=retornar_mayormenor(lista) print("Mayor elemento de la lista:",mayor) print("Menor elemento de la lista:",menor). Cada elemento de la lista se guarda en el mismo orden, es decir la componente 0 de la lista se guarda en la variable mayor y la componente 1 de la lista se guarda en la variable menor.

ejemplo:

```python
lista = [1,2,3,-1,-2-,3]

def comparar(lista):
    p = []
    n = []
    for i in range(len(lista)):
        if lista[i] >= 0:
            p.append(lista[i])
        else:
            n.append(lista[i])
    return p, n

positivos, negativos = comparar(lista)
```
 
- desempeños del 70 al 75

## clase 10

### tuplas vs listas

Una tupla permite almacenar una colección de datos no necesariamente del mismo tipo. | Los datos de la tupla son inmutables a diferencia de las listas que son mutables. Esto implica que una vez inicializada la tupla no podemos agregar, borrar o modificar sus elementos. elementos. La sintaxis para definir una tupla es indicar entre paréntesis sus valores

Podemos acceder a los elementos de una tupla en forma similar a una lista por medio de un subíndice: `print(punto[0])`

Utilizamos una tupla para agrupar datos que por su naturaleza están relacionados y que no serán modificados durante la ejecución del programa

la conversión de tuplas a listas y viceversa mediante las funciones: `list(parametro de tipo tupla)` `tuple(parametro de tipo lista)`

Podemos generar una tupla asignando a una variable un conjunto de variables o valores separados por coma

```py
x=10 
y=30 
punto=x,y 
print(punto)
#(10, 30)
print(type(punto))
#<class 'tuple'>
```

el desempaquetado de la tupla "fecha" se produce cuando definimos tres variables separadas por coma y le asignamos una tupla

```py
fecha=(25, "diciembre", 2016) 
print(fecha) 
dd,mm,aa=fecha
```



### for para recorrer tuplas y listas




