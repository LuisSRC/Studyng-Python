lista = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado. Não será adicionado a lista.')
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('=-' * 40)
print(f'Você digitou os valores: {sorted(lista)}')
