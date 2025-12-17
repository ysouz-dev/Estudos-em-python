# Desafio: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

print('=====Desafio 55=====')
kgmaior = 0
kgmenor = 0
for peso in range(1,6):
    kg = float(input(f'Qual o peso(kg) da {peso}° pessoa: '))
    if peso == 1:
        kgmaior = kg
        kgmenor = kg

    if kg > kgmaior:
        kgmaior = kg
    elif kg < kgmenor:
        kgmenor = kg

print(f'A pessoa de maior peso tem {kgmaior}kg \nE a de menor peso tem {kgmenor}kg')