#Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
atual = date.today().year
nascimento = int(input('Qual o ano de nascimento?: '))
idade = atual - nascimento
print(f'Em {atual} você tem {idade} anos de idade.')
if idade < 18:
    saldo = 18 - idade
    print(f'Ainda falta {saldo} anos para se alistar. Você se alistará em {atual + saldo}')
elif idade == 18:
    print('Você deve se alistar IMEDIATAMENTE.')
else:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado. Seu alistamento ocorreu em {atual - saldo}')




