n = int(input('Digite um numero: '))
u = n//1 % 10
d = n//10 % 10
c = n//100 % 10
m = n//1000 % 10
print('Analisando o número digitado...')
print('A unidade vale: {}'.format(u))
print('A dezena vale: {}'.format(d))
print('A centena vale: {}'.format(c))
print('O milhar vale: {}'.format(m))

