# Desafio: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.


print('=====Desafio 88=====')

from random import randint
from time import sleep

jogos_sorteados = []

print('-=-' * 10)
print(f'{"Jogo da Mega Sena":^30}')
print('-=-' * 10)

jogos = int(input('Quantos jogos você quer que eu sorteie? '))

for listas in range(0, jogos):
    jogos_sorteados.append([])

    while not len(jogos_sorteados[listas]) == 6:
        aleatorio = randint(1, 60)

        if aleatorio not in jogos_sorteados[listas]:
                jogos_sorteados[listas].append(aleatorio)

print(f'{f" SORTEANDO {jogos} JOGOS ":=^40}')
for i in range(0, jogos):
    print(f'Jogo {i + 1}: {sorted(jogos_sorteados[i])}')
    sleep(1)
print(f'{"> Boa Sorte! <":=^40}')
