#Desafio: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

i = '='
print('{} Desafio 8 {}'.format(5*i, 5*i))
met = float(input('Digite a metragem: '))
km = met/1000
hm = met/100
dam = met/10
dm = met*10
cent = met*100
mil = met*1000
print('{} metros corresponde a:\n {} quilômetro(s) \n {} hectômetro(s) \n {} decâmetro(s) \n {} decímetro(s) \n{:.0f} centímetro(s) \n{:.0f} milímetro(s)'.format(met, km, hm, dam, dm, cent, mil))
