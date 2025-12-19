print('=====Desafio 115=====')

from Desafio115.interface import interface
from Desafio115.separadores.separadores import titulo
from Desafio115.cores import cores
from pathlib import Path
from time import sleep

cor = cores.cores()
cadastros = []
base_arquivo = Path(__file__).parent


while True:
    escolha = interface.menu()
    if escolha == 1:
        try:
            if len(cadastros) == 0:
                arquivo = open(f'{base_arquivo / 'cadastros.txt'}', 'r')
                for linha in arquivo:
                    nome, idade = linha.strip().split(';')
                    cadastros.append({'nome': nome, 'idade': idade})
        except FileNotFoundError:
            print(f'{cor[1]}Error: não existem cadastros para se ver.{cor[0]}')
        else:
            interface.ver_cadastros(cadastros)
            sleep(2)

    elif escolha == 2:
        pessoa = interface.cadastrar_pessoas()
        cadastros.append(pessoa)
        arquivo = open(f'{base_arquivo / 'cadastros.txt'}', 'a')
        arquivo.write(f'{pessoa["nome"]};{pessoa["idade"]}\n')
        arquivo.close()

    else:
        print(cor[1])
        titulo(f'ENCERRANDO O SISTEMA...')
        sleep(2)
        titulo('ATÉ LOGO')
        print(cor[0])
        break
