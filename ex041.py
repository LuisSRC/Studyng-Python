from datetime import date
nasc = int(input('Digite o ano de nascimento do atleta: '))
atual = date.today().year
idade = atual - nasc
print('O atleta que nasceu em {} tem {} anos'.format(nasc, idade))
if idade <= 9:
    print('CLASSIFICAÇÃO: MIRIM')
elif idade <= 14:
    print('CLASSIFICAÇÃO INFANTIL')
elif idade <= 19:
    print('CLASSIFICAÇÃO JUNIOR')
elif idade <= 25:
    print('CLASSIFICAÇÃO SENIOR')
else:
    print('CLASSIFICAÇÃO MASTER')

