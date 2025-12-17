#Desafio: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#considerando 1 dólar = R$3,27

i = '='
print('{} Desafio 10 {}'.format(5*i, 5*i))
rs = float(input('Qual valor você gostaria de converter? '))
dol = rs/3.27
print('Com seus R${:.0f} reais você consegue converter em U${:.2f} dólares'.format(rs, dol))
