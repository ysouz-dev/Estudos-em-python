# Desafio: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
# No final, mostre: 
# A) Quantas pessoas foram cadastradas 
# B) A média de idade C) Uma lista com as mulheres 
# D) Uma lista de pessoas com idade acima da média


print('=====Desafio 94=====')

pessoas = []

pessoa_da_vez = soma_das_idades = 0
resposta = 'S'

while resposta in ['SIM', 'S']:
    pessoas.append({})

    while True:
        pessoas[pessoa_da_vez]["nome"] = str(input('Digite seu nome: ')).strip().capitalize()

        if pessoas[pessoa_da_vez]["nome"].isalpha() == False:
            print('\033[1;31mNome inválido! Tente novamente.\033[m')
        else:
            break

    while True:
        pessoas[pessoa_da_vez]["sexo"] = str(input('Digite seu sexo: ')).strip().upper()

        if pessoas[pessoa_da_vez]["sexo"] not in ['MASCULINO', 'M', 'FEMININO', 'F']:
            print('\033[1;31mGênero sexual inválido! Tente novamente.\033[m')

        else:
            break

    while True:
        try:
            pessoas[pessoa_da_vez]["idade"] = int(input('Qual sua idade: '))
            soma_das_idades += pessoas[pessoa_da_vez]["idade"]
            break
        except:
            print('\033[1;31mIdade inválida! tente novamente.\033[m')

    pessoa_da_vez += 1
    while True:
        resposta = str(input('Deseja fazer outro registro? ')).strip().upper()
        if resposta not in ['SIM', 'S', 'N', 'NAO', 'NÃO']:
            print('\033[1;31mResposta inválida! Tente novamente.\033[m')
        else:
            break

print('-=-' * 20)
print(f'Ao todo foram registradas {len(pessoas)} pessoas.')

print('-=-' * 20)
print(f'A média de idade do grupo é de {soma_das_idades / len(pessoas):.1f} anos')

print('-=-' * 20)
print(f'{" Listagem das mulheres ":=^50}')
for mulheres in pessoas:
    if mulheres["sexo"] in ['F', 'FEMININO']:
        for key, value in mulheres.items():
            print(f'{key}: {value}', end=' ')
            print('/ ',end='')
        print()

print('-=-' * 20)
print(f'{"> Pessoas com idade acima da média <":=^50}')
for pessoa_acima in pessoas:
    if pessoa_acima["idade"] > (soma_das_idades / len(pessoas)):
        for key, value in pessoa_acima.items():
            print(f'{key}: {value}', end=' ')
            print('/ ', end='')
        print()