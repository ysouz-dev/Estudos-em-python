# Desafio: Escreva um programa que leia um número N inteiro qualquer 
# e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
# Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8

print('=====Desafio 63=====')
print('Sequência de Fibonacci')
print('-' * 30)
numero = int(input('Quantos termos você quer mostrar: '))
contador = 0
f1, f2, f3, f4 = 0, 1, 0, 0
if numero == 1:
    print(f1, end=' > ')
    contador += 1
elif numero == 2:
    print(f1, end=' > ')
    print(f2, end=' > ')
    contador += 2
elif numero > 2:
    print(f1, end=' > ')
    print(f2, end=' > ')
    contador += 2
    while not contador == numero:
        f3 = f1 + f2
        f1 = f3
        print(f3, end=' > ')
        contador += 1
        if contador != numero:
            f4 = f2 + f3
            f2 = f4
            print(f4, end=' > ')
            contador += 1
print('Acabou')
print(f'Esses são os {numero} primeiros termos da sequencia de fibonacci.')
