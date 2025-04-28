from time import sleep
from os import system

def main(username='', user_in_ad=''):
	while True:
	
		sleep(1)
		system('cls')
		sleep(1)
		username = input('Nome completo da pessoa: ')
		sleep(1)
		user_in_ad = input('Coloque o nome do usuário AD aqui: ')
		sleep(1)
		admin = 'Samuel Fernandes - conv_stefanini23'
		sleep(1)
		print(f'''


O funcionário foi cadastrado na rede conforme solicitado.
		 
Login: {user_in_ad} 
Favor orientar o {username.title()} para ligar no HelpDesk (31 3589-2211) para a configuração do primeiro acesso.
		 
Qualquer dúvida, coloco-me à disposição.
Atenciosamente.
{admin}
		''')
		sleep(1)
		if escolha(opcao='') != ('S','s') or escolha(opcao='') != ('N','n'):
			sleep(2)
			print('caractere inválido, favor tente novamente')
			sleep(2)
		escolha(opcao='')
def escolha(opcao=''):
	opcao = input('gostaria de adicionar mais usuários?: [S/N] ').strip().upper()[0]
	sleep(1)
	if opcao == 'S' or opcao == 's':
		sleep(1)
		print('ok...')
		sleep(1)
		print('continuando código...')
		sleep(1)
		system('cls')
		main(username='',user_in_ad='')
		
	elif opcao == 'N' or opcao == 'n':
		sleep(1)
		print('ok')
		sleep(1)
		print('saindo do código')
		sleep(1)
		system('cls')
		sleep(1)
		exit()
	 

main(username='', user_in_ad='')