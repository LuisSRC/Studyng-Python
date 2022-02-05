from datetime import date
atual = date.today().year
contMaior = 0
contMenor = 0
for p in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu?: '.format(p)))
    idade = atual - nasc
    if idade >= 21:
        contMaior += 1
    else:
        contMenor += 1
print('No grupo, {} pessoas são MAIORES de idade'.format(contMaior))
print('E também, {} pessoas são MENORES de idade'.format(contMenor))

