# Exercício - unir listas
# Crie uma função zipper (como de zipper de roupas)
# o trabalho desta função será unir duas listas
# listas na ordem
# Use todos os valores da menor listas
# Ex.: 
# ['Salvador', 'Ubatuba','Belo Horizonte']
# ['BA','SP','MG','RJ']
# Resultado: 
# [('Salvador','BA'), ('Ubatuba','SP'), ('Belo Horizonte','MG')]

# def zipper(lista1, lista2):
	# intervalo = min(len(lista1), len(lista2))
	# return [
		# (lista1[i], lista2[i]) for i in range(intervalo)
	# ]
	

l1 =  ['Salvador', 'Ubatuba','Belo Horizonte']
l2 = ['BA','SP','MG','RJ']
print(list(zip(l1, l2)))