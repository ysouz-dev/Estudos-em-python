# Desafio: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.


from time import sleep
print('=====Desafio 72=====')
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
resposta = 'SIM'
while resposta in ['SIM','S']:
    while True:
        numero = int(input('Digite um número entre 0 e 20: '))
        if  0 <= numero <= 20:
            break
        else:
            print('\033[1;31mNúmero inválido!\033[m')
    print(f'Você digitou o número {numeros[numero]}')
    sleep(3)
    while True:
        resposta = str(input('Deseja digita um número de novo? ')).strip().upper()
        if resposta not in ['SIM', 'S', 'NAO', 'N', 'NÃO']:
            print('\033[1;31mResposta inválida! Tente novamente.\033[m')
        else:
            break
print('============ Programa encerrado ============')