# Desafio: Crie um programa que simule o funcionamento de um caixa eletrônico. 
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
# e o programa vai informar quantas cédulas de cada valor serão entregues. 
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1


print('Desafio 71')
from time import sleep
print('-=-'*10)
print(f'''{' ':^10}SIMULADOR 
{' ':^13}DE 
{' ':^7}CAIXA ELETRONICO''')
print('-=-'*10)
cedula_de_1 = cedula_de_10 = cedula_de_20 = cedula_de_50 = 0
while True:
    while True:
        valor_sacado = int(input('Qual valor você deseja sacar: '))
        if valor_sacado < 0:
            print('Quantia inválida! Digite um valor correto.')
        else:
            break

    divisao_por_50 = valor_sacado // 50
    #print(divisao_por_50, 'div por 50')
    cedula_de_50 += divisao_por_50
    valor_sacado -= divisao_por_50 * 50
    #print(valor_sacado, 'valor sacado')

    divisao_por_20 = valor_sacado // 20
    #print(divisao_por_20, 'div por 20')
    cedula_de_20 += divisao_por_20
    valor_sacado -= divisao_por_20 * 20
    #print(valor_sacado, 'valor sacado')

    divisao_por_10 = valor_sacado // 10
    #print(divisao_por_10, 'div por 10')
    cedula_de_10 += divisao_por_10
    valor_sacado -= divisao_por_10 * 10
    #print(valor_sacado, 'valor sacado') 

    divisao_por_1 = valor_sacado // 1
    cedula_de_1 += divisao_por_1
    valor_sacado -= divisao_por_1 * 1

    print('-=-'*10)
    print('Processando')
    sleep(1)
    print('.')
    sleep(1)
    print('.')
    sleep(1)
    print('.')
    sleep(1)

    print('-=-'*10)
    print(f'Total de {cedula_de_50} cédulas de R$ 50' if cedula_de_50 > 0 else '')
    print(f'Total de {cedula_de_20} cédulas de R$ 20' if cedula_de_20 > 0 else '')
    print(f'Total de {cedula_de_10} cédulas de R$ 10' if cedula_de_10 > 0 else '')
    print(f'Total de {cedula_de_1} cédulas de R$ 1' if cedula_de_1 > 0 else '')
    print('-=-'*10)
    
    while True:
        pergunta = str(input('Deseja realizar um novo saque? ')).strip().upper()
        if pergunta in ['SIM', 'S', 'N', 'NAO', 'NÃO']:
            break
        else:
            print('Resposta inválida! Tente novamente.')
    if pergunta in ['N', 'NAO', 'NÃO']:
        print('-=-'*10)
        print('Caixa eletrônico encerrado.')
        break
    else:
        cedula_de_1 = cedula_de_10 = cedula_de_20 = cedula_de_50 = 0
