#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
num = int(input('Digite o número para ver o seu fatorial: '))
print(f'Calculando {num}!= ', end='')
cont = num
f = 1
while cont > 0:
    print(f'{cont}', end='')
    f *= cont
    cont -= 1
    print(' x ' if cont >= 1 else ' = ', end='')
print(f)

