# Desafio: Crie um programa que leia vários números inteiros pelo teclado. 
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.


print('=====Desafio 65=====')

numero = loops = soma_para_media = quantidade_para_media = maior = menor = 0
resposta = 'SIM'

while resposta in 'SIMS':
    numero = int(input('Digite um número: '))
    soma_para_media += numero
    quantidade_para_media += 1
    if quantidade_para_media == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
    loops += 1
    if loops == 1:
        resposta = str(input('Você deseja continuar digitando os números? ')).strip().upper()
        loops = 0
print(f'A média entre todos os número que você digitou é {soma_para_media / quantidade_para_media:.2f}')
print(f'O maior número que você digitou foi o {maior} \nE o menor foi o {menor}')