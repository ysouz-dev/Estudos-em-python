from time import sleep

def cores():
    cor = ['\033[m', #limpar
'\033[1;31m', #vermelho
'\033[1;32m', #verde
'\033[1;33m', #amarelo
'\033[1;34m', #azul
'\033[1;35m'] #magenta
    return cor

def validador_de_numero(tipo, message):
    while True:
        try:
            numero = tipo(input(message))
        except ValueError:
            print(f'\033[1;31mError: você não digitou um número válido, tente novamente.\033[m')
        else:
            return numero

def validador_de_string(message, message_error=''):
    while True:
        string = str(input(message)).strip().title()
        if string.replace(' ', '').isalpha():
            return string
        else:
            print(f'\033[1;31mError: {message_error}\033[m')


def linha(quantidade):
    print('-' * quantidade)

def titulo(message):
    tam = len(message) + 4
    print('-' * tam)
    print(f'  {message}')
    print('-' * tam)

def menu_principal():
    cor = cores()
    while True:
        print(cor[4], end='')
        titulo('Barbearia YS')
        print(cor[0], end='')
        print('''[ 1 ] Cadastrar novo cliente
[ 2 ] Ver todos os cortes do mês
[ 3 ] Estatísticas
[ 4 ] Remover cliente
[ 5 ] Sair''')
        print(cor[4], end='')
        linha(20)
        print(cor[0], end='')
        opcao = validador_de_numero(int, 'Digite a opção desejada: ')
        if opcao < 1 or opcao > 5:
            print(f'\033[1;31mError: não existe opção {opcao}, tente novamente.\033[m')
            sleep(1.5)
        else:
            return opcao


