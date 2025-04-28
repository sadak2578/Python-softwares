# query user /server:RemoteComputerName => usar num OS

# Primeiro passo: importar o os system e o time sleep
from os import system
from time import sleep

sleep(2)
system('cls')
sleep(1)
print(r'''
   ____                            _              _   _             _   
  / ___|___  _ __ ___  _ __  _   _| |_ ___ _ __  | | | |_   _ _ __ | |_ 
 | |   / _ \| '_ ` _ \| '_ \| | | | __/ _ \ '__| | |_| | | | | '_ \| __|
 | |__| (_) | | | | | | |_) | |_| | ||  __/ |    |  _  | |_| | | | | |_ 
  \____\___/|_| |_| |_| .__/ \__,_|\__\___|_|    |_| |_|\__,_|_| |_|\__|
                      |_|                                               
''')
sleep(2)
system('cls')


def option_choice(option=''):
	while True:
		option = input('você quer procurar por mais algum computador?: [S/N]: ').strip().upper()
		if option == 's' or option == 'S':
			sleep(1)
			print('ok, continuando o código...')
			sleep(1)
		elif option == 'n' or option == 'N':
			sleep(1)
			print('ok.. saindo')
			sleep(1)
			system('cls')
			break
			exit()
		elif option != ('s','S','n','N'):
			print('caractere inválido tente novamente')
		elif option > option[0]:
			print('tanto de caracteres inválidos, favor tente novamente utilizando apenas um caractere')


def main(computer_name='', searching_computer=''):

	computer_name = input('Digite o nome do computador: ')
		
	searching_computer = system(f'query user /server:{computer_name}')
	sleep(1)
	print(searching_computer)
	sleep(1)
	option_choice(option='')


main(computer_name='',searching_computer='')