#Desafio: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

print('=====Desafio 19=====')
from random import choice
a1 = str(input('Nome do primeiro aluno: '))
a2 = str(input('Do segundo: '))
a3 = str(input('Do terceiro: '))
a4 = str(input('Do quarto: '))
l = [a1, a2, a3, a4]
print('O aluno sorteado foi o(a) {}.'.format(choice(l)))
