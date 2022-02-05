pt = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))
décimo = pt + (10 - 1) * razão
for c in range(pt, décimo + razão, razão):
    print('{}'.format(c), end=' → ')
print('ACABOU!')
