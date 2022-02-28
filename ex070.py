total = contmil = cont = menor = 0
barato = ''
while True:
    produto = str(input('Digite o nome do produto: '))
    preço = float(input('Preço R$: '))
    total += preço
    cont += 1
    if preço > 1000:
        contmil += 1
    if cont == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    resp = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        print('PROGRAMA FINALIZADO')
        break
print(f'O total das compras foi R${total:.2f}')
print(f'{contmil} produtos custam mais de R$1000,00')
print(f'E o produto mais barato foi {barato} que custa R${menor:.2f}')




