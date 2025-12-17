# Desafio: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

print('=====Desafio 52=====')
print('-=-' * 14)
print(' ' * 5, 'Identificador de Números Primos')
print('-=-' * 14)
num = int(input('Digite o número inteiro que deseja identificar: '))
pontos = 0
for primos in range(1,num + 1):
    resdiv = num % primos
    if resdiv == 0:
        pontos += 1
print(f'O número que você digitou ({num}), ', end='')
if pontos > 2 or pontos == 1:
    print('não é primo.')
else:
    print('é primo.')