# Desafio: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: a média de idade do grupo, 
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

print('=====Desafio 56=====')

media_idades = 0
idade_mulheres = 0
homem_mais_velho = ''
idade_homem_mais_velho = 0

for pessoas in range(1,5):
    print(f'-=-=-{pessoas}° Pessoa-=-=-')
    nome = str(input(f'Digite o nome da {pessoas}° pessoa: ')).strip().lower()
    idade = int(input(f'Digite a idade do(a) {nome}: '))
    sexo =  str(input(f'Qual gênero sexual do(a) {nome}: ')).strip().lower()
    media_idades += idade
    if idade > idade_homem_mais_velho and (sexo == 'masculino' or sexo == 'm'):
        idade_homem_mais_velho = idade
        homem_mais_velho = nome
    if (sexo == 'feminino' or sexo == 'f') and idade < 20:
        idade_mulheres += 1
        
print(f"""A média de idade do grupo é de {media_idades / 4:.1f} anos.
O homem mais velho, é o {homem_mais_velho} com {idade_homem_mais_velho} anos.
{idade_mulheres} mulhere(s) tem menos de 20 anos.""")