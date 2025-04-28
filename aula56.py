from time import sleep
def parametros_decorador(nome):
	def decorador(func):
		sleep(1)
		print(f"Decorador: {nome}")
		def sua_nova_funcao(*args, **kwargs):
			res = func(*args, **kwargs)
			final = f'{res} {nome}'
			return final
		return sua_nova_funcao
	return decorador


@parametros_decorador(nome='5')
@parametros_decorador(nome='4')
@parametros_decorador(nome='3')
@parametros_decorador(nome='2')
@parametros_decorador(nome='1')

def soma(x,y):
	return x + y
	
somar = soma(10,5)
sleep(1)
print(somar)
sleep(1)