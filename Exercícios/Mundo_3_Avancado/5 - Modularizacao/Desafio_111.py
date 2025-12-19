# Desafio: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. 
# Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.


print('=====Desafio 111=====')
from utilidadesCeV.dados.dados import resumo

preco = float(input('Digite o valor do produto: R$ '))
resumo(preco, 35, 22)
