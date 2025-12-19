# Desafio: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, 
# só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt('Digite um n: ')


print('=====Desafio 104=====')


def leia_inteiro(pergunta):
    while True:
        n = input(pergunta)
        if n.isnumeric() == True:
            n = int(n)
            return n
        else:
            print('\033[1;31mError! Digite um número inteiro válido.\033[m')


#programa principal
print('-' * 15)
numero = leia_inteiro('Digite um número: ')
print(f'Você digitou o número {numero}.')