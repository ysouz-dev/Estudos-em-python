# Desafio:  Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

print('=====Desafio 54=====')

from datetime import date

maior = 0
menor = 0
for anos in range(1,8):
    pessoas = int(input(f'Qual ano de nascimento do {anos}°: '))
    ano = date.today().year
    idade = ano - pessoas
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f"""{maior} pessoas atingiram a maior idade
{menor} pessoas não atingiram a maior idade""")
