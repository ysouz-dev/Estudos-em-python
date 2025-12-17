# Desafio: Crie um programa que faça o computador jogar Jokenpô com você.

from time import sleep
import pygame
from emoji import emojize
import random
from pathlib import Path

print(f'{' '*15}\033[1;31m=====Desafio 45=====\033[m')

cores = {'amarelo':'\033[1;33m', 'azul':'\033[1;34m', 'fim':'\033[m', 'vermelho':'\033[1;31m', 'verde':'\033[1;32m', 'cinza':'\033[1;37m'}

pedra_emoji = emojize(':pedra:', language= 'pt')
papel_emoji = emojize(':página_voltada_para_cima:', language='pt')
tesoura_emoji = emojize(':tesoura:', language='pt')
base_diretorio = Path(__file__).resolve().parent
som_botao = base_diretorio / 'sound_button.mp3'
som_vitoria = base_diretorio / 'sound_victory.mp3'
som_derrota = base_diretorio / 'sound_defeat.mp3'
som_empate = base_diretorio / 'sound_tie.mp3'


print(f'{cores['amarelo']}-=-'*20)
print(f'{' '*14}Bem Vindo ao Jokenpô {pedra_emoji} {papel_emoji} {tesoura_emoji}')
print(f'{cores['amarelo']}-=-'*20)
pygame.mixer.init()

while True:
    input(f'{cores['verde']}{' '*11}> PRESSIONE ENTER PARA COMEÇAR <')
    botao = pygame.mixer.Sound(som_botao)
    botao.play()
    print('Carregando...')
    sleep(1.5)
    ale1 = random.randint(1,3)
    #print(ale1) numero que o pc esta randomizando
    while True:
        print(f'{cores['cinza']}1- PEDRA{pedra_emoji} \n {cores['fim']}2- PAPEL{papel_emoji} \n  {cores['vermelho']}3- TESOURA{tesoura_emoji}')
        escolha = int(input(f'{cores['amarelo']}{' '*12}Qual sua escolha? '))
        if escolha > 3 or escolha < 1:
            print(f'{cores['vermelho']}Escolha inválida')                           #loop de escolha entre papel parede etc
        else:
            print(f'{cores['azul']}Ótima escolha!')
            sleep(0.7)
            break
    if escolha == ale1:
        print('Eu escolho...')
        sleep(1.5)
        if escolha == 1 and ale1 == 1:
            print(f'{cores['cinza']}PEDRA{pedra_emoji}{cores['fim']}')
        elif escolha == 2 and ale1 == 2:
            print(f'{cores['fim']}PAPEL{papel_emoji}')                                          #condiçao empate
        elif escolha == 3 and ale1 == 3:
            print(f'{cores['vermelho']}TESOURA{tesoura_emoji}{cores['fim']}')
        sleep(0.5)
        emp = pygame.mixer.Sound(som_empate)
        emp.play()
        print('DEU EMPATE, VAMOS DE NOVO!')
    elif escolha == 1 and ale1 == 2:                                        #condicoes derrota
        print('Eu escolho...')
        sleep(1.5)
        print(f'{cores['fim']}PAPEL{papel_emoji}')
        der = pygame.mixer.Sound(som_derrota)
        der.play()
        print(f'{cores['vermelho']}EU GANHEI! HAHAHAHA')
    elif escolha == 2 and ale1 == 3:
        print('Eu escolho...')
        sleep(1.5)
        print(f'{cores['vermelho']}TESOURA {tesoura_emoji}')
        der = pygame.mixer.Sound(som_derrota)
        der.play()
        print(f'{cores['vermelho']}EU GANHEI HAHAHAHA')
    elif escolha == 3 and ale1 == 1:
        print('Eu escolho...')
        sleep(1.5)
        print(f'{cores['cinza']}PEDRA {pedra_emoji}')
        der = pygame.mixer.Sound(som_derrota)
        der.play()
        print(f'{cores['vermelho']}EU GANHEI HAHAHAHA')
    elif escolha == 1 and ale1 == 3:                                    #condicoes vitoria
        print('Eu escolho...')
        sleep(1.5)
        print(f'{cores['vermelho']}TESOURA {tesoura_emoji}')
        vit = pygame.mixer.Sound(som_vitoria)
        vit.play()
        print(f'{cores['verde']}VOCÊ ME VENCEU...{emojize(':rosto_desapontado:', language='pt')}')
    elif escolha == 2 and ale1 == 1:
        print('Eu escolho...')
        sleep(1.5)
        print(f'{cores['cinza']}PEDRA {pedra_emoji}')
        vit = pygame.mixer.Sound(som_vitoria)
        vit.play()
        print(f'{cores['verde']}VOCE ME VENCEU...{emojize(':rosto_desapontado:', language='pt')}')
    elif escolha == 3 and ale1 == 2:
        print('Eu escolho...')
        sleep(1.5)
        print(f'{cores['fim']}PAPEL {papel_emoji}')
        vit = pygame.mixer.Sound(som_vitoria)
        vit.play()
        print(f'{cores['verde']}VOCE ME VENCEU...{emojize(':rosto_desapontado:', language='pt')}')