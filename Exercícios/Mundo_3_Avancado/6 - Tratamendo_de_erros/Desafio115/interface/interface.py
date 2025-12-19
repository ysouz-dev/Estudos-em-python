from Desafio115.separadores import separadores
from Desafio115.cores import cores
from Desafio115.validadores import validadores
from time import sleep

cor = cores.cores()


def menu():
    separadores.titulo('MENU PRINCIPAL')
    print(f'{cor[3]}1 - {cor[4]}Ver pessoas cadastradas')
    print(f'{cor[3]}2 - {cor[4]}Cadastrar nova pessoa')
    print(f'{cor[3]}3 - {cor[4]}Sair do Sistema{cor[0]}')
    separadores.linha(34)
    while True:
        opcao = validadores.validador_de_numero(int, f'{cor[3]}Digite a opção desejada: {cor[0]}', 'Error: opção inválida!')
        if  1 > opcao or opcao > 3:
            print(f'{cor[1]}Error: não existe opção {opcao}, tente novamente.{cor[0]}')
        else:
            return opcao


def cadastrar_pessoas():
    dict = {}
    separadores.titulo('NOVO CADASTRO')
    dict["nome"] = validadores.validador_de_string('Nome: ', 'Error: nome inválido, tente novamente.').title()
    dict["idade"] = validadores.validador_de_numero(int, 'Idade: ', 'Error: idade inválida, tente novamente.')
    sleep(1)
    print(f'{cor[2]}Cadastro de {dict["nome"]} adicionado com sucesso.{cor[0]}')
    return dict


def ver_cadastros(lista):
    separadores.titulo('PESSOAS CADASTRADAS')
    for pessoa in lista:
        print(f'{pessoa["nome"]:<30} {pessoa["idade"]} anos')
