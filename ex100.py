#Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia()
# e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista
# e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
numeros = list()
def sorteia(lst):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        numeros.append(randint(1, 10))
    for valores in numeros:
        print(f'{valores} ', end='')
    print('PRONTO!')


def somaPar(lst):
    soma = 0
    for valor in lst:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {numeros}, temos {soma}.')


sorteia(numeros)
somaPar(numeros)






