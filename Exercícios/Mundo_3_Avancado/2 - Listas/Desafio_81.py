# Desafio: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.


print('=====Desafio 81=====')
valores = list()
resposta = 'SIM'
while resposta in ['SIM', 'S']:
    valores.append(int(input('Digite um valor: ')))
    print('\033[1;32mValor adicionado a lista...')
    while True:
        resposta = str(input('\033[1;33mDeseja continuar?\033[m ')).strip().upper()
        if resposta not in ['SIM', 'S', 'N', 'NAO', 'NÃO']:
            print('\033[1;31mResposta inválida! Tente novamente...\033[m')
        else:
            break
print('-=-'*20)
print(f'Você digitou os valores {valores}')
print('-=-'*20)
print(f'Ao todo você digitou {len(valores)} números')
ordem = sorted(valores)
print(f'A lista dos números de forma decrescente fica {ordem[-1::-1]}')
if 5 in valores:
    for p, v in enumerate(valores):
        if v == 5:
            break
    print(f'O número 5 foi digitado, e está sim na lista na posição {p} (em relação a lista original).')
else:
    print('O número 5 não foi encontrado na lista.')