# Desafio: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
# Guarde esses resultados em um dicionário em Python. 
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.


print('=====Desafio 91=====')

from random import randint
from time import sleep
from operator import itemgetter

jogadores = dict()

for jogadas in range(1,5):
    dado = randint(1,6)
    jogadores[f"Jogador {jogadas}"] = dado

print('Valores Sorteados:')
for k, v in jogadores.items():
        print(f'{f"O {k} tirou {v}":>23}')
        sleep(1)

ordem = {}
ordem = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('Ranking dos jogadores:')
for posicao, jogador in enumerate(ordem):
    print(f'{f"{posicao + 1} lugar: {jogador[0]} com o resultado {jogador[1]}":>40}')