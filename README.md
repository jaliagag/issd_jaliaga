
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



