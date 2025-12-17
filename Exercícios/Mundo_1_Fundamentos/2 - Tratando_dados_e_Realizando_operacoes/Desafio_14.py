#Desafio: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

print('=====Desafio 14=====')
t = float(input('Informe a temperatura: °C '))
f = t*1.8+32
print('A temperatura de {}°C corresponde a {:.1f}°F!'.format(t, f))
