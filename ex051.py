#Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
pt = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão: '))
décimo = pt + (razao * 9)
for c in range(pt, décimo + razao, razao):
    print(c)
