#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa
# que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JÚNIOR
#- Até 25 anos: SÊNIOR
#- Acima de 25 anos: MASTER
from datetime import date
atual = date.today().year
nascimento = int(input('Qual o ano de nascimento do atleta?: '))
idade = atual - nascimento
print(f'Em {atual} o atleta tem {idade} anos de idade.')
if idade <= 9:
    print('CATEGORIA: MIRIM.')
elif idade <= 14:
    print('CATEGORIA: INFANTIL.')
elif idade <= 19:
    print('CATEGORIA: JUNIOR.')
elif idade <= 25:
    print('CATEGORIA: SENIOR.')
else:
    print('CATEGORIA: MASTER.')

