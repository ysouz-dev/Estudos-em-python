#Desafio: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

print('=====Desafio 18=====')
from math import radians, sin, tan, cos
an = float(input('Digite o valor do angulo: '))
sen = sin(radians(an))
coss = cos(radians(an))
tang = tan(radians(an))
print('O angulo de {}° tem o \nseno {:.2f} \ncosseno {:.2f} \ntangente {:.2f}'.format(an, sen, coss, tang))
