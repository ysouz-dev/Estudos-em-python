#Desafio: Faça um programa que leia a largura e a altura de uma parede em metros,
#calcule a sua área e a quantidade de tinta necessária para pintá-la,
#sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

i = '='
print('{} Desafio 11 {}'.format(5*i, 5*i))
alt = float(input('Qual a altura da superfície: '))
lag = float(input('Qual a largura da superfície: '))
area = alt*lag
tint = area/2
print('Tendo {}m² de altura e {}m² de largura, sua superfície tem {:.2f}m² de área. Assim precisando de {:.2f}L de tinta para pintar a superficie'.format(alt, lag, area, tint))
