from time import sleep
from random import randint
computador = randint(0, 5)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5, tente adivinhar!')
print('-=-'*20)
jogador = int(input('Em que número você acha que eu pensei?: '))
print('PROCESSANDO....')
sleep(2)
if computador == jogador:
    print('PARABÉNS!! você me venceu!')
else:
    print('Você perdeu, eu pensei no número {} e não no número {}'.format(computador, jogador))










