#Desafio: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.


print('=====Desafio 26=====')
f = str(input('Digite uma frase qualquer: '))
f1 = f.upper().strip()
print(f"""A letra "A" aparece {f1.count('A')} vezes
        ela aparece a primeira vez na posição {f1.find('A')}
        ela aparece uma ultima vez na posição {f1.rfind('A')}""")
