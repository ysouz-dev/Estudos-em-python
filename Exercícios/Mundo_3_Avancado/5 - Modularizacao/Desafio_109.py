# Desafio: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, 
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.


print('=====Desafio 109=====')
from utilidadesCeV.moeda import moeda

preco = float(input('Digite o preço do produto: R$ '))
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, format=True)}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, format=True)}')
print(f'Aumentando 10% de {moeda.moeda(preco)} fica {moeda.aumento(preco, 10, format=True)}')
print(f'Reduzindo 13% de {moeda.moeda(preco)} fica {moeda.diminuir(preco, 13, format=True)}')