# Desafio: Faça um programa que jogue par ou ímpar com o computador. 
# O jogo só será interrompido quando o jogador perder, 
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.


print('=====Desafio 68=====')
from random import randint
from time import sleep
print('-' * 20)
print('Jogo do par ou impar'.title())
print('-' * 20)
vitorias = 0
while True:
    jogador = int(input('Digite o número que deseja jogar: '))
    print('_' * 20)
    while True:
        print('[ 1 ] Ímpar\n[ 2 ] Par')
        escolha = int(input('Qual você escolhe: '))
        print('_' * 20)
        if escolha > 2 or escolha < 1:
            print('Escolha invalida! Digite novamente.')
        else:
            print('...')
            sleep(1)
            break
    computador = randint(0,10)
    soma = computador + jogador
    print('_'*20)
    print(f'Você jogou {jogador} e o computador jogou {computador}.')
    sleep(1)
    print('_'*20)
    print(f'Total de {soma}, deu par' if soma % 2 == 0 else f'Total de soma {soma}, deu ímpar')
    sleep(1)
    print('_'*20)
    if escolha == 1 and soma % 2 == 0:
        print('Você PERDEU!')
        break
    elif escolha == 2 and soma % 2 == 0:
        print('Você GANHOU!')
        vitorias += 1
        soma = 0
        input('> Pressione ENTER para jogar novamente <')
    elif escolha == 1 and soma % 2 == 1:
        print('Você GANHOU!')
        vitorias += 1
        soma = 0
        input('> Pressione ENTER para jogar novamente <')
    elif escolha == 2 and soma % 2 == 1:
        print('Você PERDEU!')
        break
print('_'*20)
print(f'GAME OVER! Você venceu {vitorias} vezes.')