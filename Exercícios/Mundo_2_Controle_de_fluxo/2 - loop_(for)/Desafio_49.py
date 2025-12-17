# Desafio: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, 
# só que agora utilizando um laço for.

print('-=-=-Desafio 49-=-=-\n')
#apresentaçao
print('-=-' * 10)
print(' ' * 10, 'Tabuada')
print('-=-' * 10)
#entrada
numero = int(input('Digite o número que deseja saber a tabuada: '))
print('-=-' * 10)
#laço de repetiçao
for t in range (1, 11):
    print(f'{numero} x {t:=2} = {numero*t}')
print('-=-' * 10)