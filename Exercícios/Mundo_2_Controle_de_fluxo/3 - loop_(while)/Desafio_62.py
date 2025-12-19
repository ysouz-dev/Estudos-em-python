# Desafio: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
# O programa encerrará quando ele disser que quer mostrar 0 termos.

print('=====Desafio 62=====')
termos = 0
primeiro_termo = 0
quantidade = 9
contador = 0
voltas = 0
pergunta = 'S'
primeiro_termo = int(input('Qual o primeiro termo da sua PA: '))
razao = int(input('Qual sua razão: '))

while pergunta == 'S' or pergunta == 'SIM':
    while not contador == quantidade:
        if voltas == 0:
            print(primeiro_termo, end=' | ')
            termos += 1
            voltas += 1
        primeiro_termo += razao
        print(primeiro_termo, end=' | ')
        termos +=1
        contador += 1

    pergunta = str(input('\nQuer mostrar mais alguns termos? (S/N) ')).strip().upper()
    if pergunta == 'S' or pergunta == 'SIM':
        contador = 0
        quantidade = int(input('Quantos termos a mais: '))
print(f'Progressão finalizada com {termos} termos mostrados.')