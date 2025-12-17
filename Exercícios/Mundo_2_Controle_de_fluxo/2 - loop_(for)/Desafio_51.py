# Desafio: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
# No final, mostre os 10 primeiros termos dessa progressão.

print('=====Desafio 51=====')
termo = int(input('Digite o primeiro termo da sua PA: '))
termo1 = termo
razao = int(input('Digite a razão: '))
print(termo, end=' ')
for pa in range(1,10):
    termo1 = termo1 + razao
    print(termo1, end=' ')
print(f'esses são os 10 primeiros termos de uma PA com primeiro termo {termo} e razão {razao}.')