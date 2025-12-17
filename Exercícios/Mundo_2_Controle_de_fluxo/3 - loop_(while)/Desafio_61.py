# Desafio: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, 
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('=====Desafio 61=====')
primeiro_termo = int(input('Digite o primeiro termo da sua PA: '))
razao = int(input('Digite sua razao: '))
contador = 0
print(primeiro_termo, end=' > ')
while not contador == 9:
    primeiro_termo += razao
    print(primeiro_termo, end=' > ')
    contador += 1
print('acabou')
print('Essa é sua progressão aritmética.')