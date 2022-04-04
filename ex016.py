#Exercício Python 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc
num = float(input('Digite um valor: '))
print(f'O número {num} tem como parte inteira: {trunc(num)}')
