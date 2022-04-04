#Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
atual = date.today().year
maior = menor = 0
for c in range(1, 8):
    nasc = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
    idade = atual - nasc
    if idade > 18:
        maior += 1
    else:
        menor += 1
print(f'{maior} pessoas são MAIORES de idade.')
print(f'{menor} pessoas são menores de idade')
