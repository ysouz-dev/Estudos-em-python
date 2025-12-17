# Desafio: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, 
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.

print('=====Desafio 46=====')

from time import sleep
from emoji import emojize

for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(f'FELIZ ANO NOVO!! {emojize(':fogos_de_artifício:', language='pt')}')
