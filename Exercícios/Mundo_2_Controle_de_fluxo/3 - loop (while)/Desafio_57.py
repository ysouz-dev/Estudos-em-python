# Desafio: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. 
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

cores = {'azul':'\033[1;34m', 'rosa':'\033[1;35m', 'fim':'\033[m', 'vermelho':'\033[1;31m'}

print('=====Desafio 57=====')
sexo = str(input(f'Digite seu sexo ( {cores["azul"]}M {cores["fim"]}OU {cores["rosa"]}F {cores["fim"]}): ')).strip().upper()
while sexo != 'M' and sexo != 'F':
    print(f'{cores["vermelho"]}resposta invalida{cores["fim"]}')
    sexo = str(input('Digite seu sexo: ')).strip().upper()
print(f'Seu sexo é {sexo}: ', end='')
if sexo == 'M':
    print(f'{cores["azul"]}Masculino')
else:
    print(f'{cores["rosa"]}Feminino')