#Desafio: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

i = '='
print('{} Desafio 6 {}'.format(i*5, i*5))
n1 = int(input('Digite um número: '))
dob = n1*2
tri = n1*3
rz = n1**(1/2)
print('você digitou o número {} \n Seu dobro vale {} \n Seu triplo {} \n Sua raiz quadrada {:.2f}'.format(n1, dob, tri, rz))
