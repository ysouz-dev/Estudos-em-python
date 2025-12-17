# Desafio: Crie um programa que leia duas notas de um aluno e calcule sua média, 
# mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

print('\033[1;31m=====Desafio 40=====\033[m')
not1 = float(input('Digite sua primeira nota: '))
not2 = float(input('Digite sua segunda nota: '))
med = (not1 + not2) / 2
if med < 5.0:
    print(f'Sua média foi de {med:.1f}, você está \033[1;31mREPROVADO')
elif med >= 5.0 and med <= 6.9:
    print(f'Sua média foi de {med:.1f}, você está de \033[1;34mRECUPERAÇÃO')
elif med >= 7.0:
    print(f'Sua média foi de {med:.1f}, você está \033[1;32mAPROVADO(A)')