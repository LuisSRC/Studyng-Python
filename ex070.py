#Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.
total = mais1000 = cont = barato = 0
nomebarato = ''
print('-' * 30)
print('LOJA DO CARVALHO')
print('-' * 30)
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    total += preco
    cont += 1
    if preco > 1000:
        mais1000 += 1
    if cont == 1 or preco < barato:
        nomebarato = nome
        barato = preco
    resp = ' '
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total da compra é de: R${total:.2f}')
print(f'{mais1000} produtos custam mais de R$1000,00')
print(f'O produto mais barato custa R${barato:.2f} e é o {nomebarato}')

