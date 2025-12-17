#Desafio: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

print('=====Desafio 24=====')
c = str(input('Digite o nome da sua cidade: '))
c1 = c.lower().strip().split()
print(f'A sua cidade {c.title().strip()}, começa com a palavra "Santo": {'santo' in c1[0]}')
