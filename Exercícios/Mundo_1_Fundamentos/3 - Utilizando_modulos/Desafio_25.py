#Desafio: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

print('=====Desafio 25=====')
no = str(input('Digite seu nome completo: '))
no1 = 'Silva' in no.lower().strip().capitalize()
print(f"""Seu nome {no.title()}
        possui "Silva" no nome: {no1}""")