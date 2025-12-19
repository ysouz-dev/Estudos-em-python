# Desafio: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). 
# Faça também um programa que importe esse módulo e use algumas dessas funções.


print('=====Desafio 107=====')
from utilidadesCeV.moeda import moeda

preco_do_produto = float(input('Digite o valor do produto: R$ '))
print(f'A metade de R$ {preco_do_produto:.2f} é {moeda.metade(preco_do_produto):.2f}')
print(f'O dobro de R$ {preco_do_produto:.2f} é {moeda.dobro(preco_do_produto):.2f}')
print(f'Aumentando 10%, temos R$ {moeda.aumento(preco_do_produto, 10):.2f}')
print(f'Reduzindo 13%, temos R$ {moeda.diminuir(preco_do_produto, 13):.2f}')