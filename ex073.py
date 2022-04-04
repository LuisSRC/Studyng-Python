#Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.
times = ('América - MG', 'Atlético - PR', 'Atlético - GO', 'Atlético - MG', 'Avaí', 'Botafogo',
         'Ceara - SC', 'Corinthias', 'Coritiba', 'Cuiaba', 'Flamengo', 'Fluminense','Fortaleza',
         'Goias', 'Internacional', 'Juventude', 'Palmeiras', 'Bragantino', 'Santos', 'São Paulo')
print(f'Os 5 primeiros colocados são: {times[0:5]}')
print(f'Os ultimos 4 colocados são: {times[-4:]}')
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'O time do São Paulo está na {times.index("São Paulo")+ 1} posição')
