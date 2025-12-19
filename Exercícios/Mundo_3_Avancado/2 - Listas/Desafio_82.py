# Desafio: Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
# Ao final, mostre o conteúdo das três listas geradas.


print('=====Desafio 82=====')
resposta = 'SIM'
valores = list()
impar = list()
par = list()
while resposta in ['SIM', 'S']:
    numero = int(input('Digite um número: '))
    if numero not in valores:
        valores.append(numero)
    while True:
        resposta = str(input('Quer continuar? ')).strip().upper()
        if resposta not in ['SIM', 'S', 'NAO', 'N', 'NÃO']:
            print('\033[1;31mResposta inválida! Tente novamente.\033[m')
        else:
            break
for valor in valores:
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
print('-=-'*20)
print(f'''a lista completa é {valores}
a lista de pares é {par}
a lista de impares é {impar}''')