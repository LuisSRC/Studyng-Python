#Exercício Python 009: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
num = int(input('Digite um número para ver a sua tabuada: '))
for c in range(0, 11):
    print(f'{num} x {c} = {num * c}')
