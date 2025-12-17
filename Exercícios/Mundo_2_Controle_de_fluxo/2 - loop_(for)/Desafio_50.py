# Desafio: Desenvolva um programa que leia seis números inteiros
#  e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

print('-=-=-Desafio 50-=-=-')
from time import sleep
soma = 0
for n in range(1,7):
    numero = int(input(f'Digite o {n}° numero inteiro: '))
    if numero % 2 == 0:
        soma += numero
print(f'A soma dos valores digitados que são pares é igual a {soma}')