# Desafio: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: 
# o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) 
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

print('=====Desafio 102=====')
def fatorial(num=1, mostrar=False):
    """
    --> Calcula o fatorial de um Número.
    :param num: Número ao ser calculado.
    :param mostrar: (Opcional) Mostrar ou não a conta do fatorial.
    :return: O valor fatorial de um numero.
    """
    fatorial = 1
    print('-' * 25)
    if mostrar == False:
        for i in range(num, 0, -1):
            fatorial *= i

        return fatorial

    else:
        for i in range(num, 0, -1):
            print(f'{i} ', end='x ' if i > 1 else '= ')
            fatorial *= i

        return fatorial

#fatorial(10, mostrar=True)
print(fatorial(5, mostrar=True))