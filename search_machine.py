from time import sleep
from os import system
# objetivo: rodar o comando query user /server:RemoteComputerName 

sleep(1)
print(r"""
  _________                           .__         _____                .__    .__               
 /   _____/ ____ _____ _______   ____ |  |__     /     \ _____    ____ |  |__ |__| ____   ____  
 \_____  \_/ __ \\__  \\_  __ \_/ ___\|  |  \   /  \ /  \\__  \ _/ ___\|  |  \|  |/    \_/ __ \ 
 /        \  ___/ / __ \|  | \/\  \___|   Y  \ /    Y    \/ __ \\  \___|   Y  \  |   |  \  ___/ 
/_______  /\___  >____  /__|    \___  >___|  / \____|__  (____  /\___  >___|  /__|___|  /\___  >
        \/     \/     \/            \/     \/          \/     \/     \/     \/        \/     \/ 
"""
)
sleep(4)
system('cls')
sleep(1)
print('bem vindo...')
def procura_maquina(nome_máquina='', query_user=''):
	sleep(1)
	print()
	nome_máquina = input('informe o nome da máquina: ')
	sleep(1)
	print('o retorno da máquina foi...')
	sleep(1)
	print()
	query_user = system(f'query user /server:{nome_máquina}')
	sleep(1)
while True:
	procura_maquina(nome_máquina='', query_user='')
	while True:
		print()
		opcao = input('você gostaria de continuar a procurar outras máquinas? [S/N] ').strip().upper()[0]
		if opcao == 's' or opcao == 'S':
			procura_maquina(nome_máquina='', query_user='')
		elif opcao == 'n' or opcao == 'N':
			sleep(1)
			print('ok.. saindo')
			sleep(1)
			system('cls')
			sleep(1)
			exit()
		else:
			sleep(1)
			print('erro de sintaxe use somente s ou n')