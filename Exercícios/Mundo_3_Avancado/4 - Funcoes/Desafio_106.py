# Desafio: Faça um mini-sistema que utilize o Interactive Help do Python. 
# O usuário vai digitar o comando e o manual vai aparecer. 
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.


print('=====Desafio 106=====')

def titulo(message):
    print('-' * (len(message) + 4))
    print(f'{message:^{len(message)+4}}')
    print('-' * (len(message) + 4))


def sistema_de_ajuda():
    from time import sleep
    cores = {'fundo verde': '\033[42m', 'fundo azul': '\033[44m', 'fundo branco': '\033[7;40m',
             'fundo vermelho': '\033[41m', 'limpar': '\033[m'}
    while True:
        print(f'{cores["fundo verde"]}', end='')
        titulo('SISTEMA DE AJUDA PyHELP')
        print(f'{cores["limpar"]}',end='')

        ajuda = input('Digite a Função ou Biblioteca > ')
        if ajuda.strip().lower() == 'fim':
            print(f'{cores["fundo vermelho"]}', end='')
            titulo('ATÉ LOGO!')
            sleep(1.5)
            break

        else:
            print(f'{cores["fundo azul"]}', end='')
            titulo(f'Acessando o manual do {ajuda}')
            sleep(1.5)

            print(f'{cores["fundo branco"]}')
            help(ajuda)
            print(f'{cores["limpar"]}', end='')


#programa principal
sistema_de_ajuda()
