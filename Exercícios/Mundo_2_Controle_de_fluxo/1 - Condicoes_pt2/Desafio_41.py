# Desafio: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta 
# e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

import datetime
from time import sleep

print('\033[1;31m=====Desafio 41=====\033[m')
print('\033[1;34mConfederação Nacional de Natação\033[m')
ano = int(input('Digite seu ano de nascimento atleta: '))
print('...')
sleep(1)
data = datetime.date.today().year
idade = data - ano
if idade > 0 and idade <= 9:
    print(f'Categoria de {idade} ano(s): MIRIM')
elif idade >= 10 and idade <= 14:
    print(f'Categoria de {idade} anos: INFANTIL')
elif idade >= 15 and idade <= 19:
    print(f'Categoria de {idade} anos: JUNIOR')
elif idade > 19 and idade <= 25:
    print(f'Categoria de {idade} anos: SÊNIOR')
elif idade > 25:
    print(f'Categoria de {idade} anos: MASTER')