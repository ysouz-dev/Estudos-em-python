# Desafio: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

print('\033[1;31m=====Desafio 38=====\033[m')
n = int(input('Digite um número: '))
n1 = int(input('Digite outro número: '))
if n > n1:
    print('O primeiro valor é maior')
elif n1 > n:
    print('O segundo valor é maior')
elif n == n1:
    print('Não existe valor maior, os dois são iguais')
