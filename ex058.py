#Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.
from random import randint
print('Olá, sou seu computador...')
print('Irei pensar em um número entre 0 e 10...')
print('Será que você consegue adivinhar em que número pensei?')
computador = randint(0, 10)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual o seu palpite?: '))
    palpites += 1
    if jogador > computador:
        print('Menos...')
    elif jogador < computador:
        print('Mais...')
    elif jogador == computador:
        print('Parabéns. Você acertou!!')
        acertou = True
print(f'Você venceu com {palpites} tentativas.')
