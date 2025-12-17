#Desafio: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.


print('=====Desafio 32=====')
import datetime
ano = int(input('Digite o ano que deseje saber se é bissexto: '))
ano4 = ano % 4
ano100 = ano % 100
ano400 = ano % 400

'''if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto')
else:                                     #resolução do guanabara#
    print(f'O ano {ano} não é bissexto')'''

if ano4 == 0:
    if ano100 == 0:
        if ano400 == 0:
            print(f'O ano {ano} é bissexto')
        else:
            print(f'O ano {ano} não é bissexto')        #- minha resolução#
    else:
        print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto')

