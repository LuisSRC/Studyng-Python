num = (int(input('Digite o primeiro valor: ')),
int(input('Digite o primeiro valor: ')),
int(input('Digite o primeiro valor: ')),
int(input('Digite o primeiro valor: ')))
print(f'Você digitou os números: {num}')
print(f'O número 9 apareceu {num.count(9)} vezes')
if 3 not in num:
    print('O número três não foi digitado.')
else:
    print(f'O primeiro número 3 se encontra na {num.index(3)+1}ª posição')
print('Os números PARES digitados são: ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')


