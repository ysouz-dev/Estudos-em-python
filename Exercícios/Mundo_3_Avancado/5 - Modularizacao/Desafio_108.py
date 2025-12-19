# Desafio: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.


print('=====Desafio 108=====')
from utilidadesCeV.moeda import moeda

preco = float(input('Digite o preço do produto: R$ '))
print(f'A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}')
print(f'Aumentando 10%, fica {moeda.moeda(moeda.aumento(preco, 10))}')
print(f'Reduzindo 13%, fica {moeda.moeda(moeda.diminuir(preco, 13))}')