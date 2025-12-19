# Desafio: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.


print('=====Desafio 113=====')


def leia_inteiro(message):
    while True:
        try:
            inteiro = int(input(message))
        except ValueError:
            print('\033[1;31mError: digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\033[1;31mO usuário preferiu não digitar esse número\033[m')
            return 0
        else:
            return inteiro


def leia_float(message):
    while True:
        try:
            flutuante = float(input(message))
        except ValueError:
            print('\033[1;31mError: digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print('\033[1;31mO usuário preferiu não digitar esse número\033[m')
            return 0
        else:
            return flutuante


#programa principal
inteiro = leia_inteiro('Digite um inteiro: ')
real = leia_float('Digite um Real: ')
print(f'O número inteiro digitado foi o {inteiro} e o Real foi o {real}')