#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
opção = 0
while opção != 5:
    print(''' MENU DE OPÇÕES
        [ 1 ] SOMAR
        [ 2 ] MULTIPLICAR
        [ 3 ] MAIOR
        [ 4 ] NOVOS NÚMEROS
        [ 5 ] SAIR DO PROGRAMA''')
    opção = int(input('Qual a opção desejada?: '))
    sleep(0.5)
    print('=' * 30)
    if opção == 1:
        print(f'A soma entre: {n1} e {n2} é: {n1 + n2}')
        print('=' * 30)
    elif opção == 2:
        print(f'A multiplicação entre: {n1} e {n2} é: {n1 * n2}')
        print('=' * 30)
    elif opção == 3:
        if n1 > n2:
            print(f'{n1} é MAIOR')
        elif n1 < n2:
            print(f'{n2} é MAIOR')
        elif n1 == n2:
            print('Ambos são iguais.')
        print('=' * 30)
    elif opção == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
        print('=' * 30)
    elif opção == 5:
        print('PROGRAMA FINALIZADO.')
    else:
        print('Opção inválida.Tente novamente.')
        continue
