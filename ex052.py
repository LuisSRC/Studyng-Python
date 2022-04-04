#Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
tot = 0
n = int(input('Digite um número para verificar se é primo: '))
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[33m', end='')
    print(f'{c}', end=' ')
print(f'\033[mO número {n} foi divisivel {tot} vezes')
if tot == 2:
    print('E por isso ele é primo.')
else:
    print('E por isso ele NÃO É PRIMO.')





