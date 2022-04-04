#Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[  1  ] converter para BINÁRIO
[  2  ] converter para OCTAL
[  3  ] converter para HEXADECIMAL''')
resp = int(input('Sua opção: '))
if resp == 1:
    print(f'{num} em BINÁRIO é: {bin(num)}')
elif resp == 2:
    print(f'{num} em OCTAL é: {oct(num)}')
elif resp == 3:
    print(f'{num} em HEXADECIMAL é: {hex(num)}')

