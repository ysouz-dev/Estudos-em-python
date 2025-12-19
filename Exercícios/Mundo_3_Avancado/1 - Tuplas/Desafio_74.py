# Desafio: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.


print('=====Desafio 74=====')
from random import randint
numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
em_ordem = sorted(numeros)
print(f'Os números gerados foram {numeros}')
print(f'O maior valor foi o {em_ordem[-1]}')
print(f'O menor valor foi o {em_ordem[0]}')
