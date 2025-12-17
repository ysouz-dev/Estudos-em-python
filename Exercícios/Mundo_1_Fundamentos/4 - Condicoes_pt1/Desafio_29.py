# Desafio: Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.

from random import randint

vel = int(input('Qual a velocidade atual do seu carro? '))
multa = float(7)
multa1 = (vel - 80) * multa
if vel > 80:
    print(f'OPA! você estava acima da velocidade ({vel}km/h). Você foi multado em R${multa1}')
else:
    print(f'{vel}km/h... Tranquilo, boa viagem!')
