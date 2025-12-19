# Desafio: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.


print('=====Desafio 78=====')
valores = list()
posicoes_maior_valor = list()
posicoes_menor_valor = list()
for i in range(1,6):
    valores.append(int(input(f'Digite o {i} valor : ')))
print('-=-'*20)
print(f'Você digitou os valores {valores}')
for posicao, valor in enumerate(valores):
    if valor == max(valores):
        posicoes_maior_valor.append(posicao)
    elif valor == min(valores):
      posicoes_menor_valor.append(posicao)
print(f'O maior valor digitado foi o {max(valores)} nas posições ', end='')
for posmax in posicoes_maior_valor:
    print(posmax, end='... ')
print(f'\nO menor valor digitado foi o {min(valores)} nas posições ', end='')
for posmin in posicoes_menor_valor:
    print(posmin, end='... ')
