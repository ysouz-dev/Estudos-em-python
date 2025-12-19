# Desafio: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. 
# Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(), 
# mas com uma validação de dados para aceitar apenas valores que seja monetários.


print('=====Desafio 112=====')

from UtilidadesCeV.dados import dados

preco = float(dados.leia_dinheiro('Digite o preço do produto: R$ ', 'Error! Preço inválido.'))
dados.resumo(preco, 35, 22)