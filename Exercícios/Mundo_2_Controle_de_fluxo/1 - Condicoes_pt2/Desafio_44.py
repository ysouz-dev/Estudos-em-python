#Desafio: Elabore um programa que calcule o valor a ser pago por um produto, 
# considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal 
# – 3x ou mais no cartão: 20% de juros

from time import sleep

print('\033[1;31m=====Desafio 44=====\033[m')
print('\033[4;35mGerenciador de Pagamentos\033[m')
produto = float(input('Qual o preço do produto: R$ '))
print('...')
sleep(1)
while True:
    print('1 - A vista no dinheiro: 10% de desconto \n2 - A vista no cartão: 5% de desconto \n3 - Até 2x no cartão: preço normal \n4 - 3x ou mais no cartão: 20% de juros')
    escolha = int(input('Digite o número da forma que deseja pagar: '))
    if escolha > 4 or escolha < 1:
        print('...')
        sleep(0.5)
        print('\033[1;31mOpção invalida! digite uma forma de pagamento valida.\033[m')
    else:
        break
if escolha == 1:
    print('...')
    sleep(1)
    desconto10 = produto - (10 / 100) * produto
    print(f'Para pagamento a vista no dinheiro, seu produto tem 10% de desconto, ficando assim R${desconto10:.2f}')
elif escolha == 2:
    print('...')
    sleep(1)
    desconto5 = produto - (5 / 100) * produto
    print(f'Para pagamento a vista no cartão, seu produto tem 5% de desconto, ficando assim R${desconto5:.2f}')
elif escolha == 3:
    print('...')
    sleep(1)
    x2 = produto / 2
    print(f'Para pagamento em ate 2x no cartao, seu produto sai no preço normal, ficando assim R${produto:.2f} / 2x de R${x2:.2f}')
elif escolha == 4:
    print('...')
    sleep(1)
    while True:
        xvezes = int(input('Deseja fazer em quantas vezes? '))
        juros20 = (20 / 100) * produto + produto
        if xvezes >= 3 and xvezes <= 12:
            print(f'Para pagamento em 3x ou mais no cartao, seu produto sai com 20% de juros, ficando assim R${juros20:.2f} / {xvezes}x de R${juros20 / xvezes:.2f}')
            break
        elif xvezes < 3:
            print('\033[1;31mNúmero de parcelas muito baixa para a forma de pagamento escolhida, escolha uma parcela maior\033[m')
        elif xvezes > 12:
            print('\033[1;31mNúmero de parcelas muito alta, escolha uma parcela menor (até 12x)\033[m')
