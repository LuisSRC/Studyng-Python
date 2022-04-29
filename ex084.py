#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.
temp = []
pessoas = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    pessoas.append(temp[:])
    temp.clear()
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 30)
print(f'Ao todo {len(pessoas)} pessoas foram cadastradas.')
print(f'O maior peso registrado foi {maior}KG, peso de: ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso registrado foi {menor}KG, peso de: ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')










