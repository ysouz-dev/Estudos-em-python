# Desafio: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: 
# o nome de um jogador e quantos gols ele marcou. 
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.


print('=====Desafio 103=====')


def ficha(nome='<desconhecido>', gols=0):
    if gols == '' or gols.isnumeric() == False:
        gols = int(0)
    else:
        gols = int(gols)

    if not nome:
        nome = '<desconhecido>'
    print(f'O jogador {nome} fez {gols} gol(s) no campeaonato.')


#programa principal
nome = str(input('Nome do jogador: ')).strip().capitalize()
gols = input('Numero de gols: ')
ficha(nome, gols)
