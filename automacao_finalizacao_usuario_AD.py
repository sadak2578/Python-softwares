# Automaização de fechamento de chamado para criação de usuários no AD
# Criar primeiro um usuário admin

from time import sleep
from os import system
import getpass

system('cls')

sleep(2)
print(r'''
==========================================================
 _ __   _____      __  _   _ ___  ___ _ __      
| '_ \ / _ \ \ /\ / / | | | / __|/ _ \ '__|     
| | | |  __/\ V  V /  | |_| \__ \  __/ |        
|_| |_|\___| \_/\_/    \__,_|___/\___|_|        
                                                
                                                
      _           _                         _ _ 
     | |         (_)                       | | |
  ___| | ___  ___ _ _ __   __ _    ___ __ _| | |
 / __| |/ _ \/ __| | '_ \ / _` |  / __/ _` | | |
| (__| | (_) \__ \ | | | | (_| | | (_| (_| | | |
 \___|_|\___/|___/_|_| |_|\__, |  \___\__,_|_|_|
                           __/ |                
                          |___/    
===========================================================

''')
sleep(2)
print('''
Bem vindo ao fechamento de chamados de usuários user new boarding/ user contract boarding...
''')
sleep(4)
print(''' 
digite o nome de usuário administrador e a senha para poder entrar...
''')
sleep(4)
system('cls')
sleep(1)


def admin(nome_usuário_admin='', nome_login_admin='' ,senha_admin='', lista_usuarios_admin={}, mensagem_final='', usuario_login='', nome_completo_usuário=''):
	nome_usuario_admin = input('Nome do Admin: ')
	nome_login_admin = input('Digite seu login no AD: ')
	senha_admin = getpass.getpass('Senha Admin: ')
	lista_usuarios_admin = {
	'Administrator':'Samuel Fernandes',
	'Login':'conv_stefanini23',
	'Senha':'Irlanda*12b5!z19@',
	}
	if nome_usuario_admin == lista_usuarios_admin['Administrator'] and nome_login_admin == lista_usuarios_admin['Login'] and senha_admin == lista_usuarios_admin['Senha']:
		while True:
			sleep(1)
			print('Iniciando módulo para finalização de chamado de criação de usuário...')
			sleep(1)
			system('cls')
			sleep(1)
			nome_completo_usuário = input('Digite o nome completo do usuário criado: ')
			usuario_login = input('Digite o nome de usuário que ficou no AD: ')
			
			
			
			print(f''' 
			O funcionário foi cadastrado na rede conforme solicitado.
 
			Login: {usuario_login}
			Favor orientar o {nome_completo_usuário} para ligar no HelpDesk (35892211) para a configuração do primeiro acesso.
			 
			Qualquer dúvida, coloco-me à disposição.
			Atenciosamente''')
			sleep(3)
			opcao1 = input('Deseja fazer novamente?: [S/N] ').strip().upper()[0]
			if opcao1 == 'S' or opcao1 == 's':
				continue
			else:
				sleep(1)
				print('Saindo...')
				sleep(2)
				print('volte sempre..')
				sleep(2)
				print()
				print()
				system(exit())

	else:
		print('erro')
		system(exit())

admin(nome_usuário_admin='', nome_login_admin='' ,senha_admin='', lista_usuarios_admin={}, mensagem_final='', usuario_login='', nome_completo_usuário='')
