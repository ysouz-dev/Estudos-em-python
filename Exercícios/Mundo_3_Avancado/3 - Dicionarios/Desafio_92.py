# Desafio: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.


print('=====Desafio 92=====')

from datetime import date

cadastro = {}
cadastro["nome"] = str(input('Nome: ')).strip().capitalize()
cadastro["idade"] = date.today().year - int(input('Ano de nascimento: '))
cadastro["CTPS"] = int(input('Carteira de Trabalho (0 não tem): '))

if cadastro["CTPS"] != 0:
    cadastro["contratacao"] = int(input('Ano de contratação: '))
    cadastro["salario"] = float(input('Salário: R$ '))
    cadastro["aposentadoria"] = cadastro["contratacao"] + 35 - (date.today().year - cadastro["idade"])

print('-=-'*20)
for k, v in cadastro.items():
    print(f'{k} tem o valor {v}')