# Desafio: Crie um programa que leia a idade e o sexo de várias pessoas. 
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.


print('=====Desafio 69=====')
print('='*20)
print('cadastro de pessoas'.upper())
pessoas_maior_idade = total =qnt_homens_cadastrados = qnt_mulheres_20mais = 0
while True:
    print('='*20)
    idade = int(input('Digite a idade: '))
    while True:
        print('='*20)
        sexo = str(input('Digite o sexo: ')).strip().upper()
        if sexo not in ['F', 'FEMININO', 'M', 'MASCULINO']:
            print('='*20)
            print('Sexo digitado inválido!')
        else:
            break
    total += 1
    if idade > 18:
        pessoas_maior_idade += 1
    if sexo in ['M', 'MASCULINO']:
        qnt_homens_cadastrados += 1
    if sexo in ['F', 'FEMININO'] and idade > 20:
        qnt_mulheres_20mais += 1
    while True:
        print('='*20)
        decisao = str(input('Quer continuar a cadastrar mais pessoas? '.title())).strip().upper()
        if decisao not in ['NAO', 'N', 'NÃO'] and decisao not in ['SIM', 'S']:
            print('='*20)
            print('Resposta inválida!')
        else:
            break
    if decisao in 'NNAONÃO':
        print('='*20)
        print('Sistema de cadastro encerrado.'.title())
        break
print('='*20)
print(f"""{total} Pessoas foram registradas, sendo...
{pessoas_maior_idade} Maiores de 18 anos.
{qnt_homens_cadastrados} Homens cadastrados.
{qnt_mulheres_20mais} Mulheres com mais de 20 anos""")

