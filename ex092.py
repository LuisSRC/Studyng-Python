#Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho
# e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO,
# o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
ficha = dict()
atual = datetime.now().year
ficha['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
ficha['Idade'] = atual - nasc
ficha['ctps'] = int(input('CTPS: '))
if ficha['ctps'] != 0:
    ficha['Contratação'] = int(input('Ano de Contratação: '))
    ficha['Salário'] = float(input('Salário: R$ '))
ficha['Aposentadoria'] = ficha['Idade'] + (ficha['Contratação'] + 35) - atual
print(ficha)







