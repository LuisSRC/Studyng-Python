from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    pi = str(input('Par ou Impar? [P/I]')).strip().upper()[0]
    while pi not in 'PI':
        pi = str(input('Par ou Impar? [P/I]')).strip().upper()[0]
    computador = randint(0, 10)
    soma = jogador + computador
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {soma}', end=' ')
    print('DEU PAR' if soma % 2 == 0 else 'DEU IMPAR')
    if pi == 'P':
        if soma % 2 == 0:
            print('VOCÊ VENCEU!!')
            v += 1
        else:
            print('Você perdeu!!')
            break
    if pi == 'I':
        if soma % 2 == 1:
            print('VOCÊ VENCEU!!')
            v += 1
        else:
            print('Você perdeu!!')
            break
print(f'GAME OVER !! Você venceu {v} vezes')




