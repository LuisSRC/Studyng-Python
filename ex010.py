#Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos dólares ela pode comprar.
dinheiro = float(input('Quanto dinheiro você tem na carteira?: R$'))
print(f'Com {dinheiro} você pode comprar U${dinheiro / 5.16:.2f}')
