# Desafio: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.




print('=====Desafio 75=====')
lista = (int(input('Digite o primeiro valor: ')), int(input('Digite o segundo valor: ')), int(input('Digite o terceiro valor: ')), int(input('Digite o quarto valor: ')))
print(f'Os números digitados foram {lista}')
print(f'O número 9 apareceu {lista.count(9)} vezes.')
if 3 in lista:
    print(f'O número 3 apareceu a primeira vez na {lista.index(3) + 1} posiçao')
else:
    print('O número 3 não foi digitado nenhuma vez')
print('Os números pares digitados foram: ', end='')
for pares in lista:
    if pares % 2 == 0:
        print(pares, end=' > ')
print('Fim')
