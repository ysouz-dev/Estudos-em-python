# Desafio: Faça um programa que leia um número qualquer e mostre o seu fatorial. 
# Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120


print('=====Desafio 60=====')
print('-=-' * 10)
print(' ' * 2, 'Calculadora de fatorial'.title())
print('-=-' * 10)

numero = int(input('Digite um numero inteiro: '))
n1 = numero
expoente = numero

#com while
while not expoente == 1:
    expoente -= 1
    numero *= expoente
print(f'O fatorial de {n1} é {numero}')

#com for
"""for indice in range(numero - 1, 0, -1):
    numero *= indice
print(numero)"""
