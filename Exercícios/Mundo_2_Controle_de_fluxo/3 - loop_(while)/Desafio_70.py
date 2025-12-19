# Desafio: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. 
# No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.


print('=====Desafio 70=====')
#imports / tuplas
cores = {'vermelho':'\033[1;31m', 'fim':'\033[m', 'verde':'\033[4;32m'}
from time import sleep

#apresentacao
print('-'*20)
print(f'{' ':^3}LOJA DO POVAO')

#contadores
total_de_produtos = total_gasto = produtos_mais_de_mil = valor_produto_mais_barato = 0
nome_produto_mais_barato = ''

#looping das entradas
while True:
    while True:
        print('-'*20)
        produto = str(input('Nome do produto: ')).strip().upper()
        if produto.isnumeric() == True:
            print('-'*20)
            print(f'{cores['vermelho']}Produto inválido{cores['fim']}')
        else:
            break

    while True:
        try:
            print('-'*20)
            preco = float(input('Valor do produto: R$ '))
            break
        except:
            print('-'*20)
            print(f'{cores['vermelho']}Resposta invalida! Tente novamente.{cores['fim']}')
    print('-'*20)
    print(f'{cores['verde']}Produto Cadastrado.{cores['fim']}')

#logica das saidas
    if total_gasto == 0:
        nome_produto_mais_barato = produto
        valor_produto_mais_barato = preco
    total_gasto += preco
    total_de_produtos +=1
    if preco < valor_produto_mais_barato:
        valor_produto_mais_barato = preco
        nome_produto_mais_barato = produto
    if preco > 1000:
        produtos_mais_de_mil += 1

#decisao final
    while True:
        print('-'*20)
        decisao = str(input('Deseja continuar? ')).strip().upper()
        if decisao not in ['NAO', 'N', 'NÃO', 'SIM', 'S']:
            print('-'*20)
            print(f'{cores['vermelho']}Resposta inválida! Tente novamente.{cores['fim']}')
        else:
            break
    if decisao in ['N', 'NAO', 'NÃO']:
        print('-'*20)
        print('Programa encerrado.'.title())
        sleep(0.8)
        print('Analisando...')
        sleep(2)
        break

print('-'*20)
print(f'''Total de produtos: {total_de_produtos}
Total da compra: R${total_gasto:.2f}
Produtos que custam mais de R$1000: {produtos_mais_de_mil}
Nome do produto mais barato: {nome_produto_mais_barato}''')
