# Desafio: Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), 
# que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.


print('=====Desafio 110=====')
from utilidadesCeV.dados.dados import resumo

preco = float(input('Digite o preço do produto: R$ '))
resumo(preco, 80, 35)
