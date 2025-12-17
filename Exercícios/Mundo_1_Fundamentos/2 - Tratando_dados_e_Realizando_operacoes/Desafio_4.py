#Desafio: Faça um programa que leia algo pelo teclado e mostre na tela
#o seu tipo primitivo e todas as informações possiveis sobre ela.

print('===Desafio 4===')
alg = input('Digite algo: ')
tip = type(alg)
n = alg.isnumeric()
coff = alg.islower()
con = alg.isupper()
d = alg.isdecimal()
let = alg.isalpha()
print('o valor é da {}\n É um número: {}\n O valor esta em caixa baixa: '
      '{}\n O valor esta em caixa alta: {}\n O valor é decimal: {}\n '
      'O valor só tem letras: {}'.format(tip, n, coff, con, d, let))
