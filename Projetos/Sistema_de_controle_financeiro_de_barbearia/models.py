from datetime import date
from utils import validador_de_string, validador_de_numero
from utils import titulo, cores
from time import sleep
from pathlib import Path

cor = cores()

class Cliente:
    lista = []
    base_diretorio = Path(__file__).parent

    def __init__(self, nome_do_cliente, servico, valor_do_servico, registro):
        self.nome = nome_do_cliente
        self.servico = servico
        self.valor = valor_do_servico
        self.data = registro

    @classmethod
    def cadastrar_novo_cliente(cls):
        data = str(date.today()).split('-')
        cliente = validador_de_string('Nome: ', 'Nome inválido, tente novamente.')
        servico = validador_de_string('Serviço realizado: ', 'serviço inválido, tente novamente.')
        valor = validador_de_numero(float, 'Valor: R$ ')
        registro = f'{data[2]}/{data[1]}/{data[0]}'
        pessoa = Cliente(cliente, servico, valor, registro)
        Cliente.lista.append(pessoa)
        arquivo = open(f'{cls.base_diretorio / 'CortesDoMes.txt'}', 'a')
        arquivo.write(f'{cliente};{servico};{valor};{pessoa.data}\n')
        arquivo.close()
        print('\033[4;32mCliente cadastrado com sucesso!\033[m')
        sleep(1)

    @classmethod
    def ver_cortes(cls):
        if len(cls.lista) > 0:
            print(cor[4], end='')
            titulo('Cortes do mês')
            print(cor[0], end='')
            for posicao, cliente in enumerate(cls.lista):
                print(f'{posicao + 1} - Nome: {cor[4]}{cliente.nome}{cor[0]} | Serviço: {cor[4]}{cliente.servico}{cor[0]} | Valor: {cor[2]}R$ {cliente.valor:.2f}{cor[0]} | Data: {cliente.data}')
            sleep(2)
            input(f'{cor[3]}Pressione ENTER para continuar{cor[0]}')
        else:
            print(f'{cor[1]}Não possui nenhum cadastro de corte no sistema.{cor[0]}')

    @classmethod
    def estatisticas(cls):
        if len(cls.lista) > 0:
            soma_valores = 0
            print(cor[4], end='')
            titulo('Estátisticas desse mês')
            print(cor[0], end='')
            for cliente in cls.lista:
                soma_valores += cliente.valor
            print(f'Total de clientes: {cor[3]}{len(cls.lista)} cliente(s){cor[0]}')
            print(f'Total recebido: {cor[2]}R$ {soma_valores:.2f}{cor[0]}')
            input(f'{cor[3]}Pressione ENTER para continuar{cor[0]}')
            return
        else:
            print(f'{cor[1]}Não possui nenhum cadastro de corte para mostrar estatística.{cor[0]}')

    @classmethod
    def remover_cliente(cls):
        print(f'{cor[4]}-{cor[0]}'*20)
        removido = validador_de_string('Nome de quem você deseja remover: ', 'digite um nome válido.')
        cliente_encontrado = None
        for cliente in cls.lista:
            if cliente.nome.lower() == removido.lower():
                cliente_encontrado = cliente
                break

        if cliente_encontrado:
            cls.lista.remove(cliente_encontrado)
            print(f'{cor[2]}Cliente {removido}{cor[1]} removido{cor[2]} com sucesso.{cor[0]}')
            arquivo = open(f'{cls.base_diretorio / 'CortesDoMes.txt'}', 'w')
            for pessoa in cls.lista:
                 arquivo.write(f'{pessoa.nome};{pessoa.servico};{pessoa.valor};{pessoa.data}\n')
            arquivo.close()
        else:
            print(f'{cor[1]}Cliente {removido} não foi encontrado na lista.{cor[0]}')

    @classmethod
    def carregar_arquivo(cls):
        try:
            arquivo = open(f'{cls.base_diretorio / 'CortesDoMes.txt'}', 'r')
        except FileNotFoundError:
            pass
        else:
            for linha in arquivo:
                nome, servico, valor, data = linha.strip().split(';')
                cls.lista.append(Cliente(nome, servico, float(valor), data))
