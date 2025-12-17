#Desafio: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

i = '='
print('{} Desafio 13 {}'.format(5*i, 5*i))
sal = float(input('Qual o valor do seu salário? '))
porc2 = int(input('Quantos porcento você ganhou de aumento? '))
au = (porc2/100)*sal+sal
print('Você hoje ganha R$ {} de salário, com seus {}% de aumento, seu salário irá para R$ {:.2f} reais '.format(sal, porc2, au))
