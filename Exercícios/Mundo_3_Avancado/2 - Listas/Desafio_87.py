# Desafio: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.


print('=====Desafio 87=====')

matrizes = [[], [], []]

soma_pares = soma_coluna = 0

for linha in range(0,3):
    for coluna in range(0,3):
        matrizes[linha].append(int(input(f'Digite um valor para [{linha}, {coluna}]: ')))
print('-=-'*20)

print('Sua matriz fica: ')

for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[  {matrizes[linha][coluna]}  ]', end='')

        if matrizes[linha][coluna] % 2 == 0:
            soma_pares += matrizes[linha][coluna]

        if coluna == 2:
            soma_coluna += matrizes[linha][coluna]
    print()

print('-=-'*20)
print(f'A soma de todos os pares digitados: {soma_pares}')
print(f'A soma dos valores da terceira coluna: {soma_coluna}')
print(f'O maior valor da segunda linha: {max(matrizes[1])}')
