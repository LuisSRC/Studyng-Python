maior = menor = 0
listanum = []
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c == 0:
        maior = listanum[c]
        menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print(f'Você digitou os valores: {listanum}')
print(f'O MAIOR número digitado foi: {maior} nas posições: ', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}...', end='')
print(f'E o menor número digitado foi: {menor} nas posições: ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}...', end='')

