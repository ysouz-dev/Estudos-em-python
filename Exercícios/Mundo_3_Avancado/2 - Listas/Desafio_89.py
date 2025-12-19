# Desafio: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.


print('=====Desafio 89=====')

from time import sleep

lista_de_alunos = []
indice_alunos = numero_do_aluno = escolha = 0
indice_notas = 1
resposta = 'S'

while resposta in ['SIM', 'S']:
    lista_de_alunos.append([])

    while True:
        nome = str(input('Nome do(a) aluno(a): ')).strip().capitalize()
        if nome.isalpha() == False:
            print('\033[1;31mNome inválido! Tente novamente.\033[m')
        else:
            lista_de_alunos[numero_do_aluno].append(nome)
            break

    for i in range(1,3):
        while True:
            try:
                while True:
                    nota = float(input(f'{i}° Nota do(a) {nome}: '))
                    if nota > 10.0:
                        print('\033[1;31mNota acima do máximo (10.0)\033[m')
                    elif nota < 0:
                        print('\033[1;34mNota abaixo do mínimo (0)\033[m')
                    else:
                        break

                if i == 1:
                    lista_de_alunos[numero_do_aluno].append([])
                lista_de_alunos[numero_do_aluno][1].append(nota)
                break

            except:
                print('\033[1;31mNota inválida! Tente novamente.\033[m')

    while True:
        resposta = str(input('Deseja continuar? ')).strip().upper()
        if resposta in ['SIM', 'S', 'NAO', 'N', 'NÃO']:
            numero_do_aluno += 1
            break
        else:
            print('\033[1;31mResposta inválida! Tente novamente.\033[m')


print('-=-'*15)
print('No. NOME', end='')
print(f'{"MÉDIA":^40}')
print('\033[1m---'*15)

for indice in range(0, len(lista_de_alunos)):
    print(f'{indice:<3} {lista_de_alunos[indice][indice_alunos]:<10} {sum(lista_de_alunos[indice][indice_notas]) / len(lista_de_alunos[indice][indice_notas]):>14.1f}')
print('-=-\033[m'*15)

while True:
    escolha = int(input('''\033[1;33m(Digite 999 para interromper ou 888 para ver o boletim)
Digite o número do aluno que deseja mostrar as notas: \033[m'''))

    if escolha == 888:
        print('-=-'*15)
        print('No. NOME', end='')
        print(f'{"MÉDIA":^40}')
        print('\033[1m---'*15)

        for indice in range(0, len(lista_de_alunos)):
            print(f'{indice:<3} {lista_de_alunos[indice][indice_alunos]:<10} {sum(lista_de_alunos[indice][indice_notas]) / len(lista_de_alunos[indice][indice_notas]):>14.1f}')
        print('-=-\033[m'*15)

    elif escolha == 999:
        print('finalizando...')
        sleep(2)
        print('<<< VOLTE SEMPRE >>>')
        break

    elif 0 <= escolha <= len(lista_de_alunos) - 1:
        print('-=-'*15)
        print(f'Notas de {lista_de_alunos[escolha][indice_alunos]} são {lista_de_alunos[escolha][indice_notas]}')
        print('-=-'*15)

    else:
        print('\033[1;31mEscolha inválida! Tente novamente.\033[m')
