#Desafio: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

i = '='
print('{} Desafio 7 {}'.format(5*i, 5*i))
not1 = float(input('Qual sua primeira nota? '))
not2 = float(input('E sua segunda? '))
med = (not1 + not2)/2
print('Sua primeira nota sendo {} e a segunda {} você obteve uma média de {:.1f} pontos'.format(not1, not2, med))
