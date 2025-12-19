# Desafio: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.


print('=====Desafio 100=====')

from random import randint
from time import sleep


def somapar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(soma)


def sorteia(lista):
    aleatorio = []
    contador = 0
    while contador <= 4:
        numero = randint(1,10)
        if numero not in aleatorio:
            aleatorio.append(numero)
            contador += 1
    for valor in aleatorio:
        lista.append(valor)


sorteados = []

sorteia(sorteados)
print(f'Sorteando {len(sorteados)} valores da lista: ', end='')
for valor in sorteados:
    print(f'{valor} ', end='')
    sleep(0.3)
print('Pronto!')

print(f'Somando os valores pares de {sorteados}, temos ', end='')
somapar(sorteados)
