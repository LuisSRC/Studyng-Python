#Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
while True:
    num = int(input('Quer ver a tabuada de qual valor?: '))
    print('-' * 30)
    if num < 0:
        print('PROGRAMA FINALIZADO!')
        break
    for c in range(1, 11):
        print(f'{num} X {c} = {num * c}')
    print('-' * 30)
