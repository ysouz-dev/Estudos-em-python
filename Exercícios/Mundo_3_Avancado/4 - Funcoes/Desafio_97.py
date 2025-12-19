# Desafio: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.


print('=====Desafio 97=====')
def escreva(msg):
    tamanho = len(msg) + 4
    print('~' * tamanho)
    print(f'{msg:^{tamanho}}')
    print('~' * tamanho)

escreva('Gustavo Guanabara')
escreva('Curso de Python')
escreva('CeV')