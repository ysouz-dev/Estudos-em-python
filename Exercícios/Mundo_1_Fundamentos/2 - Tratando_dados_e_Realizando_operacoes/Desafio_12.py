#Desafio: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

i = '='
print('{} Desafio 12 {}'.format(5*i, 5*i))
prec = float(input('Qual o preço do produto? '))
porc = int(input('Qual a porcentagem de desconto? '))
desc = prec-(porc/100)*prec
print('O produto com valor de {} sofrendo {}% de desconto cai para {:.2f}'.format(prec, porc, desc))
