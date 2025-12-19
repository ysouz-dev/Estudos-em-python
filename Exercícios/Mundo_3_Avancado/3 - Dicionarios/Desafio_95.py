# Desafio: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.


print('=====Desafio 95=====')

from time import sleep

jogadores = []

jogador_da_vez = 0
resposta = 'S'

while resposta in ['SIM', 'S']:
    jogadores.append({})
    jogadores[jogador_da_vez]["nome"] = str(input('Nome do jogador: ')).strip().capitalize()
    jogadores[jogador_da_vez]["gols"] = []

    for i in range(0, int(input(f'Quantas partidas {jogadores[jogador_da_vez]["nome"]} jogou? '))):
        jogadores[jogador_da_vez]["gols"].append(int(input(f'Quantos gols na {i + 1}o. partida? ')))
    jogadores[jogador_da_vez]["total"] = sum(jogadores[jogador_da_vez]["gols"])
    jogador_da_vez += 1

    while True:
        resposta = str(input('Deseja continuar com o registro? ')).strip().upper()
        if resposta not in ['SIM', 'S', 'N', 'NAO', 'NÃO']:
            print('\033[1;31mResposta inválida! Tente novamente.\033[m')
        else:
            print('-=-' * 20)
            break

print('\033[1m---' * 15)
print(f'{"cod":<5} {"Nome":<5} {"Gols":>15} {"Total":>15}')
print('---' * 15)
for posicao, jogador in enumerate(jogadores):
    print(f'{posicao:<5}', end='')
    for key, value in jogador.items():
        print(f'{f"{value}":<18}', end='')
    print()

while True:
    print('---' * 15)
    mostrar = int(input('Mostrar dados de qual jogador? (999 para parar)'))

    if mostrar <= (len(jogadores) - 1) and mostrar >= 0:
        print(f'--- LEVANTAMENTO DO JOGADOR {jogadores[mostrar]["nome"].upper()}:')

        for posicao, jogo in enumerate(jogadores[mostrar]["gols"]):
            print(f'    No jogo {posicao + 1} fez {jogo} gols.')

    elif mostrar == 999:
        print('Encerrando sistema...')
        sleep(3)
        print('>> VOLTE SEMPRE <<')
        break

    else:
        print(f'ERRO! Não existe jogador com o código {mostrar}! Tente novamente.')
