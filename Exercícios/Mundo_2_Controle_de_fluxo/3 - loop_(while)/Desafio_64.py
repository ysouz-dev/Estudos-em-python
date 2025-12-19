# Desafio:  Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).


print('=====Desafio 64=====')
contador_digitos = 0
soma = 0
numero = 0
while not numero == 999:
    numero = int(input('Digite um número [999 para parar]: '))
    contador_digitos += 1
    soma += numero
    if numero == 999:
        soma -= 999
        contador_digitos -= 1
print('Você acertou a flag(999).')
print(f'Você digitou {contador_digitos} números até a flag')
print(f'A soma desses números (desconsiderando a flag) é {soma}')