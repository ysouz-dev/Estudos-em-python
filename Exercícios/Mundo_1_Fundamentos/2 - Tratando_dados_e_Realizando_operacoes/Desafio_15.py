#Desafio: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
#e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

print('=====Desafio 15=====')
km = float(input('Bom dia! Quantos km você percorreu com o veículo? '))
dias = int(input('Quantos dias ficou com ele? '))
total = (km*0.15)+(dias*60)
print('Então, você percorreu {}km em {} dias. Sua dívida é de R${:.2f}'.format(km, dias, total, ))
