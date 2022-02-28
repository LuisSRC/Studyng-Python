from random import randint
computador = randint(0, 10)
print('Olá, sou o seu computador, irei pensar em um número entre 0 e 10!')
print('Você consegue adivinhar que número eu pensei?')
palpites = 0
jogador = 0
while computador != jogador:
    palpites += 1
    jogador = int(input('Qual o seu palpite?: '))
    if jogador < computador:
        print('Mais.. tente mais uma vez: ')
    elif jogador > computador:
        print('Menos.. tente mais uma vez: ')
    elif jogador == computador:
        print('Parabéns!! você acertou!')
print('Você fez {} tentativas'.format(palpites))




