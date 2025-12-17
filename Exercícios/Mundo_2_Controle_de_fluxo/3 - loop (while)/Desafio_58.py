# Desafio: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, 
# mostrando no final quantos palpites foram necessários para vencer.


print('=====Desafio 58=====')
from random import randint
print('\033[1;34m-=-' * 20)
print(' ' * 18, 'Jogo da Adivnhação')
print('-=-' * 20, '\033[m')
palpites = 1
numero_aleatorio = randint(1,10) #numero escolhido pelo pc
#print(numero_aleatorio) ver qual numero o pc escolheu
escolha_jogador = int(input('Qual número inteiro você acha que eu pensei? '))

#looping até acertar
while not escolha_jogador == numero_aleatorio:
    print('\033[1;34m-=-' * 20)
    print('\033[1;31mResposta errada! hahahaha')
    if escolha_jogador < numero_aleatorio:
        print('Eu pensei em um pouco mais...')
    else:
        print('Eu pensei em um pouco menos...')
    print('Tente novamente.')
    print('\033[1;34m-=-' * 20)
    palpites += 1
    escolha_jogador = int(input('\033[mQual número inteiro você acha que eu pensei? '))
#saida
print(f'\033[1;32mVocê acertou! eu pensei no número {numero_aleatorio} e você digitou o {escolha_jogador}')
print(f'\033[1;33mPrecisando de {palpites} palpite(s)')
