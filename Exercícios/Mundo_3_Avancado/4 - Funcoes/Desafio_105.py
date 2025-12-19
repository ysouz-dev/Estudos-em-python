# Desafio: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma 
# – A situação (opcional)


print('=====Desafio 105=====')


def notas(*notas, situacao=False):
    """
    --> função para analisar varias notas e situação de um aluno.
    :param notas: Uma ou mais notas do aluno (aceita quantas forem necessárias)
    :param situacao: Valor opcional, indicando se deve ou não adicionar a situação do aluno
    :return: Um dicionário com várias informações sobre a situação do aluno
    """
    notas_do_aluno = {}

    #total de notas
    total_de_notas = len(notas)

    #maior nota e menor nota e média
    maior_nota = menor_nota = media_das_notas = 0
    for nota in notas:
        media_das_notas += nota
        if maior_nota == 0 and menor_nota == 0:
            maior_nota = nota
            menor_nota = nota

        elif nota > maior_nota:
            maior_nota = nota

        elif nota < menor_nota:
            menor_nota = nota

    media_das_notas /= len(notas)

    #adicionando ao dicionario
    notas_do_aluno['Total'] = total_de_notas
    notas_do_aluno['Maior nota'] = maior_nota
    notas_do_aluno['Menor nota'] = menor_nota
    notas_do_aluno['Média'] = f'{media_das_notas:.2f}'
    if situacao == True:
        sit = ''
        if media_das_notas <= 4.9:
            sit = 'RUIM'
        elif media_das_notas <= 6.9:
            sit = 'RAZOÁVEL'
        else:
            sit = 'EXCELENTE'

        notas_do_aluno['Situação'] = sit

    return notas_do_aluno


#programa principal
resp = notas(3.5, 2, 6.5, 2, 7, 4, situacao=True)
print(resp)
