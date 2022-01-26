from random import choice
n1 = input('Digite o nome do Primeito Aluno: ')
n2 = input('Digite o nome do Segundo Aluno: ')
n3 = input('Digite o nome do Terceiro Aluno: ')
n4 = input('Digite o nome do Quarto Aluno: ')
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido foi')
print(escolhido)

