#Plantear una función que reciba un string en mayúsculas o minúsculas y retorne la cantidad de letras 'a' o 'A'

lorem = [
    "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Vitae tempora, quibusdam sed culpa at sint asperiores voluptatum et veritatis officia nihil laborum voluptatibus ab. Repellat et iste fugiat voluptates aut?",
    "Aliquam, nobis. Mollitia quos pariatur dignissimos odit, magni officiis fugit sed sequi voluptatibus ratione ex, a in nihil omnis vitae earum. Quod, tempore obcaecati id similique fuga et fugit magnam.",
    "Praesentium dignissimos soluta amet numquam mollitia voluptates perspiciatis expedita, beatae ducimus veniam quae nostrum repellat quia tempora corporis natus obcaecati facilis, non quod nemo consequuntur. At iusto voluptate dolorem totam?"
]


def aes_counter(sth):
    counter = 0
    for i in sth:
        a = i.split() # divido el string en palabras
        for k in a: # divido en letras
            for h in list(k.lower()): # evaluo cada letra
                if h == 'a':
                    counter += 1
    print(counter)

aes_counter(lorem)

