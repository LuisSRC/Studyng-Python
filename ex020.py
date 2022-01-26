import random
n1 = input('Digite o primeiro nome: ')
n2 = input('Digite o segundo nome: ')
n3 = input('Digite o terceiro nome: ')
n4 = input('Digite o quarto nome: ')
ordem = [n1, n2, n3, n4]
random.shuffle(ordem)
print('A ordem de apresentação é:')
print(ordem)

