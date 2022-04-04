#Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
# quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input('Quantos km rodados?: '))
dias = int(input('Quantos dias alugados?: '))
preço = (60 * dias) + (0.15 * km)
print(f'Como você alugou por {dias} dias e rodou {km:.2f}km o valor a pagar é de: R${preço:.2f}')

