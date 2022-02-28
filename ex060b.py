n = int(input('Digite o número para calcular o fatorial: '))
for c in range(n-1 , 0, -1):
    n = n * c
print('O fatorial desse número é: {}'.format(n))
