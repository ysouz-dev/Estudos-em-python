#Desafio: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import floor
print('=====Desafio 16=====')
nr = float(input('Digite um número real: '))
print('O número {} tem a parte inteira {}'.format(nr, floor(nr)))
