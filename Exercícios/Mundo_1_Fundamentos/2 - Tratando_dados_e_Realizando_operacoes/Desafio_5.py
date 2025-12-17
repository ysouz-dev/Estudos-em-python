#Desafio: Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e antecessor

i = '='
print('{} Desafio 5 {}'.format(5*i, 5*i))
n = int(input('Digite um número: '))
print('O número {} tem como sucessor o {} e seu antecessor o {}'.format(n, n+1, n-1))
