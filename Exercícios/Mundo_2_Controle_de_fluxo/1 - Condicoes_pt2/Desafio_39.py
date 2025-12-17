# Desafio: Faça um programa que leia o ano de nascimento de um jovem 
# e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
# se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

print('\033[1;31m=====Desafio 39=====\033[m')
print('\033[1;32mAlistamento militar\033[m')
import datetime
ano = int(input('Qual seu ano de nascimento: '))
idade = datetime.date.today().year - ano
sex = str(input('Você é do sexo feminino ou masculino (Responder com M ou F): ')).strip().lower()
if sex == 'm':
    print(f'Voce nasceu no ano {ano} e tem {idade} anos.')
    if idade == 18:
        print('Você esta na idade de se alistar!')
    elif idade > 18:
        passou = idade - 18
        print('Voce ja passou do tempo de se alistar')
        print(f'se passaram {passou} ano(s)')
    elif idade < 18:
        faltam = 18 - idade
        print('Voce ainda nao chegou a idade para se alistar')
        print(f'Faltam {faltam} ano(s)')
else:
    print('Você é do segmento femenino. Não precisa se alistar.')