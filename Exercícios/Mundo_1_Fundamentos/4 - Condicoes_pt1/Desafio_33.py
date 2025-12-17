#Desafio: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

print('=====Desafio 33=====')
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

#verificando maior
if n1 > n2 and n1 > n3:
    print(f'O maior número é o {n1}')
if n2 > n1 and n2 > n3:
    print(f'O maior número é o {n2}')
if n3 > n1 and n3 > n2:
    print(f'O maior número é o {n3}')

#verificando menor
if n1 < n2 and n1 < n3:
    print(f'O menor número é o {n1}')
if n2 < n1 and n2 < n3:
    print(f'O menor número é o {n2}')
if n3 < n1 and n3 < n2:
    print(f'O menor número é o {n3}')
    