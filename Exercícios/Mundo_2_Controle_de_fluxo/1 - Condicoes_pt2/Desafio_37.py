# Desafio: Escreva um programa em Python que leia um número inteiro qualquer 
# e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

from time import sleep

cor = {'verm': '\033[1;31m', 'fim':'\033[m', 'azul':'\033[1;34m', 'roxo':'\033[1;35m', 'amarelo':'\033[1;33m', 'verde':'\033[1;32m'}

print(f'{cor['verm']}=====Desafio 37====={cor['fim']}')
print(f'{cor['azul']}Bem Vindo ao Conversor de Bases Numéricas{cor['fim']}')
num = int(input(f'{cor['amarelo']}Digite o número que você deseja converter:{cor['fim']} '))
print(f'{cor['azul']}1 - {cor['roxo']}Binário \n{cor['azul']}2 - {cor['roxo']}Octal \n{cor['azul']}3 - {cor['roxo']}Hexadecimal{cor['fim']}')
num1 = int(input(f'{cor['amarelo']}Digite o número da base a qual você deseja converter: {cor['fim']}'))
print('\033[1;34m...\033[m')
sleep(1)
if num1 == 1:
    bi = bin(num)
    print(f'{cor['verde']}O número {cor['amarelo']}{num}{cor['verde']} convertido para binário fica {cor['amarelo']}{bi}{cor['fim']}')
elif num1 == 2:
    oc = oct(num)
    print(f'{cor['verde']}O número {cor['amarelo']}{num}{cor['verde']} convertido para octal fica {cor['amarelo']}{oc}')
elif num1 == 3:
    hexa = hex(num)
    print(f'{cor['verde']}O número {cor['amarelo']}{num}{cor['verde']} convertido para hexadecimal fica {cor['amarelo']}{hexa}')
