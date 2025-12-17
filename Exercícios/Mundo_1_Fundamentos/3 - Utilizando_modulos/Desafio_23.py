#Desafio: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

print('=====Desafio 23=====')
nu = str(input('Digite um número de 0 a 9999: '))
nu1 = '000' + nu
print(f"""O número {nu} tem como as seguintes casas decimais
        Milhar: {nu1[-4]}
        Centena: {nu1[-3]}
        Dezena: {nu1[-2]}
        Unidade: {nu1[-1]}""")
