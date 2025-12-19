# Desafio: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
# Caso o número já exista lá dentro, ele não será adicionado. 
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.


print('=====Desafio 79=====')
valores = list()
contador = 0
resposta = 'SIM'
while resposta in ['SIM', 'S']:
    valor = int(input('Digite um valor: '))
    if valor not in valores:
        valores.append(valor)
        print('\033[1;32mValor adicionado com sucesso...\033[m')
    elif valor in valores:
        print('\033[1;33mValor duplicado! Não vou adicionar...\033[m')
    while True:
        resposta = str(input('Deseja continuar? ')).strip().upper()
        if resposta not in ['SIM', 'S', 'NAO', 'N', 'NÃO']:
            print('\033[1;31mResposta inválida! Tente novamente\033[m')
        else:
            break
print('-=-'*20)
print('Os valores digitados foram:', sorted(valores))