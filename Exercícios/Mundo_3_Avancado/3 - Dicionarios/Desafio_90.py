# Desafio: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
# No final, mostre o conteúdo da estrutura na tela.


print('=====Desafio 90=====')
aluno = dict()
aluno["nome"] = str(input('Nome: ')).strip().capitalize()
aluno["media"] = float(input(f'Média de {aluno["nome"]}: '))
print('-=-' * 20)
print(f'O nome é igual a {aluno["nome"]}')
print(f'A média é igual a {aluno["media"]}')
if aluno["media"] >= 7.0:
    aluno["situacao"] = '\033[1;32maprovado\033[m'
elif 5 <= aluno["media"] < 7:
    aluno["situacao"] = '\033[1;33mRecuperação\033[m'
else:
    aluno["situacao"] = '\033[1;31mreprovado\033[m'
print(f'A situação do {aluno["nome"]} é igual a {aluno["situacao"]}')