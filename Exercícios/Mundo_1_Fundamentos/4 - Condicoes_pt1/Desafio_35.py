#Desafio: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('=====Desafio 35=====')
r1 = float(input('A medida da primeira reta: '))
r2 = float(input('Da segunda: '))
r3 = float(input('Da terceira: '))

if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print('Suas três medidas PODEM SIM formar um triângulo.')
else:
    print('Suas medidas NÃO PODEM formar um triângulo.')