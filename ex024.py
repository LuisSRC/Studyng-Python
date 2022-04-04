#Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
cid = str(input('Digite o nome da cidade: ')).strip().upper()
if 'SANTO' in cid:
    print('Essa cidade possui a palavra SANTO no nome.')
else:
    print('Essa cidade NÃO POSSUI a palavra SANTO no nome.')
