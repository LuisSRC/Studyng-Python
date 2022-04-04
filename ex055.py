#Exercício Python 055: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.
maior = menor = 0
for pessoa in range(1, 6):
    peso = float(input('Peso (KG): '))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso registrado foi: KG{maior}')
print(f'O menor peso registrado foi: KG{menor}')

