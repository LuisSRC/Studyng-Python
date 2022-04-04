#Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = str(input('Digite o seu nome: ')).strip().upper()
if 'SILVA' in nome:
    print('Tem SILVA no seu nome!')
else:
    print('Você não é um SILVA.')
