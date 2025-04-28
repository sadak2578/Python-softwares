# Aula de Python ==== count, contador infinito
# obs: count está no método itertools
from itertools import count

c1 = count(0)

print('c1', hasattr(c1, '__iter__'))


# for i in c1:
	# print(i)
