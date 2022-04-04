#Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.
num = (int(input('Digite um valor: ')),
       int(input('Digite um valor: ')),
       int(input('Digite um valor: ')),
       int(input('Digite um valor: ')))
print('Você digitou os números: ', end='')
for v in num:
    print(f'{v} ', end='')
print('\n')
print(f'O número 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 apareceu na {num.index(3)+1}ª posição.')
else:
    print('O número 3 não foi digitado nenhuma vez.')
print('Os números pares digitados são: ', end='')
for v in num:
    if v % 2 == 0:
        print(f'{v}', end=' ')
print('FIM')






