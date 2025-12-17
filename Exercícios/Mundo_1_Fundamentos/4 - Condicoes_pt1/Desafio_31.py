# Desafio: Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

print('=====Desafio 31=====')
print('Lembrando que para viagens mais longas acima de 200km o valor de R$ 0,50/km\n cai para R$ 0,45/km')
d = float(input('Qual a distância da viagem (em km)? '))
d1 = d * 0.50
d2 = d *0.45
if d > 200.0:
    print(f'O seu destino tem {d}km. Sua passagem fica em R${d2:.2f}  (R$0,45/KM)')
else:
    print(f'O seu destino tem {d}km. Sua passagem fica em R${d1:.2f}  (R$0,50/KM)')