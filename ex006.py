#Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
from math import sqrt
n = int(input('Digite um número: '))
print(f'O dobro de {n} é : {n * 2}')
print(f'O triplo de {n} é : {n * 3}')
print(f'A raiz quadrada de {n} é: {sqrt(n)}')
