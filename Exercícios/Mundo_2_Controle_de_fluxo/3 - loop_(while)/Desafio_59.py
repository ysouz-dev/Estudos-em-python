# Desafio: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.


print('=====Desafio 59=====')
fim = False
while fim == False:
    n1 = float(input('Digite o primeiro valor: '))
    n2 = float(input('Digite o segundo valor: '))
    print('-=-' * 10)
    print("""[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA""")
    escolha = int(input('Qual opção você deseja: '))
    print('-=-' * 10)
    if escolha > 5:
        print('Opção inválida, Tente novamente.')
        print('-=-' * 10)
    if escolha == 1:
        r = n1 + n2
        print(f'A soma dos números {n1} e {n2} = {r}')
    elif escolha == 2:
        r = n1 * n2
        print(f'A multiplicação dos números {n1} e {n2} = {r}')
    elif escolha == 3:
        if n1 > n2:
            print(f'O maior número é o {n1}')
        elif n1 == n2:
            print(f'Os número {n1} e {n2} são iguais')
        else:
            print(f'O maior número é o {n2}')
    elif escolha == 5:
        print('Programa encerrado.')
        fim = True
    if fim == False and escolha != 4 and escolha < 6:
        print('-=-' * 10)
        input('Pressione enter para começar novamente')
        print('-=-' * 10)