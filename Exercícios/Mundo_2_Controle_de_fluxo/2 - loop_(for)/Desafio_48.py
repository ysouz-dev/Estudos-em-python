# Desafio: Faça um programa que calcule a soma entre todos os números que são múltiplos de três 
# e que se encontram no intervalo de 1 até 500.

print('=====Desafio 48=====')
final = 0
for impar in range(1, 501, 2):
    if impar % 3 == 0:
        final += impar
print(f'a soma de todos os números impares multiplos de 3 da {final}')