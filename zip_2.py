from itertools import zip_longest

lista_a = [10,2,4,5]
lista_b = [12,2,3,6,50,60,70]

lista_soma = [x+y for x,y in zip_longest(lista_a, lista_b, fillvalue=0)]
'''
Neste caso, usamos o "fillvalue" como 0 (zero), assim conseguimos capturar os valores restantes da lista maior, realizando contas, sem obter um erro em nosso programa.
'''
print(lista_soma)
