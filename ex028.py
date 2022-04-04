#Exercício Python 028: Escreva um programa que faça o computador "pensar"
# em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi
# o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
computador = randint(0, 5)
print('Olá.. eu sou o seu computador...')
print('Vamos jogar um jogo de adivinhação?')
print('Eu irei pensar em um número entre 0 e 5, será que vc consegue adivinhar?')
jogador = int(input('Em que número eu pensei?'))
if computador == jogador:
    print('Parabéns!! Você me venceu.')
else:
    print(f'Que pena! você perdeu. Eu pensei no número: {computador}')
