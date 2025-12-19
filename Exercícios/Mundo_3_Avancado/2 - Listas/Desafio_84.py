# Desafio: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.


print('=====Desafio 84=====')

from time import sleep

alunos = []
aluno_da_vez = 0
maior_peso = menor_peso = 0

while True:
    alunos.append([])
    alunos[aluno_da_vez].append(str(input('Nome: ')).strip().capitalize())
    alunos[aluno_da_vez].append(float(input('Peso: ')))

    if aluno_da_vez == 0:
        maior_peso = alunos[aluno_da_vez][1]
        menor_peso = alunos[aluno_da_vez][1]

    elif alunos[aluno_da_vez][1] > maior_peso:
        maior_peso = alunos[aluno_da_vez][1]

    elif alunos[aluno_da_vez][1] < menor_peso:
        menor_peso = alunos[aluno_da_vez][1]

    aluno_da_vez += 1

    while True:
        resposta = str(input('Deseja continuar? ')).strip().upper()
        if resposta not in ['SIM', 'S', 'N', 'NAO', 'NÃO']:
            print('Resposta inválida!')
            sleep(1)
        else:
            break
    if resposta in ['N', 'NAO', 'NÃO']:
        break

print('-=-'*20)
print(f'Foram cadastradas ao todo {len(alunos)} pessoas')

print(f'O maior peso cadastrado foi de {maior_peso}kg. Peso de ', end='')
for numero_do_aluno in alunos:
    if numero_do_aluno[1] == maior_peso:
        print(f"[{numero_do_aluno[0]}]", end=' ')

print(f'\nO menor peso cadastrado foi de {menor_peso}kg. Peso de ', end='')
for numero_do_aluno in alunos:
    if numero_do_aluno[1] == menor_peso:
        print(f"[{numero_do_aluno[0]}]", end=' ')
