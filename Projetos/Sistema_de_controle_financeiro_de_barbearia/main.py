from time import sleep
from utils import menu_principal, linha, cores
from models import Cliente

cor = cores()
Cliente.carregar_arquivo()

while True:
    escolha = menu_principal()
    if escolha == 1:
        print(cor[4], end='')
        linha(20)
        print(cor[0], end='')
        Cliente.cadastrar_novo_cliente()
    elif escolha == 2:
        Cliente.ver_cortes()
    elif escolha == 3:
        Cliente.estatisticas()
    elif escolha == 4:
        Cliente.remover_cliente()
    else:
        print(cor[4], end='')
        linha(20)
        print(f'{cor[1]}Encerrando sistema...')
        sleep(3)
        print(f'Até a próxima.{cor[0]}')
        break