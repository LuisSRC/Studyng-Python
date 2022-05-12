#Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
jogador = dict()
tot = []
time = list()
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou?: '))
    tot.clear()
    for c in range(0, partidas):
        tot.append(int(input(f'Quantos gols na partida {c+1}: ')))
    jogador['Gols'] = tot[:]
    jogador['Total'] = sum(tot)
    time.append(jogador.copy())
    resp = str(input('Quer Continuar? [S/N]: ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Quer Continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 30)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15} ', end='')
    print()
print('-' * 30)
while True:
    busca = int(input('Mostrar os dados de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO!! Não existe jogador com o código {busca}! ')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}:')
        for i, g in enumerate(time[busca]["Gols"]):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')

