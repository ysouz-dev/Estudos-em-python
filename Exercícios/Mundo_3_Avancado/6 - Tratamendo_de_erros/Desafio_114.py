#Desafio: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.


print('=====Desafio 114=====')
import urllib.request

try:
    urllib.request.urlopen('https://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[1;31mError: não consegui acessar o site :(')
else:
    print('\033[1;32mConsegui acessar o site com sucesso!\033[m')