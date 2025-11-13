from time import sleep

print(""" 
======================================================		
	Soma do caixa no final do dia
======================================================
[ 1 ] Somatória do cartão
Digite :q para sair
""")
opcao = input('Digite sua opção: ')


def main(soma=float, numero=float):
	soma = 0.0
	while True:

	
		if opcao == '1':
			numero = input('Entre com seu número aqui: ')
			if numero == ':q':
				print(f'a soma dos numeros foi de: {soma:.2f}')
				break
			numero = float(numero)
			soma += numero
		elif opcao == ':q':
			sleep(1)
			print(f'a soma foi de {soma}')
			print('saindo do sistema...')
			break
		else:
			
			print("comando desconhecido")
			continue

main(soma=float, numero='')
