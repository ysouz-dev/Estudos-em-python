# Desafio: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.


print('=====Desafio 73=====')
tabela = ('Palmeira SP', 'Flamengo', 'Cruzeiro', 'Mirassol FC', 'Bahia', 'Botafogo RJ', 'Fluminense RJ', 'Vasco da Gama', 'São Paulo FC SP', 'Red Bull Bragantino SP', 'Corinthian SP', 'Gremio', 'Ceará SC', 'Internacional RS', 'Atlétco Mineiro MG', 'Santos FC SP', 'EC Vitória BA', 'EC Juventude RS', 'Fortaleza CE', 'Recife')
print(f'Os 5 primeiros colocados: \n{tabela[0:5]}')
print('-=-'*10)
print(f'Os 4 últimos colocados: \n{tabela[-1:-5:-1]}')
print('-=-'*10)
print(f'Todos os times em órdem alfabética: \n{sorted(tabela)}')
print('-=-'*10)
print(f'O time Red Bull Bragantino se encontra na posiçao de {tabela.index("Red Bull Bragantino SP") + 1} lugar')
