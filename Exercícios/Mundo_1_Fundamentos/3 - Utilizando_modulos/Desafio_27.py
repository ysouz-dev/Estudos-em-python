#Desafio: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

print('=====Desafio 27=====')
nom = str(input('Digite seu nome completo: '))
nom1 = nom.split()
print("""Seu nome completo: {}
        Tem o primeiro nome {} e o último {}. ficando {} {}.""".format(nom.title(), nom1[0], nom1[-1], nom1[0], nom1[-1] ))
