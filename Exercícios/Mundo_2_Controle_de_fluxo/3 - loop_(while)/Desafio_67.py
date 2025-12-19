# Desafio: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
# O programa será interrompido quando o número solicitado for negativo.

print('=====Desafio 67=====')
while True:
    print('=' * 20)
    numero = int(input('Digite o valor que deseja ver a tabuada: '))
    print('=' * 20)
    if numero < 0:
        print('Tabuada encerrada. \nMuito obrigado! Volte sempre.')
        break
    for tabuada in range(1,11):
        print(f'{numero} x {tabuada:2} = {numero * tabuada}')
