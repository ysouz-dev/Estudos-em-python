# Desafio: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.


print('=====Desafio 83=====')
lista_expressao = list()
parenteses = 0
lista_expressao.append(input('Digite a expressão: ').strip())
for expressao in lista_expressao:
    for letras in expressao:
        if parenteses < 0:
            break
        elif letras == '(':
            parenteses += 1
        elif letras == ')':
            parenteses -= 1
print('Sua expressão está ', end='')
if parenteses == 0 :
    print('Válida!')
else:
    print('Errada!')
