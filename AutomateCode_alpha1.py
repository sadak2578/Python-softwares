from os import system, popen, read, write
from time import sleep
from getpass import getpass
from datetime import datetime
# import csv
# colocar primeiro o título do código
sleep(1.5)
system('cls')
sleep(1.5)
print(r''' 
                                                                            
   (               )                       )          (          (          
   )\       (   ( /(         )       )  ( /(   (      )\         )\ )   (   
((((_)(    ))\  )\()) (     (     ( /(  )\()) ))\   (((_)   (   (()/(  ))\  
 )\ _ )\  /((_)(_))/  )\    )\  ' )(_))(_))/ /((_)  )\___   )\   ((_))/((_) 
 (_)_\(_)(_))( | |_  ((_) _((_)) ((_)_ | |_ (_))   ((/ __| ((_)  _| |(_))   
  / _ \  | || ||  _|/ _ \| '  \()/ _` ||  _|/ -_)   | (__ / _ \/ _` |/ -_)  
 /_/ \_\  \_,_| \__|\___/|_|_|_| \__,_| \__|\___|    \___|\___/\__,_|\___|  
                                                                            
''')

# Fazer a parte de Login do usuário administrador.
# Para isso podemos definir uma função para que o código não fique tão poluído
# como estamos definindo uma função para isso, podemos fazer uma função para colocar dentro da função administrador

# Função para fechamento de chamado
def fechamento_criacao_usuario(nome_completo_usuario='', login_usuario_ad='',senha_temporaria = '', numero_registro_usuario='' ,dia='', numero_chamado='',  texto_arquivamento='', caminho_texto='',escolha_texto=''):
	nome_completo_usuario = input('Digite o nome completo do usuário criado: ')
	login_usuario_ad = input('digite o login dele no AD: ')
	numero_chamado = input('Digite o número do chamado: ')
	numero_registro_usuario = input('Digite os dois ultimos numeros do registro do usuario: ')
	senha_temporaria = input('Digite a senha temporaria para o usuario acessar: ')
	dia = datetime.now().strftime("%d/%m/%Y")
	# Verificação de registro
	while len(numero_registro_usuario) != 2:
		print('Erro, o registro é inválido')
		numero_registro_usuario = input('Digite os dois ultimos numeros do registro do usuario: ')	
	texto_arquivamento = f'''
===================================================================
{dia}
===================================================================
usuário: {login_usuario_ad}
chamado: {numero_chamado}
senha: {senha_temporaria}@{numero_registro_usuario}
'''
	caminho_texto = r"C:\Users\conv_stefanini23\OneDrive - AngloGold Ashanti\Área de Trabalho\Criação de usuários\Chamados para criação de usuários\chamados de criação de usuário.txt"
	with open(caminho_texto,'a',encoding='utf-8') as arquivo:
		arquivo.write(texto_arquivamento)
		arquivo.write("\n")
		
	
	print(f'Texto salvo em: {caminho_texto}')

# Função para fechamento de chamado de instalação de software
def chamado_instalacao_software(nome_colaborador1='', usuario_colaborador1='', mensagem_fechamento_chamado1='',  nome_software=''):
	sleep(1)
	nome_colaborador1 = input('Digite o nome do(a) colaborador(a) aqui: ')
	sleep(1)
	usuario_colaborador1 = input('Digite o usuário(a) do(a) colaborador(a) no AD aqui: ')
	sleep(1)
	nome_software = input('Digite o nome do software aqui: ')
	sleep(1)
	mensagem_fechamento_chamado1 = f''' 
O software {nome_software} foi instalado com sucesso no computador do(a) colaborador(a) {nome_colaborador1} - {usuario_colaborador1}
'''
	sleep(1)
	print(mensagem_fechamento_chamado1)

# Função principal
def administrador_login(nome_admin='', senha_admin='', lista_admin={}, opcao_logica1='', opcao_logica2='', opcao_logica3='', opcao_logica4=''):
	lista_admin = {
	'login':'admin',
	'senha':'admin2512'
	}
	nome_admin = input('Digite o seu login: ')
	senha_admin = getpass('Digite sua senha aqui: ')
	if nome_admin == lista_admin['login'] and senha_admin == lista_admin['senha']:
		sleep(1.5)
		while True:
			print(''' 
			Escolha uma opção: 
			[1] Fechamento chamado de criação de usuário
			[2] procurar computador na rede
			[3] opções de ping
			[4] exit
			''')
			sleep(1.5)
			opcao_logica1 = input('Digite sua opcao: ')
			
			if opcao_logica1 == '1':
				sleep(1.5)
				fechamento_criacao_usuario(nome_completo_usuario='', login_usuario_ad='',senha_temporaria = '', numero_registro_usuario='' ,dia='', numero_chamado='',  texto_arquivamento='', caminho_texto='')
				sleep(1.5)
				while True:
					opcao_logica3 = input('Deseja anexar outro chamado?: [S/N] ').strip().upper()[0]
					if opcao_logica3 == 'S' or opcao_logica3 == 's':
						sleep(1)
						print('ok..')
						sleep(1)
						system('cls')
						sleep(1.5)
						fechamento_criacao_usuario(nome_completo_usuario='', login_usuario_ad='',senha_temporaria = '', numero_registro_usuario='' ,dia='', numero_chamado='', texto_arquivamento='', caminho_texto='')
					elif opcao_logica3 == 'N' or opcao_logica3 == 'n':
						sleep(1)
						print('ok.. retornando a opção anterior..')
						sleep(1)
						system('cls')
						sleep(1)
						break
						
					
			if opcao_logica1 == '4':
				opcao_logica2 = input('Tem certeza que quer sair?: [S/N] ').strip().upper()[0]
				
				if opcao_logica2 == 'S' or opcao_logica2 == 's':
					sleep(1.5)
					print('saindo...')
					sleep(1.5)
					print('volte sempre ;)...')
					sleep(1.5)
					system(exit())
				elif opcao_logica2 == 'N' or opcao_logica2 == 'n':
					print('retornando as opções...')
			elif opcao_logica1 == '2':
				chamado_instalacao_software(nome_colaborador1='', usuario_colaborador1='', mensagem_fechamento_chamado1='',  nome_software='')
				opcao_logica4 = input('Deseja terminar outro chamado de instalção de software?: [S/N] ').strip().upper()[0]
				
				if opcao_logica4 == 'S' or opcao_logica4 == 's':
					chamado_instalacao_software(nome_colaborador1='', usuario_colaborador1='', mensagem_fechamento_chamado1='',  nome_software='')
				elif opcao_logica4 == 'N' or opcao_logica4 == 'n':
					sleep(1)
					print('ok...')
					sleep(1)
					print('Retornando ao código...')
					sleep(1)
				
	else:
		print('você não é administrador, adeus')
		system(exit())


sleep(2)
print('bem vindo ao AutomateCode..')
sleep(2)
print('Antes de iniciar coloque seu login..')
sleep(1)
system('cls')

administrador_login(nome_admin='', senha_admin='', lista_admin={}, opcao_logica1='',opcao_logica2='')
