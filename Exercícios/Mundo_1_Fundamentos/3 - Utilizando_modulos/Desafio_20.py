#Desafio: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

print('=====Desafio 20=====')
from random import sample
al1 = str(input('primeiro aluno: '))
al2 = str(input('segundo aluno: '))
al3 = str(input('terceiro aluno: '))
al4 = str(input('quarto aluno: '))
lis = [al1, al2, al3, al4]
print('A lista de apresentação é essa: \n{}'.format(sample(lis, k=len(lis))))
