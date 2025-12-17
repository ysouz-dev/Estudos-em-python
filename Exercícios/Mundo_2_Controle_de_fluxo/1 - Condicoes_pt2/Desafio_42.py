#Desafio: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes


print('\033[1;31m=====Desafio 42=====\033[m')
print('\033[4;32mCalculadora de Condição de Existencia de Triangulos\033[m')
r1 = float(input('Digite o valor do primeiro segmento: '))
r2 = float(input('Digite o valor do segundo segmento: '))
r3 = float(input('Digite o valor do terceiro segmento: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('Seus segmentos PODEM SIM formar um triangulo.')
    if r1 == r2 == r3:
        print('Um triangulo EQUILÁTERO: TODOS OS LADOS IGUAIS.')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('Um triangulo ISÓSCELES: DOIS LADOS IGUAIS.')
    else:
        print('Um triangulo ESCALENO: TODOS OS LADOS DIFERENTES.')
else:
    print('Seus segmentos NÃO PODEM formar um triangulo')
