#Desafio: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
import time

n = randint(0, 5)
print('-=-'*20)
print('Bem vindo ao jogo de adivinhação')
print('-=-'*20)
input('>> Pressione a tecla ENTER para começar <<')
n1 = int(input('Em que número inteiro de 0 a 5 eu estou pensando?? '))
print('PROCESSANDO')
time.sleep(1)
print('.')
time.sleep(1)
print('.')
time.sleep(1)
print('.')
if n1 == n:
    print(f'Parabéns! Você acertou!')
else:
    print(f'Você errou... eu pensei no número {n} não no {n1}, tente outra vez')
