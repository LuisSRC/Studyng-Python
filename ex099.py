#Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
def maior(* num):
    cont = mai = 0
    tam = len(num)
    print('-=' * 30)
    print('Analisando os valores passados...')
    for n in num:
        print(f'{n}', end=' ')
    print(f'Foram informados {tam} valores ao todo.')
    for n in num:
        if cont == 0:
            mai = n
        else:
            if n > mai:
                mai = n
    print(f'O maior valor informado foi {mai}.')


maior(1, 5, 7, 9)
maior(1, 3, 5)
maior(6)
maior()

