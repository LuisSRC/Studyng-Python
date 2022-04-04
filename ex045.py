#Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('Olá, eu sou o seu computador...')
print('Vamos jogar Jokenpô?...')
print('''SUAS OPÇÕES:
[ 0 ]PEDRA
[ 1 ]PAPEL
[ 2 ]TESOURA''')
jogador = int(input('Qual a sua jogada?: '))
print(f'O computador escolheu: {itens[computador]}')
print(f'O jogador escolheu: {itens[jogador]}')
if computador == 0:
    if jogador == 0:
        print('EMPATE.')
    elif jogador == 1:
        print('JOGADOR VENCEU!!')
    elif jogador == 2:
        print('COMPUTADOR VENCEU!!')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU!!')
    elif jogador == 1:
        print('EMPATE.')
    elif jogador == 2:
        print('JOGADOR VENCEU!!')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCEU!!')
    elif jogador == 1:
        print('COMPUTADOR VENCEU!!')
    elif jogador == 2:
        print('EMPATE.')
else:
    print('JOGADA INVÁLIDA.')
