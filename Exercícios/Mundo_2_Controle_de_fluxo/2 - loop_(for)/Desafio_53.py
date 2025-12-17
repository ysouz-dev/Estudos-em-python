# Desafio: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, 
# desconsiderando os espaços. Exemplos de palíndromos:
# - APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

print('=====Desafio 53=====')
print('-=-' * 19)
print(' ' * 10,'Detector de palavras palíndromas')
print('-=-' * 19)
frase = str(input('Digite uma frase: '))
frase1 = frase.lower().strip().replace(' ', '')
print(f'A frase que você digitou "{frase.strip().capitalize()}" ao contrario fica {frase[::-1]} ela ', end='')
if frase1[::-1] == frase1:
    print('é SIM um palíndromo.')
else:
    print('NÃO é um palíndromo.')