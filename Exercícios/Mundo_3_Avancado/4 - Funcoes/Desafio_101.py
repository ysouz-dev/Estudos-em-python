# Desafio: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, 
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.


print('=====Desafio 101=====')


def voto(nascimento):
    """
    --> Função para descobrir se uma pessoa tem obrigatoriedade ou não o voto nas eleições
    :param nascimento: Data de nascimento da pessoa
    :return: Retorna a idade da pessoa e se o voto é (OBRIGATÓRIO, OPCIONAL, NÃO VOTA)
    """
    print('-' * 15)
    #from datetime import date
    ano = 2018 #date.today().year
    idade = ano - nascimento
    if idade <= 15:
        return print(f'Com {idade} anos: NÃO VOTA.')
    elif idade <= 17 or idade >= 65:
        return print(f'Com {idade} anos: VOTO OPCIONAL.')
    else:
        return print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')


#programa principal
voto(int(input('Que ano você nasceu? ')))