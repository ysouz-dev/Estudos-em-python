#Desafio:Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
#Calcule e mostre o comprimento da hipotenusa.

print('=====Desafio 17=====')
from math import sqrt
co = float(input('Qual o valor do cateto oposto: '))
ca = float(input('Qual o valor do cateto adjacente: '))
h = sqrt((ca**2 + co**2))
print('Tendo o cateto oposto {}cm e o adjacente {}cm, a hipotenusa mede {:.2f}cm'.format(co, ca, h))
