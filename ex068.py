#Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
soma = vitoria = 0
print('-=' * 30)
print('VAMOS JOGAR PAR OU IMPAR')
print('-=' * 30)
while True:
    num = int(input('Diga um valor: '))
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    computador = randint(0, 10)
    print('-' * 30)
    soma = num + computador
    print(f'Você jogou {num} e o computador {computador}. Total de {soma}', end=' ')
    if soma % 2 == 0:
        print('DEU PAR')
    if soma % 2 == 1:
        print('DEU IMPAR.')
    print('-' * 30)
    if escolha == 'P' and soma % 2 == 0:
        print('Você ganhou!!')
        vitoria += 1
    elif escolha == 'I' and soma % 2 == 1:
        print('Você ganhou!!')
        vitoria += 1
    else:
        print('Você perdeu!!')
        break
    print('-' * 30)
print(f'GAME OVER! Você venceu {vitoria} vezes.')

