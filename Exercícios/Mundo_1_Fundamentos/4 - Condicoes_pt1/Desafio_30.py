#Desafio Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

print('=====Desafio 30=====')
n = int(input('Digite um número: '))
n1 = n % 2
if n1 == 0:
    print(f'Seu número {n} é par')
else:
    print(f'Seu número {n} é ímpar')