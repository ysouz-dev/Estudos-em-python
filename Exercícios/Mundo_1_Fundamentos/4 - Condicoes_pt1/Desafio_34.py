# Desafio: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, calcule um aumento de 10%. 
# Para os inferiores ou iguais, o aumento é de 15%.


print('=====Desafio 34=====')
sal = float(input('Digite o valor do seu salário: '))
sal10 = ((10 / 100) * sal) + sal
sal15 = ((15 / 100) * sal) + sal
if sal <= 1250.0:
    print(f'Seu salário é inferior ou igual a R$1250.0, logo seu aumento será de 15%, ficando R${sal15:.2f}')
else:
    print(f'Seu salário ultrapassa R$1250.0, logo seu aumento será de 10%, ficando R${sal10:.2f}')
