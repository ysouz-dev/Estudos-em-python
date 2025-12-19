# Desafio: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. 
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1 
# b) de 10 até 0, de 2 em 2 
# c) uma contagem personalizada



print('=====Desafio 98=====')

from time import sleep


def linha():
    print('-=-' * 15)


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    elif passo < 0:
        passo *= -1

    if inicio < fim:
        linha()
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        while inicio <= fim:
            print(f'{inicio} ', end='')
            sleep(0.3)
            inicio += passo
        print('Fim!')

    elif inicio > fim:
        linha()
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        while inicio >= fim:
            print(f'{inicio} ', end='')
            sleep(0.3)
            inicio -= passo
        print('Fim!')



contador(1, 10, 1)
contador(10, 0, 2)
linha()
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)