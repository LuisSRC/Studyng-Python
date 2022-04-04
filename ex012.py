#Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
produto = float(input('Digite o valor do produto: R$ '))
novovalor = produto - (produto * 5 / 100)
print(f'Com desconto de 5% o produto que custa R${produto:.2f} passará a custar R${novovalor:.2f}')

