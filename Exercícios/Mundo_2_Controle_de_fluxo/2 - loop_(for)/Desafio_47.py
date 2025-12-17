# Desafio: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

print('=====Desafio 47=====')
for par in range(1,51):
    if par % 2 == 0:
        print(par, end=" ")
print('Esses são os números pares de 1 a 50')
