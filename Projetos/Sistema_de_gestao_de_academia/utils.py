def titulo(msg):
    tam = len(msg) + 4
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)

def linha(tamanho):
    print('-' * tamanho)

def menu(academia):
    titulo(f'BEM VINDO A ACADEMIA {academia.nome.upper()}')
    print('''[ 1 ] - Cadastrar aluno
[ 2 ] - Cadastrar funcionário
[ 3 ] - Registrar equipamento
[ 4 ] - Listar alunos
[ 5 ] - Listar funcionários
[ 6 ] - Listar equipamentos
[ 7 ] - Buscar aluno por CPF
[ 8 ] - Buscar equipamento por código
[ 9 ] - Finalizar''')
    linha(34)
    while True:
        opcao = academia.validador_de_numero(int, 'Digite a opção desejada: ', 'opção')
        if 1 <= opcao <= 9:
            return opcao
        else:
            print(f'\033[1;31mError: não existe opção {opcao}, tente novamente\033[m')