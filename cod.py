senha = 1234
usuario = 'Murilo'
for _ in range(1):
    usuariod = str(input('Digite seu nome de usuário: '))
    senhad = str(input('Digite a senha: '))
    while senhad != senha and usuariod != usuario:
        print('Acesso negado! Tente novamente...')
        usuariod = str(input('Digite seu nome de usuário: '))
        senhad = str(input('Digite a senha: '))
    else:
        print(f'Acesso concedido! Seja bem vindo Usuário {usuario}')
