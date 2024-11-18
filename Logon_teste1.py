import getpass
usuario = {'Nome': '','Senha': ''}

def criando_usuario():
    nome = input('crie um usuário: ')
    senha = getpass.getpass('crie uma senha: ')
    usuario['Nome'] = nome
    usuario['Senha'] = senha
    return  usuario

# neste Try e Except vamos validar o usuário

usuario_criado = criando_usuario()



def validando_usuario():
    try:
        nome = input('Digite o nome de usuário: ')
        senha = getpass.getpass('Digite a senha: ')

        if nome == usuario['Nome'] and senha == usuario['Senha']:
            print('usuário criado')
            return True
        else:
            print('usuario e senha incorreto')
            return False
    except ValueError as e:
        print(f'erro em: {e}')
        return False
        
usuario_validado = validando_usuario()


while True:
    
    if usuario_validado:
        print('Bem vindo ao sistem :)')
        break
    else:
        print('erro :(')
        break
        
        