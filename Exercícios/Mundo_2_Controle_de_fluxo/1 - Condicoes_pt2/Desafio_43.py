# Desafio: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida


#tilulo
print('\033[1;31m=====Desafio 43=====\033[m')
print('\n\033[4;34mCalculadora de IMC\033[m')
#entrada
peso = float(input('Qual o seu peso corporal (kg): '))
altura = float(input('Qual sua altura (ex: 1.70, 1.80, 1.90): '))
im = peso / altura ** 2
#saida
print(f'com {peso}kg e {altura} de altura, seu imc deu {im:.1f}')
#condicao
if im < 18.5:
    print('Voce está \033[4mABAIXO DO PESO\033[m.')
elif im <= 25.0:
    print('Voce está no \033[1;34mPESO IDEAL\033[m.')
elif im <= 30.0:
    print('Voce esta com \033[33mSOBREPESO\033[m.')
elif im <= 40.0:
    print('Voce esta com \033[1;33mOBESIDADE\033[m.')
else:
    print('Voce esta com \033[1;31mOBESIDADE MÓRBIDA, CUIDADO!\033[m')