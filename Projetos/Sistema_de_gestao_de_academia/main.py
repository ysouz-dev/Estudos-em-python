from models import Academia
from utils import menu, titulo
from time import sleep

academia = Academia("Smart Fit")
while True:
    escolha = menu(academia)
    if escolha == 1:
        academia.cadastrar_aluno()
    elif escolha == 2:
        academia.cadastrar_funcionario()
    elif escolha == 3:
        academia.adicionar_equipamento()
    elif escolha == 4:
        academia.listar_alunos()
    elif escolha == 5:
        academia.listar_funcionarios()
    elif escolha == 6:
        academia.listar_equipamentos()
    elif escolha == 7:
        academia.buscar_aluno_por_cpf()
    elif escolha == 8:
        academia.buscar_equipamento_por_codigo()
    else:
        print('\033[1;31m', end='')
        titulo('ENCERRANDO SISTEMA...')
        print('\033[m')
        sleep(2)
        print('MUITO OBRIGADO, VOLTE SEMPRE!!')
        break
