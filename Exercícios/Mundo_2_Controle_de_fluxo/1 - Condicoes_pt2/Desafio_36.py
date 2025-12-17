# Desafio: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

cores = {'limpa':'\033[m', 'vermelho':'\033[1;31m', 'azul':'\033[1;34m', 'verde':'\033[1;32m', 'amarelo':'\033[1;33m'}

print(f'{cores['vermelho']}=====Desafio 36====={cores['limpa']}')

casa = float(input(f'{cores['amarelo']}Qual o valor do imóvel: '))
salario = float(input('Digite o seu salário: '))
parcelas = float(input(f'Deseja pagar em quantos anos: {cores['limpa']}'))

if parcelas > 30:
    while parcelas > 30:
        print(f'{cores['vermelho']}Número de parcelas muito alto, digite um número menor (até 30 anos){cores['limpa']}')
        parcelas = int(input(f'{cores['amarelo']}Deseja pagar em quantas parcelas:{cores['limpa']} '))

parcelas2 = parcelas * 12
parcelas1 = casa / parcelas2

print(f'Para pagar uma casa de R${casa:.2f}, em {parcelas} ano(s) a parcela sera de R${parcelas1:.2f} ')

if parcelas1 <= (30 / 100) * salario:
    print(f'{cores['azul']}Seu impréstimo foi {cores['verde']}APROVADO{cores['limpa']} {cores['azul']}em {parcelas2:.0f}x de R${parcelas1:.2f}')
else:
    print(f'{cores['azul']}Seu impréstimo foi {cores['vermelho']}NEGADO{cores['limpa']}')