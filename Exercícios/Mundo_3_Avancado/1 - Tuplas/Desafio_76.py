# Desafio: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.


print('=====Desafio 76=====')
print('\033[1m--'*20)
print(f'{'Lista de Preços':^37}')
print('--'*20)
lista_de_produtos = ('Corte', 20, 'Corte Navalhado', 22, 'Barba', 10, 'Pigmentação', 5, 'Sobrancelha', 5, 'Reflexo Alinhado', 45, 'Platinado', 50, 'Colorimetria(cabelo todo)', 60,  'Colorimetria(luzes)', 55)
for produtos in range(0, len(lista_de_produtos)):
    if produtos % 2 == 0:
        print(f'{lista_de_produtos[produtos]:.<32}', end='')
    else:
        print(f'R$ {lista_de_produtos[produtos]:.2f}')
print('--'*20)
    