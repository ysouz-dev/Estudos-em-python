# Desafio: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.


print('=====Desafio 80=====')
valores = list()
for i in range(1,6):
    numero = int(input(f'Digite o {i}° valor: '))
    if i == 1:
        valores.append(numero)
        print('Adicionado no final da lista...')
    elif numero > max(valores):
        valores.append(numero)
        print('Adicionado no final da lista...')
    elif numero < min(valores):
        valores.insert(0, numero)
        print('Adicionado na posição 0 da lista...')
    else:
        for posicao, valor in enumerate(valores):
            if valor > numero:
                break
        valores.insert(posicao, numero)
        print(f'Adicionado na posição {posicao} da lista...')
print('-=-'*20)
print(f'Os valores digitados em ordem foram {valores}')
