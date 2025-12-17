#Desafio: Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas. 
# Quantas letras ao todo (sem considerar espaços).

print('=====Desafio 22=====')
n = str(input('Digite seu nome completo: '))
print(f"""Seu nome com todas as letras maiúsculas > {n.strip().upper()}
      Seu nome com todas as letras minúsculas > {n.strip().lower()}
      Seu nome possui {len(n.strip().replace(' ', ''))} letras (sem considerar espaços)
      Seu primeiro nome tem {len(n.split()[0])} letras""")
