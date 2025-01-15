from os import system, popen, read, write
from time import sleep
from getpass import getpass
from datetime import datetime
import csv
# colocar primeiro o título do código
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
def fechamento_criacao_usuario(nome_completo_usuario='', login_usuario_ad='',senha_temporaria = '', numero_registro_usuario='' ,dia='', numero_chamado='', mensagem_fechamento='', texto_arquivamento='', caminho_texto=''):
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
	mensagem_fechamento = f''' 
O funcionário foi cadastrado na rede conforme solicitado.
 
Login: {login_usuario_ad} 
Favor orientar o {nome_completo_usuario} para ligar no HelpDesk (35892211) para a configuração do primeiro acesso.
 
Qualquer dúvida, coloco-me à disposição.
Atenciosamente.'''
	texto_arquivamento = f''' 
===================================================================
{dia}
===================================================================
usuário: {login_usuario_ad}
chamado: {numero_chamado}
senha: {senha_temporaria}@{numero_registro_usuario}
	'''
	caminho_texto = r"C:\Users\conv_stefanini23\OneDrive - AngloGold Ashanti\Área de Trabalho\Criação de usuários\Chamados para criação de usuários\chamados de criação de usuário.txt"
	with open(caminho_texto, 'a', encoding='utf-8') as arquivo:
		arquivo.write(texto_arquivamento + "\n")
		
	
	print(f'Texto salvo em: {caminho_texto}')
	print(mensagem_fechamento)

# Função principal
def administrador_login(nome_admin='', senha_admin='', lista_admin={}, opcao_logica1='', opcao_logica2='', opcao_logica3=''):
	lista_admin = {
	'login':'conv_stefanini23',
	'senha':'Irlanda*12b5!z19@'
	}
	nome_admin = input('Digite o seu login: ')
	senha_admin = getpass('Digite sua senha aqui: ')
	if nome_admin == lista_admin['login'] and senha_admin == lista_admin['senha']:
		sleep(1.5)
		while True:
			print(''' 
			Escolha uma opção: 
			[1] Fechamento chamado de criação de usuário
			[2] Exit	
			''')
			opcao_logica1 = input('Digite sua opcao: ')
			
			if opcao_logica1 == '1':
				fechamento_criacao_usuario(nome_completo_usuario='', login_usuario_ad='',senha_temporaria = '', numero_registro_usuario='' ,dia='', numero_chamado='', mensagem_fechamento='', texto_arquivamento='', caminho_texto='')
				opcao_logica3 = input('Deseja anexar outro chamado?: [S/N] ').strip().upper()[0]
				if opcao_logica3 == 'S' or opcao_logica3 == 's':
					sleep(1)
					print('ok..')
					sleep(1)
					fechamento_criacao_usuario(nome_completo_usuario='', login_usuario_ad='',senha_temporaria = '', numero_registro_usuario='' ,dia='', numero_chamado='', mensagem_fechamento='', texto_arquivamento='', caminho_texto='')
				elif opcao_logica3 == 'N' or opcao_logica3 == 'n':
					sleep(1)
					print('ok.. retornando a opção anterior..')
					sleep(1)
					
					
					
			elif opcao_logica1 == '2':
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
			
	else:
		print('você não é administrador, adeus')
		system(exit())

# Função para fechamento de chamado

	

sleep(2)
print('bem vindo ao AutomateCode..')
sleep(2)
print('Antes de iniciar coloque seu login..')
sleep(1)
system('cls')

administrador_login(nome_admin='', senha_admin='', lista_admin={}, opcao_logica1='',opcao_logica2='')

