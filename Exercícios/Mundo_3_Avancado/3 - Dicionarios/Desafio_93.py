# Desafio: Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
# O programa vai ler o nome do jogador e quantas partidas ele jogou. 
# Depois vai ler a quantidade de gols feitos em cada partida. 
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.


print('=====Desafio 93=====')

dados_jogador = {}
dados_jogador["nome"] = str(input('Nome do jogador: ')).strip().capitalize()
dados_jogador['gols'] = []

for i in range(0, int(input(f'Quantas partidas {dados_jogador["nome"]} jogou? '))):
    dados_jogador["gols"].append(int(input(f'Quantos gols na {i+1}o. partida? ')))
dados_jogador["total"] = sum(dados_jogador["gols"])

print('-=-'*20)
print(dados_jogador)
print('-=-'*20)

for k, v in dados_jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=-'*20)
print(f'O jogador {dados_jogador["nome"]} jogou {len(dados_jogador["gols"])} partidas')

for i in range(0, len(dados_jogador["gols"])):
    print(f"{f'=> Na partida {i+1}, fez {dados_jogador['gols'][i]} gols.':>32}")
print(f'Foi um total de {dados_jogador["total"]} gols')