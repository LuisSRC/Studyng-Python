#Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# e R$0,45 parta viagens mais longas.
viagem = int(input('Qual a distancia em km da viagem?'))
passagem = 0
if viagem <= 200:
    passagem = viagem * 0.50
else:
    passagem = viagem * 0.45
print(f'Para viajar {viagem}km, o valor da passagem será de R${passagem} ')