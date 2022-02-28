times = ('Atlético - MG', 'Flamengo', 'Palmeiras', 'Fortaleza',
          'Corinthias', 'Bragantino', 'Fluminense', 'America - MG',
          'Atlético - GO', 'Santos', 'Ceara - SC', 'Internacional',
        'São Paulo', 'Atlético - PR', 'Cuiabá', 'Juventude',
        'Gremio', 'Bahia', 'Sport Recife', 'Chapecoense')
print(f'Os 5 primeiros colocados são: {times[:5]}')
print(f'Os ultimos 4 colocados são: {times[-4:]}')
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'O chapencoense está na {times.index("Chapecoense")+1}ª posição.')
