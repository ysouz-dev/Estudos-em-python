# Desafio: Crie um programa que leia números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).


print('=====Desafio 66=====')
count = soma = 0
while True:
    numero = int(input('Digite um número (999 para parar): '))
    if numero == 999:
        print('Programa encerrado.')
        break
    soma += numero
    count += 1
print(f'Você digitou {count} valor(es)')
print(f'A soma dele(s) é igual a {soma}')