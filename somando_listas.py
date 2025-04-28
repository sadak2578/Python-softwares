'''
Considerando duas listas de inteiros e floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com valores somados:

se uma lista for maior que a outra, a soma só vai considerar o tamanho da menor

exemplo:
lista_a = [1,2,3,4,5,6,7]
lista_b = [1,2,3,4]
'''
lista_a = [1,2,3,4,5,6,7]
lista_b = [1,2,3,4]

lista_soma = []

for i in range(len(lista_b)):
	lista_soma.append(lista_a[i] + lista_b[i])
print(lista_soma)
